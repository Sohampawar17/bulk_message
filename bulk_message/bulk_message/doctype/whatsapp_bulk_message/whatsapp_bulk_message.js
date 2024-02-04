// Copyright (c) 2023, tejal and contributors
// For license information, please see license.txt

frappe.ui.form.on('Whatsapp Bulk Message', {
	// refresh: function(frm) {

	// }
});

frappe.ui.form.on('Whatsapp Bulk Message', {
	whatsapp_template: function(frm) {
		frm.clear_table("user_registration_child_table_data");
		frm.refresh_field('user_registration_child_table_data');
		frm.call({
			method:'get_user_registration_data',
			doc:frm.doc
		})
	}
});