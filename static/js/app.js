$( "#datepicker" ).datepicker( "setDate", "04/20/2018" );

$.post( "/getwind", function( data ) {
    var windData = JSON.parse(data);
    var startDate = `${windData.data[0]["Month"]}/${windData.data[0]["Day"]}/${windData.data[0]["Year"]} ${windData.data[0]["Hour"]}:00`
    var endDate = `${windData.data[47]["Month"]}/${windData.data[47]["Day"]}/${windData.data[47]["Year"]} ${windData.data[47]["Hour"]}:00`

        var dateTime = [];
        for (var i = 0; i < windData.data.length; i ++){
            dateTime[i] = windData.data[i]["Date_Time"];
        };

        var mwh = [];
        for (var i = 0; i < windData.data.length; i ++){
            mwh[i] = windData.data[i]["pred"];
        };
        
        var weatherDescription = [];
        for (var i = 0; i < windData.data.length; i ++){
            weatherDescription[i] = windData.data[i]["Weather_Description"];
        };

        var trace1 = {
            x: dateTime,
            y: mwh,
            type: "scatter",
            mode: 'lines+markers',
            line: {
                color: "#489437"
            },
            name: 'Prediction',
            hovertemplate: '<b>Output</b>: %{y:.2f} MWH' +
                        '<br><b>Time</b>: %{x}<br>' +
                        '<b>Weather</b>: %{text}',
            text: weatherDescription

        };

        var layout1 = {
            title: {text: `Wind Prediction (${startDate} - ${endDate})`},
            xaxis: {
                title: "Time"
            },
            yaxis: {
                title: "Output (MWH)"
            }
        };

    Plotly.newPlot("windPredictPlot", [trace1], layout1);

});

$.get( "/getSolar", function( data ) {
    
        var solarData = JSON.parse(data);
        var startDate = `${solarData.data[0]["Month"]}/${solarData.data[0]["Day"]}/${solarData.data[0]["Year"]} ${solarData.data[0]["Hour"]}:00`
        var endDate = `${solarData.data[47]["Month"]}/${solarData.data[47]["Day"]}/${solarData.data[47]["Year"]} ${solarData.data[47]["Hour"]}:00`
        var dateTime = [];
        for (var i = 0; i < solarData.data.length; i ++){
            dateTime[i] = solarData.data[i]["Date_Time"];
        };

        var mwh = [];
        for (var i = 0; i < solarData.data.length; i ++){
            mwh[i] = solarData.data[i]["pred"];
        };
        
        var weatherDescription = [];
        for (var i = 0; i < solarData.data.length; i ++){
            weatherDescription[i] = solarData.data[i]["Weather_Description"];
        };

        var trace1 = {
            x: dateTime,
            y: mwh,
            type: "scatter",
            mode: 'lines+markers',
            line: {
                color: "#d84100"
            },
            name: 'Prediction',
            hovertemplate: '<b>Output</b>: %{y:.2f} MWH' +
                        '<br><b>Time</b>: %{x}<br>' +
                        '<b>Weather</b>: %{text}',
            text: weatherDescription
        };

        var layout1 = {
            title: {text: `Solar Prediction (${startDate} - ${endDate})`},
            xaxis: {
                title: "Time"
            },
            yaxis: {
                title: "Output (MWH)"
            }
        };

    Plotly.newPlot("solarPredictPlot", [trace1], layout1);
});

$("#button").click(function() {
    var currentDate = $( "#datepicker" ).datepicker( "getDate" );
        day  = currentDate.getDate(),  
        month = currentDate.getMonth() + 1,              
        year =  currentDate.getFullYear();

    $.get( `/solarPredict/${year}/${month}/${day}`, function( data ) {
        var solarData = JSON.parse(data);

        var dateTime = [];
        for (var i = 0; i < 24; i ++){
            dateTime[i] = solarData.data[i]["Date_Time"];
        };

        var predMWH = [];
        for (var i = 0; i < solarData.data.length; i ++){
            predMWH[i] = solarData.data[i]["pred"];
        };

        var actualMWH = [];
        for (var i = 0; i < solarData.data.length; i ++){
            actualMWH[i] = solarData.data[i]["MWH"];
        };

        var weatherDescription = [];
        for (var i = 0; i < solarData.data.length; i ++){
            weatherDescription[i] = solarData.data[i]["Weather_Description"];
        };

        var trace1 = {
            x: dateTime,
            y: predMWH,
            type: "scatter",
            mode: 'lines+markers',
            line: {
                color: "#d84100"
            },
            name:'Predicted',
            hovertemplate: '<b>Output</b>: %{y:.2f} MWH' +
                        '<br><b>Time</b>: %{x}<br>' +
                        '<b>Weather</b>: %{text}',
            text: weatherDescription
        };

        var trace2 = {
            x: dateTime,
            y: actualMWH,
            type: "scatter",
            mode: 'lines+markers',
            line: {
                color: "#0066d8"
            },
            name:'Actual',
            hovertemplate: '<b>Output</b>: %{y:.2f} MWH' +
                        '<br><b>Time</b>: %{x}<br>' +
                        '<b>Weather</b>: %{text}',
            text: weatherDescription
        };

        var layout1 = {
            title: {text: "Solar: Model Prediction vs Actual Output"},
            xaxis: {
                title: "Time"
            },
            yaxis: {
                title: "Output (MWH)"
            }
        };

    Plotly.newPlot("solarHistoryPlot", [trace1, trace2], layout1);
    });

    $.get( `/windPredict/${year}/${month}/${day}`, function( data ) {
        var windData = JSON.parse(data);

        var dateTime = [];
        for (var i = 0; i < 24; i ++){
            dateTime[i] = windData.data[i]["Date_Time"];
        };

        var predMWH = [];
        for (var i = 0; i < windData.data.length; i ++){
            predMWH[i] = windData.data[i]["pred"];
        };

        var actualMWH = [];
        for (var i = 0; i < windData.data.length; i ++){
            actualMWH[i] = windData.data[i]["MWH"];
        };

        var weatherDescription = [];
        for (var i = 0; i < windData.data.length; i ++){
            weatherDescription[i] = windData.data[i]["Weather_Description"];
        };

        var trace1 = {
            x: dateTime,
            y: predMWH,
            type: "scatter",
            mode: 'lines+markers',
            line: {
                color: "#489437"
            },
            name:'Predicted',
            hovertemplate: '<b>Output</b>: %{y:.2f} MWH' +
                        '<br><b>Time</b>: %{x}<br>' +
                        '<b>Weather</b>: %{text}',
            text: weatherDescription

        };

        var trace2 = {
            x: dateTime,
            y: actualMWH,
            type: "scatter",
            mode: 'lines+markers',
            line: {
                color: "#0066d8"
            },
            name: 'Actual',
            hovertemplate: '<b>Output</b>: %{y:.2f} MWH' +
                        '<br><b>Time</b>: %{x}<br>' +
                        '<b>Weather</b>: %{text}',
            text: weatherDescription
        };

        var layout1 = {
            title: {text: "Wind: Model Prediction vs Actual Output"},
            xaxis: {
                title: "Time"
            },
            yaxis: {
                title: "Output (MWH)"
            }
        };

    Plotly.newPlot("windHistoryPlot", [trace1,trace2], layout1);
    });
});