// function init() {
//   var selector = d3.select("#selDataset");

//   d3.json("samples.json").then((data) => {
//     console.log(data);
//     var sampleNames = data.names;
//     sampleNames.forEach((sample) => {
//       selector
//         .append("option")
//         .text(sample)
//         .property("value", sample);
//     });
// })}
 
// function optionChanged(newSample) {
//   buildMetadata(newSample);
//   buildBar(newSample);
// }


// function buildBar(sample) {
//   d3.json("samples.json").then((data) =>{
//     var samples = data.samples;
//     var samplesArray = samples.filter(sampleObj => sampleObj.id == sample);
//     var array = samplesArray[0];
//     var sampleValues = array.sample_values;
//     var otuIDs = array.otu_ids;
//     var otuLabels = array.otu_labels;

//       // barChart
//       var BAR = d3.select("#bar");
//       BAR.html("");
//       var barChart = {
//         x : [sampleValues[0], sampleValues[1], sampleValues[2], sampleValues[3], sampleValues[4], sampleValues[5], sampleValues[6], sampleValues[7], sampleValues[8], sampleValues[9]],
//         y : [otuIDs[0], otuIDs[1], otuIDs[2], otuIDs[3], otuIDs[4], otuIDs[5], otuIDs[6], otuIDs[7], otuIDs[8], otuIDs[9]],
//         type : 'bar',
//         text : [otuLabels[0], otuLabels[1], otuLabels[2], otuLabels[3], otuLabels[4], otuLabels[5], otuLabels[6], otuLabels[7], otuLabels[8], otuLabels[9]],
//         orientation : 'h',
//         yaxis : {autotick:false}
//       };

