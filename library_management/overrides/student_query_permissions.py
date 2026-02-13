import frappe

def get_permission_query_conditions(user):

    if not user:
        user = frappe.session.user

    return "name != 'STD00028'"