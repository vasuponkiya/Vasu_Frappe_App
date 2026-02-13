# Copyright (c) 2026, Vasu and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class ClientsideScripts(Document):
	# def after_submit(self):
	# 	if self.first_name and self.last_name:
	# 		self.db_set("full_name", f'{self.first_name} {self.last_name}')
        

	pass
# @frappe.whitelist()
# def frappe_call(msg):
# 	import time
# 	time.sleep(5)
	
# 	# self.age = 36
# 	frappe.msgprint(msg)

# 	# return 'Hii, this msg from frappe_call method'
