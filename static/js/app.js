// from data.js
const tableData = data;

// get table references
var tbody = d3.select("tbody");

function buildTable(data) {
  tbody.html("");
  data.forEach((dataRow) => {
    let row = tbody.append("tr");
    Object.values(dataRow).forEach((val) => {
      let cell = row.append("td");
      cell.text(val);
    });
  });
}
var filters = {};

function updateFilters() {
    let elemChange = d3.select(this);
    let elemVal = elemChange.property("value");
    let filterId = elemChange.attr('id');
    if (elemVal) {
        filters[filterId] =elemVal;
    } else {
      delete filters[filterId]
    }
    filterTable();
  }
  
  function filterTable() {
    let filteredData = tableData;
    Object.entries(filters).forEach(([key, value]) => {
      filteredData = filteredData.filter(row => row[key] === value);
      });
    buildTable(filteredData)
  }
  d3.selectAll("input").on("change", updateFilters);
  buildTable(tableData);
