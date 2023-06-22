
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
//whatsappmsg();
/*
app.listen(process.env.PORT || 5000,()=>{
  
    dbconnection()
    .then(() => console.log("Server is running 🚀 and connected to DB"))
    .catch((error) =>{
    console.log(error);
      console.log("Server is running, but database connection failed... ")
    }
    )
  })
*/
export async function sendTextmsg(){
    try {
        const message = await client.messages.create({
          body: 'ALERT',
          to: 'whatsapp: +917838584710',
         // to: 'whatsapp: +919667866901',
          
          from: 'whatsapp: +14344236484'
          
        });
        console.log(message);
      } catch (error) {
        // You can implement your fallback code here
        console.error(error);
      }
      
}
 

export async function  whatsappmsg(){    
    try {
    const message= await client.messages.create({
        body: `ALERT: HIGH,
        CRIME: FIGHTING,
        LOCATION:Maharaja Agrasen Institute Of Technology 
        `,
        from: 'whatsapp:+14155238886',
        to: 'whatsapp:+917838584710'
    })
    //console.log(message)
  
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