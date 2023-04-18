import frappe
def get_context(context):
	cypersecurity=frappe.db.get_all("Package",{"active":1,"main_service": "خدمة الامن السيبراني"})
	host=frappe.db.get_all("Package",{"active":1,"main_service": "خدمة الاستضافة"})
	webservice = frappe.db.get_all("Package",{"active":1,"main_service": "خدمة تصميم المواقع والتطبيقات"})

	cypersecurity_list = []
	host_list = []
	webservice_list = []

	for val in cypersecurity:
		data = frappe.get_doc("Package", val["name"])
		cypersecurity_list.append(data)

	for val in host:
		data = frappe.get_doc("Package", val["name"])
		host_list.append(data)

	for val in webservice:
		data = frappe.get_doc("Package", val["name"])
		webservice_list.append(data)

	cypersecurity_nav=frappe.db.get_all("Sub Service",{"active":1,"main_services_name": "خدمة الامن السيبراني"})
	host_nav=frappe.db.get_all("Sub Service",{"active":1,"main_services_name": "خدمة الاستضافة"})
	webservice_nav = frappe.db.get_all("Sub Service",{"active":1,"main_services_name": "خدمة تصميم المواقع والتطبيقات"})


	cypersecurity_list_nav=[]
	host_list_nav=[]
	webservice_list_nav=[]

	for val in cypersecurity_nav:
		data=frappe.get_doc("Sub Service", val["name"])
		cypersecurity_list_nav.append(data)


	for val in host_nav:
		data=frappe.get_doc("Sub Service", val["name"])
		host_list_nav.append(data)

	for val in webservice_nav:
		data=frappe.get_doc("Sub Service", val["name"])
		webservice_list_nav.append(data)


	frappe.db.commit()

	context.cypersecurity_package = cypersecurity_list
	context.host_package = host_list
	context.webservice_package = webservice_list

	context.cypersecurity_sub=cypersecurity_list_nav
	context.host_sub=host_list_nav
	context.webservice_sub=webservice_list_nav

	return context
