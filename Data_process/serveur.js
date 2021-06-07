var express = require('express');

var app = express();



const path = require("path");



    var mustache = require('mustache-express');
    const multer = require("multer");

    var bodyParser = require('body-parser');








    app.engine('html', mustache());
    app.set('view engine', 'html');
    app.set('views', '/home/jordan/Documents/TIPE/Data_process/View');


app.get('/',function (req,res) {
    var getterData = require('./Controller/dataController');
    var data = getterData.getCurrentData()
    let Current_Amp = data.Amp;
    let Current_Vol =  data.Volt ;
    let Current_Resistance = (Current_Amp == 0 ) ? 'Résistance infinie' : Current_Vol / Current_Amp+" Ohms";
    Current_Vol += " Volts"
    Current_Amp += " Ampères"
    let Current_Alt =  data.Alt +" Mètres";
    let Current_Long =  data.Long;
    let Current_Lat =  data.Lat ;
    let Current_Time =  data.Time+" Secondes" ;
    let Current_FlightTime = getterData.getFlightTime()+" minutes" ;
    console.log(data)
    let Current_Temp=  data.Temperature   +" °C";

    let display = {Current_Amp : Current_Amp , Current_Vol :Current_Vol  ,Current_Resistance : Current_Resistance
        ,Current_Alt :Current_Alt, Current_Long : Current_Long ,  Current_Lat :Current_Lat ,Current_Time: Current_Time,
        Current_FlightTime :Current_FlightTime ,Current_Temp: Current_Temp
    }
    res.render('/home/jordan/Documents/TIPE/Data_process/View/index',{display : display})

})








app.listen(3000, () => console.log('░█▀█░█▀▄░█▀█░▀▀█░█▀▀░▀█▀░░░▀█▀░▀█▀░█▀█░█▀▀\n'+
'░█▀▀░█▀▄░█░█░░░█░█▀▀░░█░░░░░█░░░█░░█▀▀░█▀▀\n'+
'░▀░░░▀░▀░▀▀▀░▀▀░░▀▀▀░░▀░░░░░▀░░▀▀▀░▀░░░▀▀▀\n'+
    'Server is Running on port 3000 ! http://localhost:3000'
));