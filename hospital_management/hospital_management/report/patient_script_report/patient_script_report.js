// Copyright (c) 2026, Mable Devassy and contributors
// For license information, please see license.txt

frappe.query_reports["Patient Script Report"] = {
	"filters": [
		 {
            fieldname: "patient",
            label: __("Patient"),
            fieldtype: "Link",
            options: "Patient"
        },
        {
            fieldname: "gender",
            label: __("Gender"),
            fieldtype: "Select",
            options: "\nMale\nFemale\nOther"
        }

	]
};
