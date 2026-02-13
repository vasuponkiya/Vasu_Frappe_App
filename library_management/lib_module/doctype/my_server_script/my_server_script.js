// Copyright (c) 2026, Vasu and contributors
// For license information, please see license.txt

frappe.ui.form.on("My Server Script", {
	refresh(frm) {

	},

    after_save: function(frm){
        if(frm.doc.first_name && frm.doc.last_name){
            frm.set_value("full_name", frm.doc.first_name +" "+frm.doc.last_name)
        }
    },

    // enable: function(frm){
    //     frm.call({
    //         doc: frm.doc,
    //         method:'frm_call',
    //         args:{
    //             msg:'hello',
    //         },
    //         callback: function(r){
    //             frappe.msgprint(r.message)
    //         }

    //     })
        
    // },

    // enable : function(frm){
    //     frappe.call({
    //         method : "library_management.lib_module.doctype.client_side_scripts.client_side_scripts.frappe_call",
    //         args:{
    //             msg : "hello",
    //         },
    //         freeze : true,
    //         freeze_message : __('calling frappe_call method'),
    //         callback: function(r){
    //             frappe.msgprint(r.message)
    //         }

    //     })
    // }
    
});
