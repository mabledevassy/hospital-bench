import frappe

# import frappe

@frappe.whitelist()
def get_doctor_schedule(doctor, date):
    appointments = frappe.get_all(
        "Appointment",
        filters={
            "doctor": doctor,
            "appointment_date": date,
            "docstatus": ["!=", 2]
        },
        fields=[
            "name",
            "patient",
            "doctor",
            "from_time",
            "to_time",
            "status"
        ],
        order_by="from_time asc"
    )

    # Add patient_name and doctor_name
    for appt in appointments:
        appt["patient_name"] = frappe.db.get_value(
            "Patient", appt["patient"], "patient_name"
        )
        appt["doctor_name"] = frappe.db.get_value(
            "Doctor", appt["doctor"], "doctor_name"
        )

    return appointments
