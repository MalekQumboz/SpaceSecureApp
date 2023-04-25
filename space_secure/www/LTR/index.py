import frappe
def get_context(context):
	cypersecurity = frappe.db.sql(""" SELECT * FROM `tabSub Service`where active = 1  and main_services_name = 'خدمة الامن السيبراني' """,as_dict=1)
	host = frappe.db.sql(""" SELECT * FROM `tabSub Service`where active = 1  and main_services_name = 'خدمة الاستضافة' """, as_dict=1)
	webservice = frappe.db.sql(""" SELECT * FROM `tabSub Service`where active = 1  and main_services_name = 'خدمة تصميم المواقع والتطبيقات' """,as_dict=1)

	frappe.db.commit()

	get_webservice=frappe.db.sql(""" SELECT * FROM `tabPackage` where active = 1  and main_service ='خدمة تصميم المواقع والتطبيقات'  and type='مواقع' ORDER BY modified DESC LIMIT 1 """,as_dict=1)
	get_webservice_2=frappe.db.sql(""" SELECT * FROM `tabPackage` where active = 1  and main_service ='خدمة تصميم المواقع والتطبيقات'  and type='تطبيقات' ORDER BY modified DESC LIMIT 1 """,as_dict=1)
	get_host=frappe.db.sql(""" SELECT * FROM `tabPackage` where active = 1  and main_service ='خدمة الاستضافة' ORDER BY modified DESC LIMIT 1""",as_dict=1)

	frappe.db.commit()

	webservice_list = []
	webservice_2_list=[]
	host_list=[]

	for val in get_webservice:
		data = frappe.get_last_doc("Package", filters={"active": 1, "name": val["name"]})
		frappe.db.commit()
		webservice_list.append(data)

	for val in get_webservice_2:
		data = frappe.get_last_doc("Package", filters={"active": 1, "name": val["name"]})
		frappe.db.commit()
		webservice_2_list.append(data)

	for val in get_host:
		data = frappe.get_last_doc("Package", filters={"active": 1, "name": val["name"]})
		frappe.db.commit()
		host_list.append(data)

	frappe.db.commit()

	context.host_package_first = host_list
	context.webservice_package_first =webservice_list
	context.webservice_package_sec = webservice_2_list

	context.cypersecurity_sub=cypersecurity
	context.host_sub=host
	context.webservice_sub=webservice

	return context
