frappe.ready(function () {

	frappe.web_form.after_load = () => {
		// 1. Show the initial message
		// frappe.msgprint('Please Enter all values carefully!');

		// 2. Bind the field change event inside after_load
		// Ensure 'enable' is the correct fieldname in your Web Form
		frappe.web_form.on('enable', (field, value) => {
			frappe.msgprint('Hello User');
			console.log('Field "enable" changed to:', value);
		});
	};

});