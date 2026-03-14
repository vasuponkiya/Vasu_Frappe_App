import frappe
from frappe.utils import nowdate



def genarate_OP(doc, method = None):

    try :

        if not doc.material_request_type == 'Purchase':
            return
        
        # Only proceed if Approved checkbox is checked
        if not doc.custom_approved_for_po:
            frappe.msgprint("Material Request submitted but not Approved. PO not created.")
            return

        # Ensure Supplier is selected
        if not doc.custom_supplier:
            frappe.throw("Supplier must be selected before submitting an Approved Material Request.")

        # Create Purchase Order
        po = frappe.new_doc("Purchase Order")
        po.supplier = doc.custom_supplier
        po.company = doc.company
        po.schedule_date = nowdate()

        for item in doc.items:
            po.append("items", {
                "item_code": item.item_code,
                "item_name": item.item_name,
                "description": item.description,
                "qty": item.qty,
                "uom": item.uom,
                "rate": item.rate,
                "schedule_date": nowdate(),
            })

        po.insert(ignore_permissions=True)
        po.submit()

        # Send Email to Supplier
        supplier_email = po.contact_email

        if supplier_email:
            frappe.sendmail(
                recipients=[supplier_email],
                subject=f"New Purchase Order {po.name}",
                message=f"""
                Dear Supplier,<br><br>
                A new Purchase Order <b>{po.name}</b> has been generated
                against Material Request <b>{doc.name}</b>.<br><br>
                Please review it in the system.<br><br>
                Regards,<br>
                {doc.company}
                """,
                reference_doctype="Purchase Order",
                reference_name=po.name
            )

        frappe.msgprint(f"Purchase Order {po.name} created successfully.")
        

    except:
        frappe.log_error("PO Creation Error",frappe.get_traceback())
        frappe.throw("PO not created, some Error occured please check the log")