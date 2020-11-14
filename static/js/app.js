

$.post( "/getwind", function( data ) {
    var windData = JSON.parse(data);

    var windDataTwo = windData["data"];
        var dateTime = [];
        for (var i = 0; i < windData.data.length; i ++){
            dateTime[i] = windData.data[i]["Date_Time"];
        };
        // console.log(dateTime)

        var mwh = [];
        for (var i = 0; i < windData.data.length; i ++){
            mwh[i] = windData.data[i]["MWH"];
        };
        // console.log(mwh)

        var trace1 = {
            x: dateTime,
            y: mwh,
            type: "bar"
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

    Plotly.newPlot("somePlot", [trace1], layout1);
    console.log(windDataTwo);

    // $( "#somePlot" ).html( windDataTwo );
})


$("#button").click(function() {
    var currentDate = $( "#datepicker" ).datepicker( "getDate" );
        day  = currentDate.getDate(),  
        month = currentDate.getMonth() + 1,              
        year =  currentDate.getFullYear();
    $.get( `/solarPredict/${year}/${month}/${day}`, function( data ) {
        var solarData = JSON.parse(data);

        var dateTime = [];
        for (var i = 0; i < 24; i ++){
            dateTime[i] = i;
        };
        console.log(dateTime);

        var mwh = [];
        for (var i = 0; i < solarData.data.length; i ++){
            mwh[i] = solarData.data[i]["pred"];
        };
        console.log(mwh);

        var trace1 = {
            x: dateTime,
            y: mwh,
            type: "bar"
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

    Plotly.newPlot("solarHistoryPlot", [trace1], layout1);
    });

});