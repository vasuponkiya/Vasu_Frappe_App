import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

def execute():
    # Call the local function
    create_new_student_fields()

def create_new_student_fields():
    custom_fields = {
        "Student": [
            {
                "fieldname": "custom_field_via_patch",
                "label": "Custom Field Via Patch",
                "fieldtype": "Select",
                "insert_after": "contact_no",
                "options":" \nA\nB\nC",
                "default": " "
            }
        ]
    }
    
    # Use the frappe utility to insert the fields
    create_custom_fields(custom_fields, ignore_validate=True)