import frappe
# import string
# import random

# def insert_note_cron():
#     letters = string.ascii_letters
#     note_title = "".join(random.choice(letters) for _ in range(20))

#     note = frappe.get_doc({
#         "doctype": "Note",
#         "title": note_title
#     })
#     note.insert(ignore_permissions=True)
#     frappe.db.commit()

# def noon_task():
#     logger = frappe.logger("noon_task")
#     logger.info("Noon task executed successfully")



def send_daily_email(users=None):
    
    logger = frappe.logger("daily_email")

    if not users:
        users = ["vasupokiya14@gmail.com"]

    try:
        # Enqueue sendmail asynchronously in worker
        frappe.enqueue(
            method="frappe.sendmail",
            queue="default",
            is_async=True,
            delayed=True,  # store in Email Queue
            recipients=users,
            subject="Test Daily Email",
            message="<p>This is a test daily email.</p>"
        )

        logger.info(f"Daily email queued for {users}")

    except Exception:
        logger.error(frappe.get_traceback())
        frappe.log_error("Email Scheduler Error",frappe.get_traceback())

