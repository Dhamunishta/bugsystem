frappe.pages['ticket-status-base'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Ticket Status Base',
		single_column: true
	});
}