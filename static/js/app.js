$( "#datepicker" ).datepicker( "setDate", "04/20/2018" );

$.post( "/getwind", function( data ) {
    var windData = JSON.parse(data);

        var dateTime = [];
        for (var i = 0; i < windData.data.length; i ++){
            dateTime[i] = windData.data[i]["Date_Time"];
        };
        // console.log(dateTime)

        var mwh = [];
        for (var i = 0; i < windData.data.length; i ++){
            mwh[i] = windData.data[i]["pred"];
        };
        // console.log(mwh)

        var trace1 = {
            x: dateTime,
            y: mwh,
            type: "line"
        };

        var layout1 = {
            title: {text: "Wind Prediction"},
            xaxis: {
                title: "Date"
            },
            yaxis: {
                title: "MWH"
            }
        };

    Plotly.newPlot("windPredictPlot", [trace1], layout1);

    // $( "#somePlot" ).html( windDataTwo );
});

$.get( "/getSolar", function( data ) {
    
        var solarData = JSON.parse(data);
        console.log(solarData);
        var dateTime = [];
        for (var i = 0; i < solarData.data.length; i ++){
            dateTime[i] = solarData.data[i]["Date_Time"];
        };
        // console.log(dateTime)

        var mwh = [];
        for (var i = 0; i < solarData.data.length; i ++){
            mwh[i] = solarData.data[i]["pred"];
        };
        // console.log(mwh)

        var trace1 = {
            x: dateTime,
            y: mwh,
            type: "line"
        };

        var layout1 = {
            title: {text: "Solar Prediction"},
            xaxis: {
                title: "Time"
            },
            yaxis: {
                title: "MWH"
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

        console.log(solarData);

        var dateTime = [];
        for (var i = 0; i < 24; i ++){
            dateTime[i] = i;
        };
        console.log(dateTime);

        var predMWH = [];
        for (var i = 0; i < solarData.data.length; i ++){
            predMWH[i] = solarData.data[i]["pred"];
        };
        console.log(predMWH);

        var actualMWH = [];
        for (var i = 0; i < solarData.data.length; i ++){
            actualMWH[i] = solarData.data[i]["MWH"];
        };
        console.log(actualMWH);

        var trace1 = {
            x: dateTime,
            y: predMWH,
            type: "line"
        };

        var trace2 = {
            x: dateTime,
            y: actualMWH,
            type: "line"
        };

        var layout1 = {
            title: {text: "Date vs MWH"},
            xaxis: {
                title: "Date"
            },
            yaxis: {
                title: "MWH"
            }
        };

    Plotly.newPlot("solarHistoryPlot", [trace1, trace2], layout1);
    });

    $.get( `/windPredict/${year}/${month}/${day}`, function( data ) {
        var windData = JSON.parse(data);

        var dateTime = [];
        for (var i = 0; i < 24; i ++){
            dateTime[i] = i;
        };

        var predMWH = [];
        for (var i = 0; i < windData.data.length; i ++){
            predMWH[i] = windData.data[i]["pred"];
        };

        var actualMWH = [];
        for (var i = 0; i < windData.data.length; i ++){
            actualMWH[i] = windData.data[i]["MWH"];
        };
        console.log(actualMWH);

        var trace1 = {
            x: dateTime,
            y: predMWH,
            type: "line"
        };

        var trace2 = {
            x: dateTime,
            y: actualMWH,
            type: "line"
        };

        var layout1 = {
            title: {text: "Date vs MWH"},
            xaxis: {
                title: "Date"
            },
            yaxis: {
                title: "MWH"
            }
        };

    Plotly.newPlot("windHistoryPlot", [trace1,trace2], layout1);
    });
});