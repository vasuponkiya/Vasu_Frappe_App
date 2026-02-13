import frappe

def before_migrate():
    print("\n\n\n before_migrate hook executed \n\n\n")


def after_migrate():
    print("\n\n\n after_migrate hook executed \n\n\n")
