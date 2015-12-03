frappe.pages['bug-report-project-w'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Project Wise Ticket',
		single_column: true
	});

	page.main.append(frappe.render_template("bug_report_project_w",{}))
    
    var rdata="";
    var rchart="";
    frappe.call({
        "method": "bugsystem.bug_tracking_system.doctype.bugproject.bugproject.projectwise_data",
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
        var radio = [],
            radElem,
            val,
            revenueChart = new FusionCharts({
                type: 'column3d',
                renderAt: 'chart-container',
                width: '600',
                height: '450',
                dataFormat: 'json',
                dataSource: rdata
            });

        revenueChart.render();       

    });
}