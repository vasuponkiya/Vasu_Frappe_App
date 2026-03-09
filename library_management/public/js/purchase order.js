// frappe.ui.form.on('Purchase Order Item', {

//     item_code: function (frm, cdt, cdn) {

//         let row = locals[cdt][cdn];

//         if (!row.item_code) return;

//         frappe.db.get_doc('Item', row.item_code).then(item_doc => {

//             // console.log(row.item_code);
//             console.log(item_doc);


//             let child_data = item_doc.custom_item_child || [];

//             // console.log(child_data);

//             let html_content = "";

//             if (child_data.length > 0) {

//                 html_content = `
//                     <table class="table table-bordered table-condensed"
//                            style="background-color:#f8f9fa; margin-top:10px;">
//                         <thead>
//                             <tr>
//                                 <th style="width:50%">Batch No</th>
//                                 <th style="width:50%">Serial No</th>
//                             </tr>
//                         </thead>
//                         <tbody>
//                             ${child_data.map(d => `
//                                 <tr>
//                                     <td>${d.batch_no || ""}</td>
//                                     <td>${d.serial_no || ""}</td>
//                                 </tr>
//                             `).join("")}
//                         </tbody>
//                     </table>
//                 `;
//             } else {
//                 html_content =
//                     "<p class='text-muted'>No additional specifications found.</p>";
//             }

//             // Store HTML
//             frappe.model.set_value(cdt, cdn,
//                 'batch_no_and_serial_no', html_content);
//         });
//     },

//     form_render: function (frm, cdt, cdn) {

//         let row = locals[cdt][cdn];

//         if (!frm.cur_grid || !frm.cur_grid.grid_form) return;

//         frm.cur_grid.grid_form
//             .fields_dict.batch_no_and_serial_no
//             .html(row.batch_no_and_serial_no || "");
//     }
// });



frappe.ui.form.on("Purchase Order Item", {

    item_code(frm, cdt, cdn) {
        // fetch_item_batches(frm, cdt, cdn);
    },

    form_render(frm, cdt, cdn) {
        // render_editable_batches(frm, cdt, cdn);
        render_table(frm, cdt, cdn)
    },

    batch_serial_json(frm, cdt, cdn) {
        // render_editable_batches(frm, cdt, cdn);
    },

    show_table(frm, cdt, cdn) {
        show_dialogbox_AddData(frm, cdt, cdn)
    },

    before_items_remove: function (frm, cdt, cdn) {
        delete_items_child(frm, cdt, cdn);
        frm.refresh_field('custom_batch_no_and_serial_no');
    }


});


//Fatch Item child-table data
function fetch_item_batches(frm, cdt, cdn) {

    const row = locals[cdt][cdn];

    if (!row?.item_code) return clear_batches(frm, cdt, cdn);

    frappe.call({
        method: "frappe.client.get",
        args: {
            doctype: "Item",
            name: row.item_code
        }
    }).then(r => {

        const child = r.message.custom_item_child || [];

        if (!child.length) return;

        const json = child.map(d => ({
            batch_no: d.batch_no || "",
            serial_no: d.serial_no || ""
        }));

        frappe.model.set_value(
            cdt,
            cdn,
            "batch_serial_json",
            JSON.stringify(json)
        );

    });
}


// Function for Render HTML table into grid view
function render_editable_batches(frm, cdt, cdn) {

    const row = locals[cdt][cdn];

    // if (!row?.batch_serial_json) return;

    const widget = frm.cur_grid.grid_form.fields_dict.batch_no_and_serial_no;

    if (!widget || !widget.html) return;

    const data = JSON.parse(row.batch_serial_json || "[]");

    let html = `
    <style>
        .po-batch-table table {
            border-collapse: collapse !important;
            margin: 0 !important;
            width: 50%;
        }
        .po-batch-table .control-input {
            margin: 0 !important;
            padding: 0 !important;
        }
        .po-batch-table input {
            height: 28px;
            padding: 2px 6px;
        }
    </style>

    <div class="po-batch-table">

      <p><strong>Total Rows:</strong> ${data.length}</p>

      <table class="table table-bordered table-sm">
        <thead>
          <tr>
            <th style="width:5%">
                <input type="checkbox" class="select-all" style="width:16px; height:16px;  margin-left: 10px; margin-top: 5px;">
            </th>
            <th style="width:47%">Batch No</th>
            <th style="width:48%">Serial No</th>  
          </tr>
        </thead>
        <tbody>
    `;

    data.forEach((d, i) => {

        html += `
      <tr data-index="${i}" style="height:5px !important">
        <td>
            <input type="checkbox" class="row-check" data-index="${i}" style="width:16px; height:16px; margin-top: 26px; margin-left: 10px;">
        </td>
        <td class="batch-cell" data-index="${i}"></td>
        <td class="serial-cell" data-index="${i}"></td>
      </tr>
    `;
    });

    html += `
        </tbody>
      </table>

      <div style="margin-top:8px;">
        <button class="btn btn-xs btn-primary add-row">
            Add Row
        </button>
        <button class="btn btn-xs btn-danger delete-selected">
            Delete
        </button>
      </div>

    </div>
    `;

    widget.html(html);

    attach_batch_controls(frm, cdt, cdn, data);
    attach_batch_buttons(frm, cdt, cdn, data);
}


//Function for Enter value and Update value into columns
function attach_batch_controls(frm, cdt, cdn, data) {

    const widget = frm.cur_grid.grid_form.fields_dict.batch_no_and_serial_no;
    if (!widget) return;

    data.forEach((row, i) => {

        frappe.ui.form.make_control({
            parent: widget.$wrapper.find(`.batch-cell[data-index="${i}"]`),
            df: {
                fieldtype: "Data",
                fieldname: `batch_${i}`,
                placeholder: "Enter Batch No",
                change() {
                    update_batch_json(frm, cdt, cdn, i, {
                        batch_no: this.get_value()
                    });
                }
            },
            value: row.batch_no,
            render_input: true
        });

        frappe.ui.form.make_control({
            parent: widget.$wrapper.find(`.serial-cell[data-index="${i}"]`),
            df: {
                fieldtype: "Data",
                fieldname: `serial_${i}`,
                placeholder: "Enter Serial No",
                change() {
                    update_batch_json(frm, cdt, cdn, i, {
                        serial_no: this.get_value()
                    });
                }
            },
            value: row.serial_no,
            render_input: true
        });

    });
}

// Function for buttons Action
function attach_batch_buttons(frm, cdt, cdn, data) {

    const widget = frm.cur_grid?.grid_form?.fields_dict?.batch_no_and_serial_no;
    if (!widget) return;

    // ADD ROW
    widget.$wrapper.find(".add-row").click(() => {

        data.push({
            batch_no: "",
            serial_no: ""
        });

        save_and_refresh_batches(frm, cdt, cdn, data);
    });

    // SELECT ALL
    widget.$wrapper.find(".select-all").click(function () {

        const checked = $(this).prop("checked");
        widget.$wrapper.find(".row-check").prop("checked", checked);
    });

    // DELETE SELECTED
    widget.$wrapper.find(".delete-selected").click(() => {

        let indexes = [];

        widget.$wrapper.find(".row-check:checked").each(function () {
            indexes.push(parseInt($(this).data("index")));
        });

        if (!indexes.length) {
            frappe.msgprint("Please select at least one row.");
            return;
        }

        // Remove from highest index to lowest (important)
        indexes.sort((a, b) => b - a);

        indexes.forEach(i => {
            data.splice(i, 1);
        });

        save_and_refresh_batches(frm, cdt, cdn, data);
    });
}

// save and refresh JSON field
function save_and_refresh_batches(frm, cdt, cdn, data) {

    frappe.model.set_value(
        cdt,
        cdn,
        "batch_serial_json",
        JSON.stringify(data)
    );

    setTimeout(() => {
        render_editable_batches(frm, cdt, cdn);
    }, 50);
}


//Update Function for saved data into JSON field
function update_batch_json(frm, cdt, cdn, index, changes) {

    const row = locals[cdt][cdn];
    const data = JSON.parse(row.batch_serial_json || "[]");

    if (!data[index]) return;

    Object.assign(data[index], changes);

    frappe.model.set_value(
        cdt,
        cdn,
        "batch_serial_json",
        JSON.stringify(data)
    );
}


// Function for clear and 
function clear_batches(frm, cdt, cdn) {

    frappe.model.set_value(cdt, cdn, "batch_serial_json", "");
    frappe.model.set_value(cdt, cdn, "batch_no_and_serial_no", "");

    const widget = frm.cur_grid?.grid_form?.fields_dict?.batch_no_and_serial_no;
    if (widget?.html) widget.html("");
}



function show_dialogbox_popup(frm, cdt, cdn) {
    const row = locals[cdt][cdn];

    data = JSON.parse(row.batch_serial_json || '[]');


    let d = new frappe.ui.Dialog({
        title: 'Enter details',
        fields: [
            {
                label: 'Enter Batch No',
                fieldname: 'batch_no',
                fieldtype: 'Data'
            },
            {
                label: 'Enter serial No',
                fieldname: 'serial_no',
                fieldtype: 'Data'
            }
        ],
        size: 'small',
        primary_action_label: 'Submit',
        primary_action(values) {
            data.push({ 'batch_no': values.batch_no, 'serial_no': values.serial_no })
            frappe.model.set_value(
                cdt,
                cdn,
                "batch_serial_json",
                JSON.stringify(data)
            );

            d.hide();
        }
    })
    d.show();
}


function show_dialogbox_AddData(frm, cdt, cdn) {
    const row = locals[cdt][cdn];
    // console.log(row.__unsaved);

    // console.log(row.child_docname);
    if (row.child_docname) {
        frappe.msgprint("Please save This row first!")
        frm.refresh_field('items')
        return
    }

    let d = new frappe.ui.Dialog({
        title: 'Enter details',
        fields: [
            {
                label: 'Enter Batch No',
                fieldname: 'batch_no',
                fieldtype: 'Data'
            },
            {
                label: 'Enter serial No',
                fieldname: 'serial_no',
                fieldtype: 'Data'
            },
            {
                label: 'item Id',
                fieldname: 'item_id',
                fieldtype: 'Data',
                default: row.name,
                read_only: 1
            },
        ],
        size: 'small',
        primary_action_label: 'Submit',
        primary_action(values) {
            frm.add_child('custom_batch_no_and_serial_no', {
                batch_no: values.batch_no,
                serial_no: values.serial_no,
                item: values.item_id
            });
            frm.refresh_field('custom_batch_no_and_serial_no')

            d.hide();
        }
    })
    d.show();
}


function render_table(frm, cdt, cdn) {

    const row = locals[cdt][cdn];
    const widget = frm.cur_grid.grid_form.fields_dict.batch_no_and_serial_no;

    if (!widget || !widget.html) return;
    if (row.child_docname) {
        return
    }

    frappe.call({
        method: "library_management.api.getBatchNo.get_batch_serial_rows",
        args: {
            item: row.name
        },
        callback: function (r) {

            const data = r.message || [];
            // console.log(data);

            let html = `
            <style>
            .po-batch-table table{
                width:50%;
                border-collapse: collapse;
            }

            .po-batch-table th,
            .po-batch-table td{
                padding:6px;
                border:1px solid #ddd;
            }

            .po-batch-table input[type="text"]{
                width:100%;
                height:28px;
                padding:2px 6px;
            }

            .po-batch-table td:first-child{
                text-align:center;
                vertical-align:middle;
            }
            </style>

            <div class="po-batch-table">

            <p><strong>Total Rows:</strong> ${data.length}</p>

            <table class="table table-bordered table-sm">

            <thead>
            <tr>
            <th style="width:5%">
            <input type="checkbox" class="select-all">
            </th>
            <th style="width:47%">Batch No</th>
            <th style="width:48%">Serial No</th>
            </tr>
            </thead>

            <tbody>
            `;

            data.forEach((d, i) => {

                html += `
            <tr data-index="${i}">

            <td>
            <input type="checkbox"
                class="row-check"
                data-index="${i}">
            </td>

            <td>
            <input type="text"
                class="form-control batch-input"
                data-index="${i}"
                value="${d.batch_no || ""}">
            </td>

            <td>
            <input type="text"
                class="form-control serial-input"
                data-index="${i}"
                value="${d.serial_no || ""}">
            </td>

            </tr>
            `;

            });

            html += `
            </tbody>
            </table>

            </div>
            `;

            widget.html(html);

        }
    });
}


function delete_items_child(frm, cdt, cdn) {

    const row = locals[cdt][cdn];
    frappe.call({
        method: 'library_management.api.getBatchNo.delete_all',
        args: {
            item: row.name
        },
        callback: function (r) {
            if (r.message) {
                frm.refresh_field('custom_batch_no_and_serial_no');
            }
        }
    });

}