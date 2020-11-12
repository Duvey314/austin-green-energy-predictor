d3.json("../static/json/wind_data.json").then((data) => {
    var windData = data
    // // print the windData to the consol: data and schema
    // console.log(windData)
    
    // // print the data from the wind data to the console
    // // each index is a row from the dataframe
    // console.log(windData.data)
    // console.log(windData.data[0])
    // console.log(windData.data[31390])

    // print each column from each row
    console.log(windData.data[0]["Date_Time"])
    console.log(windData.data[0]["Year"])
    console.log(windData.data[0]["Month"])
    console.log(windData.data[0]["Day"])
    console.log(windData.data[0]["Hour"])
    console.log(windData.data[0]["MWH"])
    console.log(windData.data[0]["Temperature_F"])
    console.log(windData.data[0]["Humidity_percent"])
    console.log(windData.data[0]["WindSpeed_mph"])
    console.log(windData.data[0]["WindGust_mph"])
    console.log(windData.data[0]["WindDirection_degrees"])
    console.log(windData.data[0]["WindDirection_compass"])
    console.log(windData.data[0]["Weather_Description"])
});