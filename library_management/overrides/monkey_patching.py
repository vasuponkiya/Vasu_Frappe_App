import frappe
from erpnext.buying.doctype.purchase_order.purchase_order import PurchaseOrder

def custom_validate(self):

    # just print msg while save the record
    frappe.msgprint("Hello! This message is coming from a Monkey Patch.")

