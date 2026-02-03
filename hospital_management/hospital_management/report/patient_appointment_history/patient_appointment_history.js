// Copyright (c) 2026, Mable Devassy and contributors
// For license information, please see license.txt

frappe.query_reports["Patient Appointment History"] = {
    filters: [
        {
            fieldname: "patient",
            label: "Patient",
            fieldtype: "Link",
            options: "Patient",
            reqd: 1
        }
    ]
};
