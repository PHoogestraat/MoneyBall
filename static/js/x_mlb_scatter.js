// set the dimensions and margins of the graph
var margin = {top: 10, right: 30, bottom: 60, left: 60},
    width = 1000 - margin.left - margin.right,
    height = 800 - margin.top - margin.bottom;

// append the svg object to the body of the page
var svg = d3.select(".chart")
    .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform",
          "translate(" + margin.left + "," + margin.top + ")");


// call to json 

d3.json("/year.json").then(function(data) {
  data.forEach(d => {
    d.wins = +d.wins;
    d.cost_per_win = +d.cost_per_win;
  });

// create x axis 

var x = d3.scaleLinear()
  .domain(d3.extent(data.map(d => d.wins)))
  .range([0,width]);

svg.append("g")
  .attr("transform", "translate(0," + height + ")")
  .call(d3.axisBottom(x));

// x label

svg.append("text")
  .attr("text-anchor", "middle")
  .attr("x", width / 2)
  .attr("y", height + 40)
  .text("Regular Season Wins");

// y axis

var y = d3.scaleLinear()
  .domain(d3.extent(data, d => d.cost_per_win))
  .range([0,height]);
svg.append("g")
  .call(d3.axisLeft(y));

// y label

svg.append("text")
  .attr("text-anchor", "middle")
  .attr("transform", "rotate(-90)")
  .attr("x", (height / 2) * -1)
  .attr("dy", (-70))
  .text("Cost Per Regular Season Win ($)");

// create dots variables


var gdots = svg.selectAll("g.dot")
  .data(data)
  .enter()
  .append('g');

// add dots to gdots

gdots.append("circle")
.attr("cx", d => x(d.wins))
.attr("cy", d => y(d.cost_per_win))
.attr("r", 10)
// .style("fill", "#01df3a")
.style("fill", d => {
  console.log(d);
  if (d.team === "OAK") {
    return "#01df3a";
  }
  if(d.championship === "yes") {
    return "pink";
  }
  return "lightblue";
});
gdots.append("text")
  .text(d => d.team)
  .attr("x", d => x(d.wins))
  .attr("y", d => y(d.cost_per_win))
  .attr("dx", -5)
  .attr("dy", 2)
  .style("font-size", "7px")
  .style(font-weight, "bold");
}).catch(e => {
  console.log(e);
});


























