frappe.ready(function () {

	frappe.web_form.after_load = function () {
		frappe.msgprint("Form Loaded...");
	}();

	frappe.web_form.on('name1', (field, value) => {
		frappe.msgprint(__('Name Added'));
		console.log('Field "enable" changed to:', value);

	});

	frappe.web_form.on('date_of_birth', (field, value) => {
		if (value) {
			dob = new Date(value);
			var today = new Date();
			var age = Math.floor((today - dob) / (365.25 * 24 * 60 * 60 * 1000));

			frappe.web_form.set_value('age', age)
		}
	});

	frappe.web_form.validate = () => {
		const email = frappe.web_form.get_value('email_id');
		const mobileNum = frappe.web_form.get_value('contact_no');

		const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
		if (email && !emailPattern.test(email)) {
			frappe.msgprint(__('Please enter a valid Email'));
			return false;
		}

		const mobilePattern = /^[0-9]{10}$/;
		if (mobileNum && !mobilePattern.test(mobileNum)) {
			frappe.msgprint(__('Please enter a valid 10-digit Contact Number'));
			return false;
		}

		return true;

	}

});
