
import frappe

@frappe.whitelist(allow_guest=True)
def get_customers_groupwise(**data):
    try:
        # Filter applied from code
        customers = frappe.get_all(
            "Customer",
            filters={"customer_group": data.get("filter_customer_group") }, 
            fields=["customer_name", "customer_group","custom__group_sequence_id"],
            order_by="custom__group_sequence_id asc"
        )
        return customers
    except Exception as e:
        return {"error": str(e)}