const config = require('./config')
const request = require('request')
var geocode = (location, callback)=> {
  request({
    url:`${config.mapquest_api}key=${config.mapquest_key}&location=${location}`,
    json:true
  },(error, response, body)=>{
    if(error){
      callback("Something went wrong")
    }
    else if(body.info.statuscode == 602){
      callback("Address not found")
    }
    else {
      callback(undefined,{
      latitude: body.results[0].locations[0].latLng.lat,
      longitude:body.results[0].locations[0].latLng.lng,
      Country:body.results[0].locations[0].adminArea1,
      State:body.results[0].locations[0].adminArea3,
      City:body.results[0].locations[0].adminArea5
    })
    }
  })
}
var temperature = (country, state, city, lat, long, callback)=> {
  request({
    url:`${config.darksky_api}${config.darksky_key}/${lat},${long}`,
    json:true
  },(error, response, body)=>{
    if(error){
      callback("Oops, Something went wrong")
    }
    else if (body.statusCode==404) {
      console.log("Failed to fetch the weather");
    }
    else {
      callback(undefined,{
        Country:country,
        State:state,
        City:city,
        timezone:body.timezone,
        temperature:body.currently.temperature,
        apparentTemperature:body.currently.apparentTemperature
    })
    }
  })
}

module.exports = {
  geocode,
  temperature
}
