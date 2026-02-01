// Copyright (c) 2026, Mable Devassy and contributors
// For license information, please see license.txt

frappe.ui.form.on("Patient", {
    dob(frm) {
        if (frm.doc.dob) {
            let today = frappe.datetime.get_today();
            let age = frappe.datetime.get_diff(today, frm.doc.dob) / 365;
            frm.set_value("age", Math.floor(age));
        }
    }
});
