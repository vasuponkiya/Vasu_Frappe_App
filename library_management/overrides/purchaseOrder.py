import frappe
from frappe import _
from erpnext.buying.doctype.purchase_order.purchase_order import PurchaseOrder

class CustomPurchaseOrder(PurchaseOrder):
    def validate(self):

        super().validate()

        if(not self.custom_expected_delivery_date):
            frappe.throw(_("Please Provide Expected delivery date"))
    