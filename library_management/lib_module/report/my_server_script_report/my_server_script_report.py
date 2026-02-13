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
	
	for d in cs_data:
		row = frappe._dict({
			'first_name' : d.first_name,
			'age': d.age,
			'dob': d.dob
		})
		data.append(row)
	
	chart_data = get_chart_data(data)
	# print(chart_data)
	chart_summary = get_chart_summary(data)

	return columns, data, None, chart_data, chart_summary


def get_columns():
	return [
		{
			"fieldname": 'first_name',
			"label": _("Name"),
			"fieldtype": 'Data',
			"width": '120'
		},
		{
			"fieldname": 'dob',
			"label": _("DOB"),
			"fieldtype": 'Date',
			"width": '120'
		},
		{
			"fieldname": 'age',
			"label": _("Age"),
			"fieldtype": 'Int',
			"width": '120'
		},
	]

def get_cs_data(filters):
	conditions = get_conditions(filters)
	data = frappe.get_all(
		doctype = "My Server Script",
		fields = ['first_name','age','dob'],
		filters = conditions,
		order_by = 'first_name desc'
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

    labels = ['Age <= 45', 'Age > 45']

    age_data = {
        'Age <= 45': 0,
        'Age > 45': 0
    }

    for entry in data:
		
        if entry.age <= 45:
            age_data['Age <= 45'] += 1
        else:
            age_data['Age > 45'] += 1

    chart = {
        "data": {
            "labels": labels,
            "datasets": [
                {
                    "name": "Age Status",
                    "values": [
                        age_data['Age <= 45'],
                        age_data['Age > 45']
                    ]
                }
            ]
        },
        "type": "pie",
        "height": 300
    }

    return chart



def get_chart_summary(data):
	if not data:
		return None
	
	age_below_45, age_above_45 = 0, 0

	for enrty in data:
		if enrty.age <= 45:
			age_below_45 += 1
		else:
			age_above_45 += 1
	return [
		{
			'value': age_below_45,
			'indicator': 'Green',
			'label': 'Age Below 45',
			'datatype': 'Int',
		},
		{
			'value': age_above_45,
			'indicator': 'Red',
			'label': 'Age Above 45',
			'datatype': 'Int',
		}
	]

