const yargs = require('yargs')
const axios  = require('axios')
const config = require('./config')
const argv = yargs
            .options({
              address:{
                demand:true,
                alias:'a',
                describe:'Address for weather app',
                string:true
              }
            })
            .help()
            .argv
var location = encodeURIComponent(argv.address)
var geocodeUrl = `${config.mapquest_api}key=${config.mapquest_key}&location=${location}`
axios.get(geocodeUrl).then((response)=>{
  if(response.data.statusCode==404){
    throw new Error("Could not find given address")
  }
  var lat =  response.data.results[0].locations[0].latLng.lat
  var long = response.data.results[0].locations[0].latLng.lng
  var weatherUrl = `${config.darksky_api}${config.darksky_key}/${lat},${long}`
  axios.get(weatherUrl).then((weather_response)=>{
    console.log(response.data.results[0].locations[0].adminArea1)
    console.log(response.data.results[0].locations[0].adminArea3)
    console.log(response.data.results[0].locations[0].adminArea5)
    console.log(weather_response.data.currently.temperature)
    console.log(weather_response.data.currently.apparentTemperature);
  }).catch((e)=>{
    console.log("Somethig went wrong while fetching the climate");
  })
}).catch((e)=>{
  console.log("Somethig went wrong while fetching location");
})
