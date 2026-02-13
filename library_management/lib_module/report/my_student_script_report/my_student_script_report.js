// Copyright (c) 2026, Vasu and contributors
// For license information, please see license.txt

frappe.query_reports["My Student Script Report"] = {
	"filters": [
		{
			"fieldname": 'name',
			"label": __("Student"),
			"fieldtype": 'Link',
			"options": 'Student'
		},
		{
			"fieldname": 'date_of_birth',
			"label": __("DOB"),
			"fieldtype": 'Date'
		},
		{
			"fieldname": 'gender',
			"label": __("Gender"),
			"fieldtype": 'Data'
		}
	]
};
