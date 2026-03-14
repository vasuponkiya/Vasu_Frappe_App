// Copyright (c) 2026, Vasu and contributors
// For license information, please see license.txt

frappe.query_reports["Sales Order Detailed Report"] = {
	"filters": [

		{
			fieldname: "report",
			label: "Sales Order Report",
			fieldtype: "Link",
			options: "Sales Order Report",
			reqd: 1
		},

		{
			fieldname: "customer",
			label: "Customer",
			fieldtype: "Link",
			options: "Customer"
		},

		{
			fieldname: "from_date",
			label: "From Date",
			fieldtype: "Date"
		},

		{
			fieldname: "to_date",
			label: "To Date",
			fieldtype: "Date"
		}

	]
};