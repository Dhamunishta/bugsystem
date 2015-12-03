# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "bugsystem"
app_title = "Bug System"
app_publisher = "Nishta"
app_description = "Bug Tracking System"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "anandh.nishta@gmail.com"
app_version = "0.0.1"

# Includes in <head>
# ------------------
app_include_js = "/assets/bugsystem/js/fusioncharts.js"
app_include_js = "/assets/bugsystem/js/themes/fusioncharts.theme.zune.js"
# include js, css files in header of desk.html
# app_include_css = "/assets/bugsystem/css/bugsystem.css"
# app_include_js = "/assets/bugsystem/js/bugsystem.js"

# include js, css files in header of web template
# web_include_css = "/assets/bugsystem/css/bugsystem.css"
# web_include_js = "/assets/bugsystem/js/bugsystem.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "bugsystem.install.before_install"
# after_install = "bugsystem.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "bugsystem.notifications.get_notification_config"

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

# scheduler_events = {
# 	"all": [
# 		"bugsystem.tasks.all"
# 	],
# 	"daily": [
# 		"bugsystem.tasks.daily"
# 	],
# 	"hourly": [
# 		"bugsystem.tasks.hourly"
# 	],
# 	"weekly": [
# 		"bugsystem.tasks.weekly"
# 	]
# 	"monthly": [
# 		"bugsystem.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "bugsystem.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "bugsystem.event.get_events"
# }

