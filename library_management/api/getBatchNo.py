import frappe

@frappe.whitelist()
def get_batch_serial_rows(item):
    return frappe.get_all(
        "Item Child",
        filters={"item": item},
        fields=["batch_no", "serial_no"]
    )

@frappe.whitelist()
def delete_all(item):
    frappe.db.delete("Item Child", {"item": item})
    frappe.db.commit()
    return "Deleted"