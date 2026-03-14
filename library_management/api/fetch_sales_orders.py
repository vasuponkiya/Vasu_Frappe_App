import frappe

@frappe.whitelist()
def fetch_sales_orders(docname):
    doc = frappe.get_doc("Records", docname)

    sales_orders = frappe.get_all(
        "Sales Order",
        filters={
            "company": doc.company,
            "transaction_date": ["between", [doc.from_date, doc.end_date]]
        },
        fields=[
            "name",
            "customer",
            "transaction_date",
            "grand_total",
            "status"
        ]
    )

    doc.orders = []

    for so in sales_orders:
        doc.append("orders", {
            "sales_order": so.name,
            "customer": so.customer,
            "transaction_date": so.transaction_date,
            "grand_total": so.grand_total,
            "status": so.status
        })

    doc.save()
    return "Sales Orders fetched successfully"