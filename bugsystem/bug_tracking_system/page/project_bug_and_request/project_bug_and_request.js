frappe.pages['Project Bug and Request'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Project Bugs and Requests',
		single_column: true
	});
	page.main.append(frappe.render_template("project_bug_and_request",{}))
	frappe.call({
        "method": "bugsystem.bug_tracking_system.page.project_bug_and_request.project_bug_and_request.bug_request",
        callback: function (data) {    
            rdata=data.message[0]
            //console.log(rdata)
            renderChart(rdata)
        }
    });
}
function renderChart(rdata){
    FusionCharts.ready(function () {
        var radio = [],
            radElem,
            val,
            revenueChart = new FusionCharts({
                type: 'MSColumn2D',
                renderAt: 'chart-container',
                width: '600',
                height: '450',
                dataFormat: 'json',
                dataSource: rdata
            });

        revenueChart.render();       

    });
}