
import express from "express";
const app= express();
import * as dotenv from 'dotenv' 
dotenv.config()

app.use(express.json());
let accountSid='AC1c0a96e3d7f4756b98d4045b5b5164f0';

import dbconnection from "./mongoDB"
import { whatsappmsg,sendTextmsg } from "./sms";
import CrimeModel from "./databaseModel"

const client = require('twilio')(accountSid,process.env.authToken);


   const savetoDB = async (req,res)=>{
    const crime = new CrimeModel({
        alertLevel:"high",
        crime :"fighting",
        location:"Maharaja Agrasen Institute Of Technology"
    })
    let report;
        try {
            report =  await crime.save();
            console.log(report)
            /*
            console.log(res);
            return res.write({
                success: true,
                message: 'Crime has been successfully saved',
                data: report
            })
            */
        } catch (error) {
            console.log(error);
            /*
          return res.json({
            success: false,
            message: 'Some Error occurred while saving the crime. Contact your administrator'
            });
            */
        }
    }
    
    savetoDB();   
    whatsappmsg();



app.listen(process.env.PORT || 5000,()=>{
  
    dbconnection()
    .then(() => console.log("Server is running 🚀 and connected to DB"))
    .catch((error) =>{
    console.log(error);
      console.log("Server is running, but database connection failed... ")
    }
    )
  })
