var regions = { "SAS": "South Asia" , "ECS": "Europe and Central Asia", "MEA": "Middle East & North Africa", "SSF": "Sub-Saharan Africa", "LCN": "Latin America & Caribbean", "EAS": "East Asia &amp; Pacific", "NAC": "North America" },
	w = 925,
	h = 550,
	margin = 30,
	startYear = -0.5, 
	endYear = 0.5,
	startAge = 180,
	endAge = 230,
	y = d3.scale.linear().domain([endAge, startAge]).range([0 + margin, h - margin]),
	x = d3.scale.linear().domain([-.5, 0.5]).range([0 + margin -5, w]),
	years = d3.range(startYear, endYear);


var vis = d3.select("#vis")
    .append("svg:svg")
    .attr("width", w)
    .attr("height", h)
    .append("svg:g");
    // .attr("transform", "translate(0, 600)");

			
var line = d3.svg.line()
    .x(function(d,i) { return x(d.x); })
    .y(function(d) { return y(d.y); });
					

// Regions
// var currents_regions = {};
// d3.text('country-regions.csv', 'text/csv', function(text) {
//     var regions = d3.csv.parseRows(text);
//     for (i=1; i < regions.length; i++) {
//         currents_regions[regions[i][0]] = regions[i][1];
//     }
// });

var startEnd = {},
    currentCodes = {};
d3.text('sim_matrix6.csv', 'text/csv', function(text) {
    var currents = d3.csv.parseRows(text);
    past_thres = currents[0].slice(1, (currents[0].length));

    console.log(past_thres);
    for (i=1; i < currents.length; i++) {
        var values = currents[i].slice(1, currents[i.length-2]);

        console.log(values.length);
        var currData = [];
        currentCodes[currents[i][0]] = currents[i][0];
        
        var started = false;
        for (j=0; j < values.length; j++) {
            if (values[j] != '') {
                currData.push({ x: past_thres[j], y: values[j] });
                
                if (!started) {
                    startEnd[currents[i][0]] = { 'startYear':past_thres[j], 'startVal':values[j] };
                    started = true;
                } else if (j == (values.length - 2)) {
                    startEnd[currents[i][0]]['endYear'] = past_thres[j];
                    startEnd[currents[i][0]]['endVal'] = values[j];
                }
                
            }
        }

        vis.append("svg:path")
            .data([currData])
            .attr("country", currents[i][0])
            //.attr("class", currents_regions[currents[i][1]])
            .attr("d", line)
            .on("mouseover", onmouseover)
            .on("mouseout", onmouseout);
    }

});  
    
vis.append("svg:line")
    .attr("x1", x(-0.5))
    .attr("y1", y(startAge))
    .attr("x2", x(0.5))
    .attr("y2", y(startAge))
    .attr("class", "axis");

vis.append("svg:line")
    .attr("x1", x(startYear))
    .attr("y1", y(startAge))
    .attr("x2", x(startYear))
    .attr("y2", y(endAge))
    .attr("class", "axis");
			
vis.selectAll(".xLabel")
    .data(x.ticks(5))
    .enter().append("svg:text")
    .attr("class", "xLabel")
    .text(String)
    .attr("x", function(d) { return x(d); })
    .attr("y", h-10)
    .attr("text-anchor", "middle");

vis.selectAll(".yLabel")
    .data(y.ticks(4))
    .enter().append("svg:text")
    .attr("class", "yLabel")
    .text(String)
	.attr("x", 0)
	.attr("y", function(d) { return y(d); })
	.attr("text-anchor", "right")
	.attr("dy", 3);
			
vis.selectAll(".xTicks")
    .data(x.ticks(5))
    .enter().append("svg:line")
    .attr("class", "xTicks")
    .attr("x1", function(d) { return x(d); })
    .attr("y1", y(startAge))
    .attr("x2", function(d) { return x(d); })
    .attr("y2", y(startAge)+7);
	
vis.selectAll(".yTicks")
    .data(y.ticks(4))
    .enter().append("svg:line")
    .attr("class", "yTicks")
    .attr("y1", function(d) { return y(d); })
    .attr("x1", x(1959.5))
    .attr("y2", function(d) { return y(d); })
    .attr("x2", x(1960));

function onclick(d, i) {
    var currClass = d3.select(this).attr("class");
    if (d3.select(this).classed('selected')) {
        d3.select(this).attr("class", currClass.substring(0, currClass.length-9));
    } else {
        d3.select(this).classed('selected', true);
    }
}

function onmouseover(d, i) {
    var currClass = d3.select(this).attr("class");
    d3.select(this)
        .attr("class", currClass + " current");
    
    var currentCode = $(this).attr("country");
    var countryVals = startEnd[currentCode];
    var percentChange = 100 * (countryVals['endVal'] - countryVals['startVal']) / countryVals['startVal'];
    
    var blurb = '<p>With a threshold of </p><h2><em>' + currentCodes[currentCode] + '</em> standard deviations above the average user for current performance, </h2>';
    blurb += "<p>a user would face maximum amount of <em><strong>" + Math.round(countryVals['startVal']) + "</em></strong> questions  given that a user is expected to exceed a <em><strong>" + countryVals['startYear'] + "</em></strong> standard deviations above the average user on their past projects. The most rigorous threshold on their past performance of <em><strong>"+ countryVals['endYear'] + "</em></strong> standard deviations above the average user would result in the user having to engage in gold questions every  <em><strong>"  + Math.round(countryVals['endVal']) + "</em></strong> , ";
    if (percentChange >= 0) {
        blurb += "an increase of <em><strong>" + Math.round(percentChange) + "</em></strong> percent."
    } else {
        blurb += "a decrease of <em><strong>" + -1 * Math.round(percentChange) + "</em></strong> percent."
    }
    blurb += "</p>";
    
    $("#default-blurb").hide();
    $("#blurb-content").html(blurb);
}
function onmouseout(d, i) {
    var currClass = d3.select(this).attr("class");
    var prevClass = currClass.substring(0, currClass.length-8);
    d3.select(this)
        .attr("class", prevClass);
    // $("#blurb").text("hi again");
    //$("#default-blurb").show();
    //$("#blurb-content").html('');
}

// function showRegion(regionCode) {
//     var currents = d3.selectAll("path."+regionCode);
//     if (currents.classed('highlight')) {
//         currents.attr("class", regionCode);
//     } else {
//         currents.classed('highlight', true);
//     }
// }
