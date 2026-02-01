// Copyright (c) 2026, Mable Devassy and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Appointment", {
// 	refresh(frm) {

// 	},
// });
// frappe.ui.form.on("Appointment", {
//     validate(frm) {

//         // Mandatory fields check
//         if (!frm.doc.doctor || !frm.doc.appointment_date || !frm.doc.from_time || !frm.doc.to_time) {
//             return;
//         }

//         frappe.db.get_list("Appointment", {
//             filters: {
//                 doctor: frm.doc.doctor,
//                 appointment_date: frm.doc.appointment_date,
//                 docstatus: ["!=", 2]
//             },
//             fields: ["name", "from_time", "to_time"],
//             limit: 100
//         }).then(records => {

//             for (let appt of records) {

//                 // Skip current document while editing
//                 if (appt.name === frm.doc.name) continue;

//                 // Overlap condition
//                 if (
//                     frm.doc.from_time < appt.to_time &&
//                     frm.doc.to_time > appt.from_time
//                 ) {
//                     frappe.throw(__("This doctor already has an appointment during the selected time."));
//                 }
//             }
//         });
//     }
// });

frappe.ui.form.on("Appointment", {
    validate(frm) {

        // Mandatory fields check
        if (!frm.doc.doctor || !frm.doc.appointment_date || !frm.doc.from_time || !frm.doc.to_time) {
            return;
        }

        return frappe.db.get_list("Appointment", {
            filters: {
                doctor: frm.doc.doctor,
                appointment_date: frm.doc.appointment_date,
                docstatus: ["!=", 2]
            },
            fields: ["name", "from_time", "to_time"],
            limit: 100
        }).then(records => {

            for (let appt of records) {

                // Skip current document while editing
                if (appt.name === frm.doc.name) continue;

                // Overlap condition
                if (
                    frm.doc.from_time < appt.to_time &&
                    frm.doc.to_time > appt.from_time
                ) {
                    frappe.throw(
                        __("This doctor already has an appointment during the selected time.")
                    );
                }
            }
        });
    }
});
