#send an email by using doc_events.
def sendEmail(doc,method):
    a = frappe.sendmail(
        recipients=["vasuponkiya14@gmail.com"],
        subject=f"New Student Created: {doc.name1}",
        message=f"""
            Hello vasu,<br><br>
            A new student record has been created.<br><br>
            <b>Name:</b> {doc.name1}<br>
           
            Regards,<br>
            Frappe System
        """,
        attachments=[frappe.attach_print(doc.doctype, doc.name, file_name=doc.name)],   # generate pdf dynamically
        reference_doctype="Student",
        reference_name=doc.name,
    )
    if a:
        frappe.msgprint("Email sent successfully")
    else:
        frappe.msgprint("Email sending failed")
    
#------------------------------------------------------------------
#------------------------------------------------------------------
#-----------For Customer Group Count--------------------------------
import frappe
from frappe import _

def customer_group_count_validate(doc, method=None):
   
    if not doc.customer_group:
        return

    try:
       
        total_count = frappe.db.count('Customer', filters={
            'customer_group': doc.customer_group
        })

        #for New Record
        if doc.is_new():
            total_count += 1

        frappe.db.sql("""
            UPDATE `tabCustomer`
            SET custom_customer_group_count = %s
            WHERE customer_group = %s
        """, (total_count, doc.customer_group))
        
        doc.custom_customer_group_count = total_count
        
    except Exception as e:
        frappe.db.rollback()
        frappe.log_error(message=frappe.get_traceback(), title="Customer Group Count Update Failed")
        frappe.msgprint(_("Could not update group count"))


#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#------------------------Task: Sort based on Sequence ID------------------------
#--------------------------Using Scheduler--------------------------------------

def fix_customer_group_sequence():

    # this query calculate groups and related sequence and then update in custom__group_sequence_id
    query = """
        UPDATE `tabCustomer` AS target
        INNER JOIN (
            SELECT 
                name, 
                ROW_NUMBER() OVER (
                    PARTITION BY customer_group 
                    ORDER BY creation ASC
                ) AS new_seq
            FROM `tabCustomer`
        ) AS source ON target.name = source.name
        SET target.custom__group_sequence_id = source.new_seq
        WHERE target.custom__group_sequence_id != source.new_seq 
           OR target.custom__group_sequence_id IS NULL
    """
    
    frappe.db.sql(query)
    
    frappe.db.commit()
    frappe.logger().info("Customer sequences set by Customer Group")


#-----------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
#----------Popup Msg for on save event for customer Doctype-------------------------

def show_Popup_on_save(doc, method=None):
    if doc.customer_name and doc.customer_primary_address:
        msg = f"""
            <b>Customer Name:</b> {doc.customer_name} <br>
            <b>Primary Address:</b> {doc.customer_primary_address} <br>
            <hr>
        """
        
        frappe.msgprint(
            msg=msg,
            title=_("Record Verification"),
            indicator="blue" 
        )

#-------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------
#--------Set Custom field for Sales Orders---------------------------------------------------

def set_default_discount_sale_order(doc, method):
    doc.custom_default_discount = 5
    frappe.msgprint(f" discount percentage is { doc.custom_default_discount} ")
