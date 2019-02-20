const express = require('express')
const fs = require('fs')
const hbs = require('hbs')
var app = express()
const port = process.env.PORT || 3000

 // app.use((req, res, next)=>{
 //   res.send("Under maintenance")
 // })

 hbs.registerPartials(__dirname+ '/views/partials')
 app.use(express.static(__dirname +'/views'))
 app.use(express.static(__dirname))
 app.set('view engine', 'hbs')


  app.use((req, res, next)=>{
    var log = (`${new Date().toString()} ${req.method} ${req.url}`);
    fs.appendFile('log.log', log + '\n', (err)=>{
      if(err){
      console.log("cannot append to log file");
    }})
    next()
  })

 hbs.registerHelper('yearT', function (context){
   const year_time = {
     year: new Date().getFullYear(),
     time: new Date().toLocaleTimeString()
   }
   return context.fn(year_time)
 })
 hbs.registerHelper('yearr', (msgg)=>{
   return msgg.toUpperCase()
 })

 app.get('/about', (req, res)=>{
   res.render('about.hbs',{
     text:'Kaise Ho, Ye about page hai',
   })
 })

 app.get('/home', (req, res)=>{
   res.render('home.hbs',{
     text:'Namaste, Ye Home page hai',
   })
 })

 app.get('/', (req, res)=>{
   res.render(index.html)
 })

 app.listen(port, ()=>{
   console.log("Starting server");
 })
