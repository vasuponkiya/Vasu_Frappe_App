frappe.ui.form.on("Sales Invoice", {
    refresh(frm) {
        frm.add_custom_button(__('Play Sound'), function () {
            frappe.utils.play_sound('call');
        });// Button for Paly Sounds
    }
});
