
import express from "express";
const app= express();
import * as dotenv from 'dotenv' 
dotenv.config()

app.use(express.json());
let accountSid='AC1c0a96e3d7f4756b98d4045b5b5164f0';


const client = require('twilio')(accountSid,process.env.authToken);
/**
 * these are the numbers for sending sms 
 * body: 'Hello from Node you arethe best footballer',
          to: 'whatsapp: +917838584710',
          from: 'whatsapp: +14344236484'
 */

//sendTextmsg();
whatsappmsg();

app.listen(3000,()=>{
    console.log("Server is running 🚀 and connected to DB")
})


async function sendTextmsg(){
    try {
        const message = await client.messages.create({
          body: 'Hello from Node you arethe best footballer',
          to: 'whatsapp: +917838584710',
          from: 'whatsapp: +14344236484'
          
        });
        console.log(message);
      } catch (error) {
        // You can implement your fallback code here
        console.error(error);
      }
      
}


async function  whatsappmsg(){
     console.log(process.env.authToken);
    const client = require('twilio')(accountSid,process.env.authToken);
    
    try {
    const message= await client.messages.create({
        body: 'hey you are the best footballer',
        from: 'whatsapp:+14155238886',
        to: 'whatsapp:+917838584710'
    })
    console.log(message)

} catch (error) {
    console.log(error)
}
}

/*
client.messages
    .create({
        body: 'hey',
        from: 'whatsapp:+14155238886',
        to: 'whatsapp:+917838584710'
    })
    .then(message => console.log(message.sid))
    .done();
}
**/
/**
 * 
 */