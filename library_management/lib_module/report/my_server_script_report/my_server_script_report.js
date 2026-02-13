// Copyright (c) 2026, Vasu and contributors
// For license information, please see license.txt

frappe.query_reports["My Server Script Report"] = {
	"filters": [
		{
			"fieldname": 'name',
			"label": __("My Server Script"),
			"fieldtype": 'Link',
			"options": 'My Server Script'
		},
		{
			"fieldname": 'dob',
			"label": __("DOB"),
			"fieldtype": 'Date'
		},
		{
			"fieldname": 'age',
			"label": __("Age"),
			"fieldtype": 'Int'
		}
	]
};
