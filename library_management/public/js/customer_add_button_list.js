frappe.listview_settings['Customer'] = {
    onload: function (listview) {
        listview.page.add_inner_button('Update Customer', () => {
            frappe.msgprint('Button clicked!');
        });
    }
};
