const yargs = require('yargs')
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
var geocode = require('./geocode')
geocode.geocode(location, (errorMessage, response)=>{
  if(errorMessage){
    console.log(errorMessage)
  }
  else {
    geocode.temperature(response.Country,response.State,
      response.City,response.latitude, response.longitude, (errorMsg, response)=>{
      if(errorMsg){
        console.log("Something went wrong while finding the temperature")
      }
      else {
        console.log(`Country:${response.Country}\nState:${response.State}\nCity:${response.City}`)
        console.log(`Actual temperature=${((response.temperature-32)*(5/9)).toFixed(2)} celsius`)
        console.log(`It feels like:${((response.apparentTemperature-32)*5/9).toFixed(2)} celsius`)
      }
    })
  }
})
