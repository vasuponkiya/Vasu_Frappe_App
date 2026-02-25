import frappe
from frappe import _
from frappe.utils import get_link_to_form
from frappe.model.naming import getseries

from erpnext.controllers.item_variant import get_variant
from erpnext.stock.doctype.item.item import ItemVariantExistsError


# -----------------------------------
# Duplicate Variant Protection

def validate_item_variant(doc, method):

    if doc.is_new() and frappe.db.exists("Item", doc.name):
        link = get_link_to_form("Item", doc.name)
        frappe.throw(
            _("Item already exists: {0}").format(link)
        )

    if (
        doc.is_new()
        and doc.variant_of
        and doc.variant_based_on == "Item Attribute"
    ):

        args = {}
        for d in doc.attributes:
            if d.attribute_value:
                args[d.attribute] = d.attribute_value

        variant = get_variant(doc.variant_of, args, doc.name)

        if variant:
            variant_link = get_link_to_form("Item", variant)

            frappe.throw(
                _("Item Variant already exists: {0}").format(variant_link),
                ItemVariantExistsError,
            )


# -----------------------------------
# Auto Serial Number Creation

def create_serial_no(doc, method):

    if not doc.has_serial_no:
        return

    if not doc.item_code or not doc.item_group:
        return  

    item_prefix = doc.item_code[:2].upper()
    group_prefix = doc.item_group[:2].upper()

    prefix = f"{item_prefix}-{group_prefix}-"

    num = getseries(prefix, 4)
    serial_no = prefix + num

    if frappe.db.exists("Serial No", serial_no):
        return

    serial_doc = frappe.get_doc({
        "doctype": "Serial No",
        "serial_no": serial_no,
        "item_code": doc.item_code
    })

    serial_doc.insert(ignore_permissions=True)

