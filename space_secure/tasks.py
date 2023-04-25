import frappe

def daily():
    subscription=frappe.db.get_all("Subscription")
    for val in subscription:
        print(val)


def cron():
    subscription = frappe.db.get_all("Subscription")

    for val in subscription:
        data = frappe.get_last_doc("Subscription", filters={"name": val["name"]})
        total_subscription_days = 0
        if data.start_date and data.end_date:
            total_subscription_days = frappe.utils.date_diff(data.end_date, frappe.utils.getdate(frappe.utils.today)) + 1

            if total_subscription_days == 10:
                # new_email = frappe.get_doc({
                #     "doctype": "Communication",
                #     # "email_template": "123122",
                #     "subject": "mm",
                #     "communication_medium": "Email",
                #     "sender": "malek.hossam.209@gmail.com",
                #     "recipients":"malek.h.qumboz@gmail.com",
                #     "content":"dddddd"
                #
                # })
                #
                # new_email.insert(ignore_permissions=True)
                # frappe.db.commit()

                print(total_subscription_days)
            elif total_subscription_days ==5:
                print(5)
            elif total_subscription_days== 1:
                print(1)


