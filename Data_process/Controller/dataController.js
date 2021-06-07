var Sqlite = require('better-sqlite3');
var db = new Sqlite('Database/DataBase.sqlite');


exports.getCurrentData= function(){
    let select = db.prepare('Select * from data  WHERE id=(SELECT max(id) FROM data)');
    return select.get()
}



exports.getFlightTime = function () {
    let select = db.prepare('Select Time from data  WHERE id=(SELECT min(id) FROM data)');
    let startDate = select.get().Time.split(' ')[1]
    let startHour = parseInt(startDate.split(':')[0])
    let startMin = parseInt(startDate.split(':')[1])


    let date = new Date;

    return Math.abs(startMin-date.getMinutes()+((startHour-date.getHours())*60))
}