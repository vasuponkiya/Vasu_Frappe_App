// Copyright (c) 2026, Vasu and contributors
// For license information, please see license.txt

frappe.ui.form.on("Student", {
    refresh: function (frm) {
        if (!frm.is_new()) {

            // Check if Employee already exists for this Student
            if (frm.doc.has_employee) {
                frm.add_custom_button(__('Create Employee'), () => {
                    frappe.msgprint("Employee already exists for this Student");
                    return;
                }, __("Create"));
            } else {
                // Show Create Employee button only if not created
                frm.add_custom_button(__('Create Employee'), () => {

                    frappe.call({
                        method: "library_management.lib_module.doctype.student.student.make_new_Employee",
                        args: {
                            doc: frm.doc
                        },
                        callback: function (r) {
                            if (!r.exc && r.message) {

                                let visit_link = `
                                    <a href="#" onclick="frappe.set_route('Form', 'Employee', '${r.message.employee}')">
                                        Visit
                                    </a>
                                    `;

                                frappe.msgprint(
                                    r.message.message + ": " + r.message.employee + " " + visit_link
                                );

                                // Set has_employee true
                                frm.set_value("has_employee", 1);

                                // Save the form so value persists
                                frm.save();
                            }
                        }
                    });

                }, __("Create"));
            }
        }
    },

    validate: function (frm) {

        let today = frappe.datetime.nowdate();

        // Date of Birth validation
        if (frm.doc.date_of_birth && frm.doc.date_of_birth >= today) {
            frappe.throw(__('Date of Birth cannot be in the future'));
        }

        // Enrollment Date validation
        if (frm.doc.enrollment_date && frm.doc.enrollment_date > today) {
            frappe.throw(__('Enrollment Date cannot be in the future'));
        }

        // age calculation from DOB
        if (frm.doc.date_of_birth) {
            let dob = new Date(frm.doc.date_of_birth);
            let now = new Date();

            let age = now.getFullYear() - dob.getFullYear();
            let monthDiff = now.getMonth() - dob.getMonth();

            if (monthDiff < 0 || (monthDiff === 0 && now.getDate() < dob.getDate())) {
                age--;
            }

            frm.set_value('age', age);
        }

        //Email validation
        const email = (frm.doc.email_id || '').trim();
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (email && !emailPattern.test(email)) {
            frappe.msgprint(__('Please enter a valid Email'));
            frappe.validated = false;
        }

        // Child table marks validation
        (frm.doc.subjects || []).forEach(row => {
            if (row.marks < 0 || row.marks > row.total_marks) {
                frappe.throw(
                    __('Invalid marks for subject {0}', [row.subject_name])
                );
            }
        });

    }
});



