// Copyright (c) 2026, Mable Devassy and contributors
// For license information, please see license.txt

frappe.query_reports["Daily Visit Summary"] = {
    filters: [
        {
            fieldname: "date",
            label: "Date",
            fieldtype: "Date",
            default: frappe.datetime.get_today(),
            reqd: 1
        }
    ]
};
