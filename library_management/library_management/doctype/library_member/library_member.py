# Copyright (c) 2025, Vasu and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class LibraryMember(Document):
	def before_save(self):
		self.full_name = f'{self.first_name} {self.last_name or ""}'





#----------------------------------------------------------
#----------------------------------------------------------
#----------To Fatch All Articles from tabArticle Based on Author in Library Member
@frappe.whitelist()
def get_author_articles(author):
	articles = frappe.db.sql(f"""
						SELECT name FROM `tabArticle` WHERE author = '{author}';
						""", as_dict=True)
	
	return articles