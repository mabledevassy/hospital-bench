// frappe.pages['doctor-schedule'].on_page_load = function(wrapper) {
// 	var page = frappe.ui.make_app_page({
// 		parent: wrapper,
// 		title: 'Doctor Schedule',
// 		single_column: true
// 	});
// }
frappe.pages['doctor-schedule'].on_page_load = function (wrapper) {

    let page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'Doctor Schedule',
        single_column: true
    });

    // Doctor filter
    let doctor = page.add_field({
        label: 'Doctor',
        fieldtype: 'Link',
        fieldname: 'doctor',
        options: 'Doctor',
        reqd: 1
    });

    // Date filter
    let date = page.add_field({
        label: 'Date',
        fieldtype: 'Date',
        fieldname: 'date',
        default: frappe.datetime.get_today(),
        reqd: 1
    });

    let result = $('<div class="schedule-result"></div>').appendTo(page.body);

    page.set_primary_action('Get Schedule', () => {

        if (!doctor.get_value() || !date.get_value()) {
            frappe.msgprint("Please select Doctor and Date");
            return;
        }

        frappe.call({
            method: "hospital_management.hospital_management.page.doctor_schedule.doctor_schedule.get_doctor_schedule",
            args: {
                doctor: doctor.get_value(),
                date: date.get_value()
            },
            callback: function (r) {

                result.empty();

                if (!r.message || r.message.length === 0) {
                    result.html("<p>No appointments found.</p>");
                    return;
                }

                let html = `
                    <table class="table table-bordered">
                        <tr>
                            <th>Time</th>
                            <th>Patient</th>
                            <th>Status</th>
                        </tr>
                `;

                r.message.forEach(row => {
                    html += `
                        <tr>
                            <td>${row.from_time} - ${row.to_time}</td>
                            <td>${row.patient_name}</td>
                            <td>${row.status}</td>
                        </tr>
                    `;
                });

                html += "</table>";

                result.html(html);
            }
        });
    });
};
