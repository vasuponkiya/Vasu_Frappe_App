// This runs only for the Job Application Web Form
frappe.ready(function () {
    frappe.web_form.after_load = function () {
        frappe.msgprint("Form Loaded...");
    }
    frappe.web_form.on('applicant_name', (field, value) => {
        frappe.msgprint(__('Name Added'));
        console.log('Name:', value);

    });
});
