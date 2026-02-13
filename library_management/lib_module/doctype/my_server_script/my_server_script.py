# Copyright (c) 2026, Vasu and contributors
# For license information, please see license.txt
import frappe
from frappe import _
from frappe.model.document import Document


class MyServerScript(Document):
	pass
	
	#-----------------------------Event Handlers-----------------------------#

	# def validate(self):
	# 	frappe.msgprint("Validation successful for MyServerScript.")
	# def before_validate(self):
	# 	frappe.msgprint("before_Validation successful for MyServerScript.")

	# def before_save(self):
	# 	frappe.msgprint("You can`t before_save this doc")
		
	# def after_save(self):
	# 	frappe.msgprint("You can`t after_save this doc")


	# def before_insert(sefl):
	# 	frappe.throw("This is massage from 'before insret' Event ")
	
	# def after_insert(self):
	# 	frappe.msgprint("This Msg from 'after insert' Event")

	# def on_update(self):
	# 	frappe.msgprint("this is msg while update form")

	# def before_submit(self):
	# 	frappe.throw("Can`t submit this form")

	# def on_submit(self):
	# 	frappe.msgprint("Submmited successfilly")

	# def before_cancel(self):
	# 	frappe.msgprint("Before Cancel Event")

	# def on_cancel(self):
	# 	frappe.msgprint("On Cancel Event, while cancel doc")

	# def on_trash(self):
	# 	frappe.msgprint("You called 'on_trash' while deleting doc")

	# def after_delete(self):
	# 	frappe.msgprint("You have deleted this doc")


	#-----------------------Values Fetching----------------------------------#

	# def validate(self):
	# 	if (self.first_name and self.last_name):
	# 		frappe.msgprint(
	# 			_("My Full Name is {0}").format(
	# 				f"{self.first_name} {self.last_name}"
	# 			)
	# 		)
	
	# def validate(self):
	# 	for row in self.get('family_member'): # iterate over child tables rows
	# 		frappe.msgprint(
	# 			_("Family Member`s Name is {0} and relation is {1}").format(
	# 				row.name1,row.relations)
	# 		)

	
	# def validate(self):
	# 	if self.first_name and self.last_name:
	# 		self.full_name = f' {self.first_name}  {self.last_name}'
	# 	else:
	# 		self.full_name = None
		
		#self.get_document()

		#self.new_documents()
		

		


#--------doc.get()----------------------------
	# def get_document(self):
		
	# 	Doc = frappe.get_doc("Client side Scripts", self.client_script)

	# 	if(Doc.first_name):
	# 		# print("True")
	# 		Doc.first_name = "Raj"
	# 		# print(Doc.first_name)
	# 		Doc.save()

	# 	frappe.msgprint("this msg from client side, name is {0} and age is {1}".format(
	# 		Doc.first_name, Doc.age
	# 	))

	# 	#Itorate over the client scripts's child table which is Family Members
	# 	for row in Doc.get('family_member'):
	# 		frappe.msgprint(_(
	# 			"{0} Family Member's name is {1} and realation is {2} "
	# 		).format(row.idx, row.name1, row.relations))

	# def before_insert(self):
	# 	last_script = frappe.get_last_doc("My Server Script")

	# 	if last_script:
	# 		print(last_script.first_name)
	# def before_insert(self):
	# 	demo = frappe.get_cached_doc("My Server Script",'SR-0024')
	# 	print(demo.first_name)
#-----------doc.new_doc('doctype_name')------------------------------------

	# def new_documents(self):
	# 	Doc = frappe.new_doc("Client side Scripts")
	# 	Doc.first_name = 'jknrfiur'
	# 	Doc.last_name = 'patel'

	# 	Doc.append("family_member",{
	# 		"name1":"rhweyr",
	# 		"relations":"Brother",
	# 		"age" : 23
	# 	})

	# 	Doc.insert()


#------------frappe.detele_doc(doctype, name)--------------------------------


	# def validate(self):
	# 	frappe.delete_doc("Client side Scripts", 'CS-0018')


#------------doc.db_set()----and----doc.get_title()----------------------------------------------

	# def validate(self):
	# 	self.db_set_document()
	# 	# print(self.get_title()) #------> print title of main document

	# def db_set_document(self):
	# 	Doc = frappe.get_doc("Client side Scripts", 'CS-0019')
	# 	# print(Doc.get_title())  3--------------> print title of Child Document
	# 	Doc.db_set('first_name','ruhr', notify=True)


#---------------------Databse API------------------------------------
#----------------------frappe.db.get_list()--------------------------
#frappe.db.get_list(doctype, filters, or_filters, fields, order_by, group_by, start, page_length)

	# def validate(self):
	# 	self.get_list() 
	

	# def get_list(self):
	# 	Doc = frappe.db.get_list("Client side Scripts",
	# 			filters= {
	# 				'enable' : 1
	# 			},
	# 			fields = ['first_name', 'age'])

	# 	for obj in Doc:
	# 		frappe.msgprint(_("Parent First Name is {0} and age is {1}").format(obj.first_name, obj.age))


#---------------frappe.db.get_value()---------------------------
# frappe.db.get_value(doctype, name, fieldname) or frappe.db.get_value(doctpye, filters, fieldname)


	# def validate(self):
	# 	self.get_document_value() 
	
	# def get_document_value(self):
	# 	first_name, age = frappe.db.get_value("Client side Scripts", 'CS-0019', ['first_name', 'age'])
	# 	frappe.msgprint(_("the parent first_name is {0} and age is {1}").format(first_name, age))


#--------------------frappe.db.set_value()-----------------------------------------
# frappe.db.set_value(doctype, name, fieldname, vaule)


	# def validate(self):
	# 	self.set_values()
	
	# def set_values(self):

	# 	frappe.db.set_value("Client side Scripts", 'CS-0019', 'age', 24)

	# 	self.get_document_value()




#------------------frappe.db.exists()--------------------------------------------------


	# def validate(self):
		# present = frappe.db.exists("Client side Scripts", 'CS-0023')

		# if present:
		# 	frappe.msgprint(_("The Document existed in Database"))
		# else:
		# 	frappe.msgprint(_("The Document isnot present in Databse"))



#-----------------------frappe.db.count()----------------------------------------------
#frappe.db.count(doctype, filters)


	# def validate(self):

	# 	no_of_doc = frappe.db.count("Client side Scripts", {'enable':1}) 

	# 	frappe.msgprint(_("the totale no. Of Enable Doc is {0}").format(no_of_doc))



#--------------------frappe.db.sql---------------------------------------------------
# frappe.db.sql(query, filters, as_dict)


	# def validate(self):
	# 	self.sql_query() 
	
	# def sql_query(self):

	# 	my_data = frappe.db.sql(
	# 			"""
	# 			SELECT first_name, age
	# 			FROM `tabClient side Scripts`
	# 			WHERE enable = 1;
	# 			""",
	# 			as_dict =1
	# 	)

	# 	for data in my_data:
	# 		frappe.msgprint(_("from Selected data, first_name is {0} and age is {1} "
	# 						).format(data.first_name, data.age))


#-------------------call()method----------------------------------------

	# @frappe.whitelist()
	# def frm_call(self, msg):

	# 	import time 
	# 	time.sleep(5)

	# 	self.age = 36
		# frappe.msgprint(msg)
		
		# return 'hii, this msg from frm_call method'
