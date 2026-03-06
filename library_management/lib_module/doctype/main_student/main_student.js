// Copyright (c) 2026, Vasu and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Main Student", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on('Child Item', {
    configure_parameters: function (frm, cdt, cdn) {
        let row = locals[cdt][cdn];


        // 1. Create the Dialog
        let d = new frappe.ui.Dialog({
            title: 'Configure Item Parameters',
            fields: [
                {
                    label: 'Item Parameters',
                    fieldname: 'item_parameters',
                    fieldtype: 'Table',
                    cannot_add_rows: false,
                    in_place_edit: true,
                    data: JSON.parse(row.grandchild_item || "[]"), // Load existing data
                    fields: [
                        {
                            fieldtype: 'Data',
                            fieldname: 'item_color',
                            label: 'Item Color',
                            in_list_view: 1
                        },
                        {
                            fieldtype: 'Data',
                            fieldname: 'item_size',
                            label: 'Item Size',
                            in_list_view: 1
                        }
                    ]
                }
            ],
            primary_action_label: 'Save',
            primary_action(values) {
                // 2. Save the Dialog table data back to the hidden JSON field
                frappe.model.set_value(cdt, cdn, 'grandchild_item', JSON.stringify(values.item_parameters));
                d.hide();
                frappe.msgprint(__('Grandchild Item saved to row'));
            }
        });


        d.show();
    }
});