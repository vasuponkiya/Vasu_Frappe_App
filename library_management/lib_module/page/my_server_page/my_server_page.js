frappe.pages['my-server-page'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Demo Page ',
		single_column: true
	});

	page.set_title('My Page');

	page.set_indicator('Done', 'green'); //red , blue , black

	let $btn = page.set_primary_action('New',()=>frappe.msgprint("You clicked btn"));

	let $btnOne = page.set_secondary_action('Refresh',()=>frappe.msgprint('Refresh btn'));

	page.add_menu_item("Send Email", ()=>frappe.msgprint("Mail Send"));
	// page.add_menu_item("cancel Email", ()=>frappe.msgprint("Mail cancel"));

	page.add_action_item("Delete", ()=>frappe.msgprint('data canceled'));

	let field = page.add_field({
		fieldtype: 'Select',
		fildname: 'status',
		label: 'Status',
		options:[
			'Oppend',
			'closed',
		],
		change(){
			frappe.msgprint(field.get_value());
		}
	})
	
	// $(frappe.render_template("my_server_page", {})).appendTo(page.body);
	
	$(frappe.render_template("my_server_page",{
		data:'Hii, this data Passing from HTML Page',
	})).appendTo(page.body)
}

	