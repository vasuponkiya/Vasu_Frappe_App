// Copyright (c) 2026, Vasu and contributors
// For license information, please see license.txt

frappe.ui.form.on("Client side Scripts", {

    //---------------------Events-------------------------------------
	// refresh(frm) {
    //     frappe.msgprint("Hello, Refresh call");
    //     // console.log("Refreshed");
        
    //     // frappe.throw("you've got an Error");
        
	// },
    // setup(frm){
    //     frappe.msgprint("you have called setup event")
    //     console.log("setup event");
        
    // },

    // onload: function(frm){
    //     frappe.msgprint("Hello from onloan Event");
    //     console.log("onload");
    // },

    // validate: function(frm) {
    //     frappe.msgprint("Hello, from 'validate' event");
    //     console.log("validate");
        
    // },

    // before_save: function(frm) {
    //     frappe.msgprint("Hello, from 'before save ' event");
    //     console.log("before save");
        
    // },

    // after_save: function(frm){
    //     frappe.msgprint("Hello, from 'after save' event");
    //     console.log('after save');
        
        
    // },

    // enable: function(frm){
    //     frappe.msgprint("Hello, from Enable Event")
    // }

    // age: function(frm){
    //     frappe.msgprint("You change the age value")
    // }

    // family_member_on_form_rendered: function(frm){
    //     frappe.msgprint('you have added a row in chile table')
    // }


    // before_submit: function(frm){
    //     frappe.msgprint("This is an before submit error");
    //     console.log('before submit');
        
        
    // },

    // on_submit: function(frm){
    //     frappe.msgprint("Form submitted, using after submit event ");
    //     console.log('on submit');
        
    // },

    // before_cancel: function(frm){
    //     frappe.msgprint("msg from before cancel")
            
    // },

    // after_cancel: function(frm){
    //     frappe.msgprint("You have cancelled this form");
            
    // },

    //--------------------------------Values Fetching------------------

    // after_save: function(frm){
    //     // frappe.msgprint(__("The full name is '{0}'",
    //     //     [frm.doc.first_name +" "+frm.doc.last_name]))
    
    //     for(let row of frm.doc.family_member){
    //         frappe.msgprint(__("'{0}' The Family Member name is '{1}' and Relation is '{2}'",
    //             [row.idx, row.name1, row.relations]
    //         ))

    //         }
    // },
    // refresh: function(frm){
        
    //     //frm.set_intro('Now you can create new DocType for client scripts')
    //     if(frm.is_new()){
    //         frm.set_intro("Now you can create new DocType for client scripts")
    //     }
            
    // },

    

    //--------------------Set Values --------------------------
    // after_save(frm){
    //     if(frm.doc.first_name && frm.doc.last_name){
    //         frm.set_value("full_name", frm.doc.first_name +" "+frm.doc.last_name)
    //     }
        // let row = frm.add_child("family_member",
        //     {
        //         name1:"riuef neirh",
        //         relations: "Father",
        //         age: 45,
        //     }
        // )
    // },

    // enable: function(frm){
    //     frm.set_df_property('first_name', 'reqd', 1);

    //     //for mendatory we can aslo use this method 
    //     frm.toggle_reqd('age',true)

    //     // set read_only fields if enable is true
    //     // frm.toggle_enable('mobile',true)
        

    // },

    //--------------add_custom_button-----------------------------------------------------------
    // refresh:function(frm) {
    //     // frm.add_custom_button("ClickMe",()=>{
    //     //     frappe.msgprint("Youhave cliked the button")
    //     // })
        
    //     // frm.add_custom_button("ClickMe_1",()=>{
    //     //     frappe.msgprint(__("Youhave cliked the button clickme_1"));
	//     // },'clickMe')

    //     // frm.add_custom_button("ClickMe_2",()=>{
    //     //     frappe.msgprint(__("Youhave cliked the button clickme_2"));
	//     // },'clickMe')

    // }
});

frappe.ui.form.on("Family Members",{
    // name1: function(frm){
    //     frappe.msgprint("Name field name is triggered in child table")
    // },

    // -----------------------------------------
    // age(frm, cdt, cdn){
    //    frappe.msgprint("age Values changed using age event in child table ") 
    // },

    //--------------------------------------------------
    // family_member_add(frm, cdt, cdn){
    //     // frm: current client_side_scripts form
    //     // cdt: child DocType 'Family Members'
    //     // cdn: child docname 

    //     frappe.msgprint('A row has been added to the child  table');
    // },

    //------------------------------------------------------

    // before_family_member_remove(frm, cdt, cdn){

    //     frappe.throw("A row can't remove from the child  table");
    // },

    //------------------------------------------------------
    // family_member_remove(frm, cdt, cdn){
    //     frappe.msgprint("A row removed from the child  table");
    // }

    // form_render(frm, cdt, cdn){
    //     frappe.msgprint("form open in Edit for child table")
    // }

});
