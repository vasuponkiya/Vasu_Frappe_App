# Copyright (c) 2026, Vasu and contributors
# For license information, please see license.txt

import frappe
from frappe import _, msgprint


def execute(filters=None):
	if not filters: filters = {}

	columns, data = [], []

	columns = get_columns()
	cs_data = get_cs_data(filters)

	if not cs_data:
		msgprint(_("No record found"))
		return columns, cs_data
	# print(cs_data)

	for d in cs_data:
		row = frappe._dict({
			'name1' : d.name1,
			'gender': d.gender,
			'date_of_birth': d.date_of_birth,
			'percentage': d.percentage
		})
		data.append(row)

	chart_data = get_chart_data(data)
	return columns, data, None, chart_data

def get_columns():
	return [
		{
			"fieldname": 'name1',
			"label": _("Name"),
			"fieldtype": 'Data',
			"width": '120'
		},
		{
			"fieldname": 'date_of_birth',
			"label": _("DOB"),
			"fieldtype": 'Date',
			"width": '120'
		},
		{
			"fieldname": 'gender',
			"label": _("Gender"),
			"fieldtype": 'Data',
			"width": '120'
		},
	]


def get_cs_data(filters):
	conditions = get_conditions(filters)
	data = frappe.get_all(
		doctype = "Student",
		fields = ['name1','gender','date_of_birth', 'percentage'],
		filters = conditions,
		order_by = 'name1 desc'
	)

	return data

def get_conditions(filters):
	conditions = {}

	for key, value in filters.items():
		if filters.get(key):
			conditions[key] = value
	
	return conditions

def get_chart_data(data):
    if not data:
        return None

    labels = ['Pass', 'Fail']

    percentage_data = {
        'Pass': 0,
        'Fail': 0
    }

    for entry in data:
        if entry.percentage <= 60:
            percentage_data['Fail'] += 1
        else:
            percentage_data['Pass'] += 1

    chart = {
        "data": {
            "labels": labels,
            "datasets": [
                {
                    "name": "Result Status",
                    "values": [
                        percentage_data['Fail'],
                        percentage_data['Pass']
                    ]
                }
            ]
        },
        "type": "pie",
		#bar,line, pie
        "height": 300
    }

    return chart
