import frappe
def get_context(context):

	cypersecurity=frappe.db.get_all("Sub Service",{"active":1,"main_services_name": "خدمة الامن السيبراني"})
	host=frappe.db.get_all("Sub Service",{"active":1,"main_services_name": "خدمة الاستضافة"})
	webservice = frappe.db.get_all("Sub Service",{"active":1,"main_services_name": "خدمة تصميم المواقع والتطبيقات"})


	cypersecurity_list=[]
	host_list=[]
	webservice_list=[]

	for val in cypersecurity:
		data=frappe.get_doc("Sub Service", val["name"])
		cypersecurity_list.append(data)


	for val in host:
		data=frappe.get_doc("Sub Service", val["name"])
		host_list.append(data)

	for val in webservice:
		data=frappe.get_doc("Sub Service", val["name"])
		webservice_list.append(data)


	webservice_2 = frappe.db.get_all("Package", {"active": 1, "main_service": "خدمة تصميم المواقع والتطبيقات"})
	get_webservice_2=frappe.get_last_doc("Package",filters={"active": 1, "name": webservice_2[0]["name"]}  )

	get_host=frappe.get_last_doc("Package", filters={"active": 1, "main_service": "خدمة الاستضافة"})
	get_cypersecurity=frappe.get_last_doc("Package",filters={"active": 1, "main_service": "خدمة الامن السيبراني"})
	get_webservice= frappe.get_last_doc("Package", filters={"active": 1,"main_service": "خدمة تصميم المواقع والتطبيقات"})

	frappe.db.commit()

	context.webservice_package_2 = get_webservice_2
	context.host_package = get_host
	context.cypersecurity_package = get_cypersecurity
	context.webservice_package =get_webservice

	context.cypersecurity_sub=cypersecurity_list
	context.host_sub=host_list
	context.webservice_sub=webservice_list

	return context