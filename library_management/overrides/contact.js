frappe.ui.form.on('Contact', {
    refresh: function (frm) {
        frm.add_custom_button(__('Add'), function () {
            let d = new frappe.ui.Dialog({
                title: 'Enter details',
                fields: [
                    {
                        label: 'Enter Num',
                        fieldname: 'num',
                        fieldtype: 'Int'
                    }],
                size: 'small',
                primary_action_label: 'Submit',
                primary_action(values) {
                    // console.log(values);
                    let v = values['num']
                    // console.log(v);
                    d.hide();

                    frappe.call({
                        method: 'library_management.overrides.contact_api.call_api',
                        args: {
                            doc: v
                        },
                    }).then(
                        r => {
                            frm.set_value('first_name', r.massege)
                        }
                    )
                },

            });
            d.show();
        })
    }
});
