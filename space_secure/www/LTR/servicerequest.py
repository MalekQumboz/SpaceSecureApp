import frappe
def get_context(context):
    package = frappe.db.sql(""" SELECT * FROM `tabPackage`where active = 1 """,as_dict=1)
    service = frappe.db.sql(""" SELECT * FROM `tabMain Service` """,as_dict=1)

    cypersecurity_nav = frappe.db.sql(""" SELECT * FROM `tabSub Service`where active = 1  and main_services_name = 'خدمة الامن السيبراني' """,as_dict=1)
    host_nav = frappe.db.sql(""" SELECT * FROM `tabSub Service`where active = 1  and main_services_name = 'خدمة الاستضافة' """, as_dict=1)
    webservice_nav = frappe.db.sql(""" SELECT * FROM `tabSub Service`where active = 1  and main_services_name = 'خدمة تصميم المواقع والتطبيقات' """, as_dict=1)

    frappe.db.commit()

    context.mainservices = service
    context.packages = package

    context.cypersecurity_sub = cypersecurity_nav
    context.host_sub = host_nav
    context.webservice_sub = webservice_nav

    return context
