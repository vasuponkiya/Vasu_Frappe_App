// Copyright (c) 2026, Vasu and contributors
// For license information, please see license.txt

frappe.ui.form.on("Author", {
	refresh(frm) {
        frm.set_value("author_full_name", frm.doc.author_first_name + " " + frm.doc.author_last_name)

	},

});
