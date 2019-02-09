# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "customer_loan_management"
app_title = "Customer Loan Management"
app_publisher = "frappe"
app_description = "App for Manage Customer Loan"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "frappe@io"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/customer_loan_management/css/customer_loan_management.css"
# app_include_js = "/assets/customer_loan_management/js/customer_loan_management.js"

# include js, css files in header of web template
# web_include_css = "/assets/customer_loan_management/css/customer_loan_management.css"
# web_include_js = "/assets/customer_loan_management/js/customer_loan_management.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "customer_loan_management.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "customer_loan_management.install.before_install"
# after_install = "customer_loan_management.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "customer_loan_management.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

scheduler_events = {
	"daily": [
		"customer_loan_management.customer_loan_management.loan_due_amount.update_interest_amount",
		"customer_loan_management.customer_loan_management.loan_due_amount.update_interest_amount_ar"
	]
}

# Testing
# -------

# before_tests = "customer_loan_management.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "customer_loan_management.event.get_events"
# }

