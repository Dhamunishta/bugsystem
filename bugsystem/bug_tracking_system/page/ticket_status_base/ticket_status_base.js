frappe.pages['ticket-status-base'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Ticket Status Base',
		single_column: true
	});

	page.main.append(frappe.render_template("ticket_status_base",{}))
    frappe.call({
        "method": "bugsystem.bug_tracking_system.page.ticket_status_base.ticket_status_base.ticket_status_data",
        callback: function (data) {    
            rdata=data.message[0]
            console.log(rdata)
            renderChart(rdata)
        }
    });
}
function renderChart(rdata){
    /*var myChartcm2 = new FusionCharts( "Pie3D", "2ps", "30%","180" );
    myChartcm2.setJSONData("");
    myChartcm2.render("chart-container");*/
   
    FusionCharts.ready(function () {
            revenueChart = new FusionCharts({
                type: 'pie3d',
                renderAt: 'chart-container',
                width: '600',
                height: '450',
                dataFormat: 'json',
                dataSource: rdata
            });

        revenueChart.render();       

    });
}