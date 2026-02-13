import frappe

@frappe.whitelist(allow_guest=True)
def tl_bot_webhook(**kwrgs):
    frappe.log_error("New TG Bot Message",frappe.form_dict)
