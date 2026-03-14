# Copyright (c) 2026, Vasu and contributors
# For license information, please see license.txt

import re
import frappe
from frappe import _
from frappe.utils import getdate

def execute(filters=None):
    filters = filters or {}
    validate_filters(filters)

    columns = get_columns()
    data = get_data(filters)
    chart = get_chart(data)

    return columns, data, None, chart

def validate_filters(filters):
    from_date = filters.get("from_date")
    to_date = filters.get("to_date")
    
    if from_date and to_date:
        if getdate(from_date) > getdate(to_date):
            frappe.throw(_("From Date cannot be greater than To Date"))

    report = filters.get("report")
    if report:
        # Example: SOR-[2025-01-01-2026-03-12]-0025 -> Match 2025-01-01 and 2026-03-12
        match = re.search(r'\[(\d{4}-\d{2}-\d{2})-(\d{4}-\d{2}-\d{2})\]', report)
        if match:
            master_from_date = getdate(match.group(1))
            master_to_date = getdate(match.group(2))

            if from_date and getdate(from_date) < master_from_date:
                frappe.throw(_("From Date cannot be earlier than the report start date ({0})").format(match.group(1)))
                
            if to_date and getdate(to_date) > master_to_date:
                frappe.throw(_("To Date cannot be later than the report end date ({0})").format(match.group(2)))


def get_columns():

    return [
        {
            "label": _("Sales Order"),
            "fieldname": "sales_order",
            "fieldtype": "Link",
            "options": "Sales Order",
            "width": 150
        },
        {
            "label": _("Customer"),
            "fieldname": "customer",
            "fieldtype": "Link",
            "options": "Customer",
            "width": 180
        },
        {
            "label": _("Transaction Date"),
            "fieldname": "transaction_date",
            "fieldtype": "Date",
            "width": 120
        },
        {
            "label": _("Item"),
            "fieldname": "item_code",
            "fieldtype": "Link",
            "options": "Item",
            "width": 150
        },
        {
            "label": _("Quantity"),
            "fieldname": "qty",
            "fieldtype": "Float",
            "width": 100
        },
        {
            "label": _("Grand Total"),
            "fieldname": "grand_total",
            "fieldtype": "Currency",
            "width": 140
        },
        {
            "label": _("Status"),
            "fieldname": "status",
            "fieldtype": "Data",
            "width": 120
        },
        {
            "label": _("Delivery Status"),
            "fieldname": "delivery_status",
            "fieldtype": "Percent",
            "width": 150
        }
    ]


def get_data(filters):

    conditions = ""
    values = {}

    if filters.get("report"):
        conditions += " AND parent = %(report)s"
        values["report"] = filters.get("report")

    if filters.get("customer"):
        conditions += " AND customer = %(customer)s"
        values["customer"] = filters.get("customer")

    if filters.get("from_date"):
        conditions += " AND transaction_date >= %(from_date)s"
        values["from_date"] = filters.get("from_date")

    if filters.get("to_date"):
        conditions += " AND transaction_date <= %(to_date)s"
        values["to_date"] = filters.get("to_date")


    data = frappe.db.sql(f"""
        SELECT
            sales_order,
            customer,
            transaction_date,
            item_code,
            qty,
            grand_total,
            status,
            delivery_status
        FROM
            `tabSales Order Report Item`
        WHERE
            docstatus < 2
            {conditions}
        ORDER BY
            transaction_date DESC
    """, values, as_dict=True)


    return data


def get_chart(data):
    if not data:
        return None

    labels = []
    status_data = {}
    processed_orders = set()

    print(f'\n\n\n{len(data)}\n\n\n')
    
    for row in data:
        so = row.get("sales_order")
        # Ensure we don't double count the same SO
        if so in processed_orders:
            continue
        processed_orders.add(so)
        # print(f'\n\n\n{processed_orders}\n\n\n')
        customer = row.get("customer")
        status = row.get("status")

        if customer not in labels:
            labels.append(customer)

        if status not in status_data:
            status_data[status] = {}

        status_data[status][customer] = status_data[status].get(customer, 0) + 1

        # print(f'\n\n\n{status_data}\n\n\n')

    datasets = []
    for status, vals in status_data.items():
        datasets.append({
            "name": status,
            "values": [vals.get(customer, 0) for customer in labels]
        })

    # print(f'\n\n\n{datasets}\n\n\n')

    return {
        "data": {
            "labels": labels,
            "datasets": datasets
        },
        "type": "bar"
    }