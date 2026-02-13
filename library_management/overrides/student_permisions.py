import frappe

def student_permission(doc, user=None, permission_type=None):
    # If user is not passed, get the current session user
    if not user:
        user = frappe.session.user

    roles = frappe.get_roles(user)

    print(f'\n\n\n{permission_type}\n\n\n')

    if 'Academics User' in roles:
        if permission_type == "delete":
            return False
        elif permission_type == "read":
            return False 
    return True