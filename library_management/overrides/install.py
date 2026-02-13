import frappe

def before_install():
    # runs BEFORE app is installed
    print("\n\n\n Before installing App \n\n\n\n")

def after_install():
    # runs AFTER app is installed
    frappe.msgprint("\n\n\n App installed successfully! \n\n\n")
