import frappe

@frappe.whitelist(allow_guest=True)
def create_student(**data):
	try:
		# if isinstance(data, str):
		# 	data = frappe.parse_json(data)

		student = frappe.get_doc({
			"doctype": "Student",
			"name1": data.get("student_name"),
			"student_id": data.get("student_id"),
			"date_of_birth": data.get("date_of_birth"),
			"gender": data.get("gender"),
		})


		for row in data.get("subjects", []):
			student.append("subjects", {
				"subject_name": row.get("subject_name"),
				"marks": row.get("marks"),
				"total_marks":row.get("total_marks")
			})

		# --- Save ---
		student.insert(ignore_permissions=True)
		return {
			"status": "success",
			"student_name": student.name
		}
	
	except Exception as e:
		return {"error": str(e)}
