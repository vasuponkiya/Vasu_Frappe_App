# Copyright (c) 2026, Vasu and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document


class SalesOrderReport(Document):


	@frappe.whitelist()
	def generate_report_data(self):

		self.report_items = []

		conditions = ""
		filters = {
			
			"company": self.company,
			"from_date": self.from_date,
			"to_date": self.to_date
		}

		conditions += " AND so.company = %(company)s"
		conditions += " AND so.transaction_date BETWEEN %(from_date)s AND %(to_date)s"

		data = frappe.db.sql("""
			SELECT
				so.name as sales_order,
				so.customer,
				so.transaction_date,
				soi.item_code,
				soi.qty,
				so.grand_total,
				so.status,
				so.per_delivered
			FROM
				`tabSales Order` so
			JOIN
				`tabSales Order Item` soi
			ON
				soi.parent = so.name
			WHERE
				so.docstatus = 1
				{conditions}
		""".format(conditions=conditions), filters, as_dict=True)

		if not data:
			frappe.msgprint(_("No Sales Orders found."))
			return

		for row in data:
			self.append("report_items", {
				"sales_order": row.sales_order,
				"customer": row.customer,
				"transaction_date": row.transaction_date,
				"item_code": row.item_code,
				"qty": row.qty,
				"grand_total": row.grand_total,
				"status": row.status,
				"delivery_status": row.per_delivered
			})
		