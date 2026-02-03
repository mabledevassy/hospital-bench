# Copyright (c) 2026, Mable Devassy and contributors
# For license information, please see license.txt

import frappe

import frappe

def execute(filters=None):
    date = filters.get("date")

    columns = [
        {"label": "Doctor", "fieldname": "doctor_name", "width": 200},
        {"label": "Total Visits", "fieldname": "total", "width": 120},
        {"label": "Completed", "fieldname": "completed", "width": 120},
        {"label": "Cancelled", "fieldname": "cancelled", "width": 120}
    ]

    data = []

    doctors = frappe.get_all("Doctor", fields=["name", "doctor_name"])

    for doc in doctors:
        appointments = frappe.get_all(
            "Appointment",
            filters={
                "doctor": doc.name,
                "appointment_date": date
            },
            fields=["status"]
        )

        total = len(appointments)
        completed = sum(1 for a in appointments if a.status == "Completed")
        cancelled = sum(1 for a in appointments if a.status == "Cancelled")

        if total > 0:
            data.append({
                "doctor_name": doc.doctor_name,
                "total": total,
                "completed": completed,
                "cancelled": cancelled
            })

    return columns, data



