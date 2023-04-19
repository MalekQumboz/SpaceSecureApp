import frappe
def get_context(context):


	host=frappe.db.sql(""" SELECT * FROM `tabPackage`where active = 1  and main_service = 'خدمة الاستضافة' """,as_dict=1)
	webservice=frappe.db.sql(""" SELECT * FROM `tabPackage`where active = 1  and main_service = 'خدمة تصميم المواقع والتطبيقات' """,as_dict=1)

	cypersecurity=frappe.db.get_all("Package",{"active":1,"main_service": "خدمة الامن السيبراني"})
	cypersecurity_list = []
	for val in cypersecurity:
		data = frappe.get_last_doc("Package",filters={"active": 1, "name":val["name"]})
		frappe.db.commit()
		cypersecurity_list.append(data)

	cypersecurity_nav = frappe.db.sql(""" SELECT * FROM `tabSub Service`where active = 1  and main_services_name = 'خدمة الامن السيبراني' """,as_dict=1)
	host_nav = frappe.db.sql(""" SELECT * FROM `tabSub Service`where active = 1  and main_services_name = 'خدمة الاستضافة' """, as_dict=1)
	webservice_nav = frappe.db.sql(""" SELECT * FROM `tabSub Service`where active = 1  and main_services_name = 'خدمة تصميم المواقع والتطبيقات' """,as_dict=1)

	frappe.db.commit()

	for val in cypersecurity:
		print("*"*100)
		print(val)

	context.cypersecurity_package=cypersecurity_list
	context.host_package=host
	context.webservice_package=webservice

	context.cypersecurity_sub = cypersecurity_nav
	context.host_sub = host_nav
	context.webservice_sub = webservice_nav

	return context

