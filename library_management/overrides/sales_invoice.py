import frappe
from erpnext.accounts.doctype.sales_invoice.sales_invoice import (
    make_delivery_note as core_make_delivery_note
)
from erpnext.accounts.doctype.sales_invoice.sales_invoice import SalesInvoice
from pycoingecko import CoinGeckoAPI


@frappe.whitelist()
def make_delivery_note(source_name, target_doc=None):
	# Call core ERPNext logic
    delivery_note = core_make_delivery_note(source_name, target_doc)

    if delivery_note and not delivery_note.get("custom_special_note"):
        delivery_note.custom_special_note = "Thank you for your business!"

    return delivery_note
    

    

class SalesInvoiceCustom(SalesInvoice):
    def get_crypto_price(self):
        cg =  CoinGeckoAPI()
        price = frappe._dict(cg.get_price(ids=['bitcoin', 'ethereum'], vs_currencies= self.currency))

        return {
            'bitcoin' : float(self.grand_total/price.bitcoin[self.currency.lower()]),
            'ethereum' : float(self.grand_total/price.ethereum[self.currency.lower()]),
            }
