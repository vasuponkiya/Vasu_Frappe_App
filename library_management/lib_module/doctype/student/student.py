# Copyright (c) 2026, Vasu and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document


class Student(Document):

    def validate(self):
        try:
            total = 0
            max_total = 0

            # Loop through child table 'subjects'
            for row in self.subjects:
                if row.marks is not None and row.total_marks:
                    total += row.marks
                    max_total += row.total_marks

            # Calculate percentage
            self.percentage = (total / max_total * 100) if max_total > 0 else 0

            # Assign status
            if self.percentage < 33:
                self.status = "Failed"
            elif 33 <= self.percentage <= 50:
                self.status = "Pass"
            else:
                self.status = "Excellent"

        except Exception as e:
            frappe.log_error(message=frappe.get_traceback(), title="Student Validation Error")
            frappe.throw(_("An error occurred during calculation: {0}").format(str(e)))
        

    #To delete Linked Employee
    # def on_trash(self):
    #     frappe.db.delete("Employee", {
    #         "custom_student": self.name
    #     })


#Create Employee Record from Student Doctype using custom button
@frappe.whitelist()
def make_new_Employee(doc):
    logger = frappe.logger("Employee Creation")
    try :
        doc = frappe.parse_json(doc)


        # Create Employee
        employee = frappe.new_doc("Employee")
        employee.first_name = doc.get("name1")
        employee.gender = doc.get("gender")
        employee.date_of_birth = doc.get("date_of_birth")
        employee.date_of_joining = doc.get("enrollment_date")
        employee.custom_student = doc.get("name")

        employee.insert(ignore_permissions=True)

        return {
            "message": "Employee created successfully",
            "employee": employee.name
        }
    except Exception:
        frappe.log_error("Employee creation Error",frappe.get_traceback(
    
        ))
        frappe.throw("Employee creation Error please chec Error log")


@frappe.whitelist()
def getStdList():
    std_list = frappe.db.get_list(
            "Student",
            filters = {"status": "Failed"},
            fields = ["name1", "student_id", "gender"]
        )
    print(std_list)