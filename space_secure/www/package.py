import frappe
def get_context(context):


	host=frappe.db.sql(""" SELECT * FROM `tabPackage`where active = 1  and main_service = 'خدمة الاستضافة' """,as_dict=1)
	webservice=frappe.db.sql(""" SELECT * FROM `tabPackage`where active = 1  and main_service = 'خدمة تصميم المواقع والتطبيقات' and type='مواقع'""",as_dict=1)
	app=frappe.db.sql(""" SELECT * FROM `tabPackage`where active = 1  and main_service = 'خدمة تصميم المواقع والتطبيقات' and type='تطبيقات'""",as_dict=1)
	cypersecurity=frappe.db.get_all("Package",{"active":1,"main_service": "خدمة الامن السيبراني"})


	host_list = []
	webservice_list = []
	app_list=[]
	cypersecurity_list = []

	for val in host:
		data = frappe.get_last_doc("Package", filters={"active": 1, "name": val["name"]})
		frappe.db.commit()
		host_list.append(data)

	for val in webservice:
		data = frappe.get_last_doc("Package", filters={"active": 1, "name": val["name"]})
		frappe.db.commit()
		webservice_list.append(data)

	for val in app:
		data = frappe.get_last_doc("Package", filters={"active": 1, "name": val["name"]})
		frappe.db.commit()
		app_list.append(data)

	for val in cypersecurity:
		data = frappe.get_last_doc("Package",filters={"active": 1, "name":val["name"]})
		frappe.db.commit()
		cypersecurity_list.append(data)

	cypersecurity_nav = frappe.db.sql(""" SELECT * FROM `tabSub Service`where active = 1  and main_services_name = 'خدمة الامن السيبراني' """,as_dict=1)
	host_nav = frappe.db.sql(""" SELECT * FROM `tabSub Service`where active = 1  and main_services_name = 'خدمة الاستضافة' """, as_dict=1)
	webservice_nav = frappe.db.sql(""" SELECT * FROM `tabSub Service`where active = 1  and main_services_name = 'خدمة تصميم المواقع والتطبيقات' """,as_dict=1)

	frappe.db.commit()


	context.cypersecurity_package=cypersecurity_list
	context.host_package=host_list
	context.webservice_package=webservice_list
	context.app_package=app_list

	context.cypersecurity_sub = cypersecurity_nav
	context.host_sub = host_nav
	context.webservice_sub = webservice_nav

	return context





