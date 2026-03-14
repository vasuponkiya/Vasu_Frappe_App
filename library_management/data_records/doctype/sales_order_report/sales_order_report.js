// Copyright (c) 2026, Vasu and contributors
// For license information, please see license.txt

frappe.ui.form.on("Sales Order Report", {
    refresh(frm) {
        if (frm.doc.report_items && frm.doc.report_items.length > 0) {
            frm.set_df_property("from_date", "read_only", 1);
            frm.set_df_property("to_date", "read_only", 1);
            frm.add_custom_button("View Report", function () {
                frappe.set_route("query-report", "Sales Order Detailed Report", {
                    "report": frm.doc.name
                });
            }).addClass("btn");
        } else {
            frm.add_custom_button("Generate Report", function () {
                if (!frm.doc.from_date || !frm.doc.to_date) {
                    frappe.msgprint({
                        title: "Error",
                        message: "Please select from date and to date",
                        indicator: "red"
                    });
                    return;
                }
                frm.call({
                    doc: frm.doc,
                    method: "generate_report_data",
                    callback: function (r) {
                        if (!r.exc) {
                            frappe.msgprint({
                                title: "Report Generated",
                                message: "Report generated successfully.",
                                indicator: "green"
                            });
                            frm.refresh_fields('report_items');
                        }
                    }
                })
            }).addClass("btn");
        }
    },

});
