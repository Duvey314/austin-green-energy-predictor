function init() {
    var selector = d3.select("#selDataset");
  
    d3.json("samples.json").then((data) => {
      console.log(data);
      var sampleNames = data.names;
      sampleNames.forEach((sample) => {
        selector
          .append("option")
          .text(sample)
          .property("value", sample);
      });
  })}
   
function optionChanged(newSample) {
    buildMetadata(newSample);
    buildBar(newSample);
}

function buildMetadata(sample) {
  d3.json("samples.json").then((data) => {
    var metadata = data.metadata;
    var resultArray = metadata.filter(sampleObj => sampleObj.id == sample);
    var result = resultArray[0];
    var PANEL = d3.select("#sample-metadata");
    PANEL.html("");
    var demInfo = Object.entries(result)
    demInfo.forEach((item) => {
      PANEL.append("h6").text(item[0]+': '+item[1]);
    });
  });
}

function buildBar(sample) {
  d3.json("samples.json").then((data) =>{
    var samples = data.samples;
    var samplesArray = samples.filter(sampleObj => sampleObj.id == sample);
    var array = samplesArray[0];
    var sampleValues = array.sample_values;
    var otuIDs = array.otu_ids;
    var otuLabels = array.otu_labels;

      // barChart
      var BAR = d3.select("#bar");
      BAR.html("");
      var barChart = {
        x : [sampleValues[0], sampleValues[1], sampleValues[2], sampleValues[3], sampleValues[4], sampleValues[5], sampleValues[6], sampleValues[7], sampleValues[8], sampleValues[9]],
        y : [otuIDs[0], otuIDs[1], otuIDs[2], otuIDs[3], otuIDs[4], otuIDs[5], otuIDs[6], otuIDs[7], otuIDs[8], otuIDs[9]],
        type : 'bar',
        text : [otuLabels[0], otuLabels[1], otuLabels[2], otuLabels[3], otuLabels[4], otuLabels[5], otuLabels[6], otuLabels[7], otuLabels[8], otuLabels[9]],
        orientation : 'h',
        yaxis : {autotick:false}
      };

      var barLayout = {
        title: 'Top Results For Selected Subject',
        showlegend:false,
        orientation:'h',
        xaxis:{title: 'Sample Value'},
        yaxis:{autotick:false, type:'category', title: 'OTU ID'}
      };

      //bubbleChart
      var BUBBLE = d3.select("#bubble");
      BUBBLE.html("");
      var bubbleChart = {
        x: otuIDs,
        y: sampleValues,
        mode: 'markers',
        text: otuLabels,
        marker: {
          size: sampleValues,
          color: otuIDs
        }
      };
      var bubbleLayout = {
        title: 'All Results For Subject',
        showlegend: false,
        xaxis:{title: 'OTU ID'}
      };

      Plotly.newPlot('bar', [barChart], barLayout);
      Plotly.newPlot('bubble', [bubbleChart], bubbleLayout);
  });
}

  init();

optionChanged(940);