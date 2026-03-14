app_name = "library_management"
app_title = "Library Management"
app_publisher = "Vasu"
app_description = "Library Management System"
app_email = "vasu123@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "library_management",
# 		"logo": "/assets/library_management/logo.png",
# 		"title": "Library Management",
# 		"route": "/library_management",
# 		"has_permission": "library_management.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/library_management/css/desk.css"
# app_include_js = "/assets/library_management/js/desk.js"

# include js, css files in header of web template
# web_include_css = "/assets/library_management/css/library_management.css"
# web_include_js = "/assets/library_management/js/library_management.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "library_management/public/scss/website"

# include js, css files in header of web form
webform_include_js = {"Job Application": "/assets/library_management/js/web_form_Job_application.js"}
webform_include_css = {"Job Application": "/assets/library_management/js/web_form_Job_application.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
    # "Student" : "public/js/student_js.js",
    "Sales Invoice": "public/js/sales_invoice_custom.js",
    "Customer":"public/js/customer.js",
    "Purchase Order":'public/js/purchase order.js',
    "Contact":"overrides/contact.js"
 }

doctype_list_js = {
    "Customer" : 'public/js/customer_add_button_list.js',
    }
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "library_management/lib_module/doctype/my_calandar/my_calandar_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "library_management/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"\q
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "library_management.utils.jinja_methods",
# 	"filters": "library_management.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "library_managementapps.overrides.install.py"
# after_install = "library_managementapps.overrides.install.py"

# Uninstallation
# ------------

# before_uninstall = "library_management.uninstall.before_uninstall"
# after_uninstall = "library_management.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "library_management.utils.before_app_install"
# after_app_install = "library_management.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "library_management.utils.before_app_uninstall"
# after_app_uninstall = "library_management.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "library_management.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#     "Student":"library_management.overrides.student_query_permissions.get_permission_query_conditions",
# }


# has_permission = {
# 	"Student": "library_management.overrides.student_permisions.student_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

override_doctype_class = {
	# "ToDo": "custom_app.overrides.CustomToDo",
    #"Purchase Order" : "library_management.overrides.purchaseOrder.CustomPurchaseOrder",
    "Sales Invoice" : "library_management.overrides.sales_invoice.SalesInvoiceCustom",
}

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
    "Customer": {
         "after_insert":[
            "library_management.overrides.events.customer_group_count_validate"
        ],
        "on_update":[
            "library_management.overrides.events.customer_group_count_validate",
            # "library_management.overrides.events.show_Popup_on_save"
        ],
        "after_delete":[
            "library_management.overrides.events.customer_group_count_validate"
        ],
        
    },
    "Sales Order":{
        "before_save":[
            "library_management.overrides.events.set_default_discount_sale_order",
        ],
    },
    "Material Request":{
        "on_submit":["library_management.overrides.genarate_PO.genarate_OP"
        ],
    },

    "Item": {
        "validate": ["library_management.overrides.item_events.validate_item_variant",
        ],
        "after_insert": ["library_management.overrides.item_events.create_serial_no"
        ],
    }

    # "Student": {
    #     # "validate": ["library_management.overrides.events.validate_student"],
    #     "on_update":["library_management.overrides.events.sendEmail"]
    # }
}


# Scheduled Tasks
# ---------------

# scheduler_events = {

#     "cron": {
#         "* * * * *": [
#             "library_management.overrides.tasks.insert_note_cron"
#         ],
#         "0 12 * * *": [
#             "library_management.overrides.tasks.noon_task"
#         ],
#         "*/2 * * * *": [
#             "library_management.overrides.tasks.send_daily_email"
#         ],
#         "0 14 * * *": [
#         "library_management.overrides.events.fix_customer_group_sequence"
#         ],
#     },

# 	"all": [
# 		"library_management.overrides.tasks.all"
# 	],
# 	# "daily": [
# 	# 	"library_management.overrides.tasks.send_daily_email"
# 	# ],
# 	"hourly": [
# 		"library_management.overrides.tasks.hourly"
# 	],
# 	"weekly": [
# 		"library_management.overrides.tasks.weekly"
# 	],
# 	"monthly": [
# 		"library_management.overrides.tasks.monthly"
# 	],
#}


# Testing
# -------

# before_tests = "library_management.install.before_tests"

# Overriding Methods
# ------------------------------
#
override_whitelisted_methods = {
    "erpnext.accounts.doctype.sales_invoice.sales_invoice.make_delivery_note":
        "library_management.overrides.sales_invoice.make_delivery_note"
}
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "library_management.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["My Doc_1", "My_Doc_2"]

# Request Events
# ----------------
# before_request = ["library_management.utils.before_request"]
# after_request = ["library_management.utils.after_request"]

# Job Events
# ----------
# before_job = ["library_management.utils.before_job"]
# after_job = ["library_management.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"library_management.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

# Fixtures
#------------------

fixtures =[
   # 'Library Member',
#    {'dt': 'Property Setter', 'filters': [['module', '=', 'lib_module']]}
]


#sounds
#---------------------------
sounds = [
    {
        "name": "call",
        "src": "/assets/library_management/sounds/call-disconnect.mp3",
        "volume": 0.2
    },
]

#Migrate
#-------------------------------------------------------------

after_migrate ="library_management.overrides.migrate.after_migrate"
before_migrate = "library_management.overrides.migrate.before_migrate"

#Add DocType Calender
calendars = ["my_calandar"]
  

# additional_timeline_content = {
#     "ToDo": ["library_management.overrides.timeline.todo_timeline"]
# }


#change Brand logo in website
brand_html = """
<div class="navbar-brand">
    <a href="/">
        <img src="/assets/library_management/images/sigzen.png"
            style="height:28px;">
    </a>
</div>
"""