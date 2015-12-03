frappe.pages['project-wise-bugs'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Project Wise Bugs',
		single_column: true
	});
}