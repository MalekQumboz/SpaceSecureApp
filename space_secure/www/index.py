import frappe
def get_context(context):
	cypersecurity = frappe.db.sql(""" SELECT * FROM `tabSub Service`where active = 1  and main_services_name = 'خدمة الامن السيبراني' """,as_dict=1)
	host = frappe.db.sql(""" SELECT * FROM `tabSub Service`where active = 1  and main_services_name = 'خدمة الاستضافة' """, as_dict=1)
	webservice = frappe.db.sql(""" SELECT * FROM `tabSub Service`where active = 1  and main_services_name = 'خدمة تصميم المواقع والتطبيقات' """,as_dict=1)

	frappe.db.commit()

	get_webservice=frappe.db.sql(""" SELECT * FROM `tabPackage` where active = 1  and main_service ='خدمة تصميم المواقع والتطبيقات' ORDER BY modified DESC LIMIT 1 """,as_dict=1)
	get_webservice_2=frappe.db.sql(""" SELECT * FROM `tabPackage` where active = 1  and main_service ='خدمة تصميم المواقع والتطبيقات' ORDER BY modified DESC LIMIT 1 ,1""",as_dict=1)
	get_host=frappe.db.sql(""" SELECT * FROM `tabPackage` where active = 1  and main_service ='خدمة الاستضافة' ORDER BY modified DESC LIMIT 1""",as_dict=1)

	frappe.db.commit()

	context.host_package_first = get_host
	context.webservice_package_first =get_webservice
	context.webservice_package_sec = get_webservice_2

	context.cypersecurity_sub=cypersecurity
	context.host_sub=host
	context.webservice_sub=webservice

	return context


@frappe.whitelist(True)
def insert_data(full_name,email,phone,description):

    doc = frappe.get_doc({
        "doctype": "Communication Requests",
        "full_name": full_name,
        "email": email,
        "phone": phone,
		"description":description,
        "type":"طلب خدمة"
    })
    doc.insert(ignore_permissions=True)
    frappe.db.commit()
