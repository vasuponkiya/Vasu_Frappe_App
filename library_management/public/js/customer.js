frappe.ui.form.on('Customer', {
    after_save: function (frm) {
        console.log("After save");

        if (frm.doc.customer_primary_address) {
            let msg = `<b>Customer Name:</b> ${frm.doc.customer_name} <br>
                <b>Primary Address:</b> ${frm.doc.customer_primary_address} <br>
                <hr>`;

            frappe.msgprint({
                message: msg,
                title: __("Record Verification"),
                indicator: "blue"
            });
        }
    }
});
