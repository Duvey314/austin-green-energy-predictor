//  MODULE 11 EXAMPLE OF D3 & USER INPUT TO FILTER A TABLE




// from data.js
const tableData = data;

// get table references
var tbody = d3.select("tbody");

function buildTable(data) {
  // First, clear out any existing data
  tbody.html("");

  // Next, loop through each object in the data
  // and append a row and cells for each value in the row
  data.forEach((dataRow) => {
    // Append a row to the table body
    let row = tbody.append("tr");
    
    // Loop through each field in the dataRow and add
    // each value as a table cell (td)
    Object.values(dataRow).forEach((val) => {
      let cell = row.append("td");
      cell.text(val);
      //console.log(cell.text(val));
    });
  });
}

// Keep track of all filters
var filters = {};

function updateFilters() {

  let elementChange = d3.select(this);
  let elementValue = elementChange.property("value");
  let elementID = elementChange.attr("id");

  if (elementValue) {
    filters[elementID] = elementValue;
  }
  else {
    delete filters[elementID];
  }
  filterTable();
}

function filterTable() {

  // set the filteredData to the existing tableData
  let filteredData = tableData;
  // loop through all of the filters and keep any data that matches the filter values
  //console.log(filters)
  
  Object.entries(filters).forEach(([key,value]) => {
    //console.log('key: ', key, 'value: ', value)
    filteredData = filteredData.filter(row => row[key] === value);
  });
  
  //console.log(filteredData);
  //Use .slice above!

  // Finally, rebuild the table using the filtered Data
buildTable(filteredData);
}

// Attach an event to listen for changes to each filter
// Hint: You'll need to select the event and what it is listening for within each set of parenthesis
d3.selectAll("input").on("change", updateFilters);

// Build the table when the page loads
buildTable(tableData);
