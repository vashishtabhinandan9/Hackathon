
/*
 * This ESP32 code is created by esp32io.com
 *
 * This ESP32 code is released in the public domain
 *
 * For more detail (instruction and wiring diagram), visit https://esp32io.com/tutorials/esp32-light-sensor
 */

// constants won't change

#define LIGHT_SENSOR_PIN  15  // ESP32 pin GIOP36 (ADC0) connected to light sensor for taking input
#define LED_PIN           22  // ESP32 pin GIOP22 connected to LED //output
#define LED_PIN2          21
#define ANALOG_THRESHOLD  2500//threshold of ldr 
#define RADAR  18
bool radardetect =false;//radar has detected something
bool val= false;//to read current value of radar
int p=0;//to store value of val 

//#define TRIG_PIN 23 // ESP32 pin GIOP23 connected to Ultrasonic Sensor's TRIG pin
//#define ECHO_PIN 13 // ESP32 pin GIOP13 connected to Ultrasonic Sensor's ECHO pin
//bool  cam = false;
String work;
//float duration_us, distance_cm;

void setup() {

   Serial.begin (9600);
   pinMode(LED_PIN, OUTPUT); // set ESP32 pin to output mode for ldr
   pinMode(LED_PIN2, OUTPUT); // set ESP32 pin to output mode for ldr
   
  pinMode (RADAR, INPUT);
}

void loop() {
  int analogValue = analogRead(LIGHT_SENSOR_PIN); // read the value on analog pin //takes in the input od ldr sensor 
   Serial.println(analogValue);
  //if (analogValue > ANALOG_THRESHOLD) // digitalWrite(LED_PIN2, HIGH);
   // else digitalWrite(LED_PIN2, LOW);



  // if (Serial.available() > 0){
  //    if (Serial.read() == 'x')cam =true;
  // } 
  // else if (Serial.read() == 'y') cam =false;

    if (analogValue > ANALOG_THRESHOLD){ 
      digitalWrite(LED_PIN2, HIGH);


      val = digitalRead(RADAR);//radar do it works 
      Serial.println("radar read ");
      Serial.println(val);

      if(val==1){
     // p=val;
      // digitalWrite(LED_PIN, HIGH);
     if (Serial.available() > 0){
       // read the incoming byte:
       work = "";
       while(Serial.available() > 0){ 
         char Serial_Data= Serial.read();
         
         work=work+Serial_Data;  
         //if(Serial_Data == "y")
        // if (Serial.read() == 'x')  {} digitalWrite(LED_PIN, HIGH);
           // delay(1000);
      }
        //if(work!="")
        //int incomingByte = Serial.read();
        Serial.println(" I received:");
       Serial.println(work);
       digitalWrite(LED_PIN, HIGH);

       
       Serial.end();
       Serial.begin(9600);
       delay(1000);
        //digitalWrite(LED_PIN, LOW);
      
  }
  else  {
     Serial.println("turn off due camera");
    digitalWrite(LED_PIN, LOW);

  }
    
 } // turn on LED
      
      else{//flag=0; 
        Serial.println("turn off due radar");//no person is around the light // false reading by US
        digitalWrite(LED_PIN, LOW);
        }
      }
    //else{digitalWrite(LED_PIN, LOW);}//person exits 11111111111111111111

  

  
  
    else{
   digitalWrite(LED_PIN, LOW); 
   digitalWrite(LED_PIN2, LOW); 
   
   Serial.println(" => turn off due ldr");
   //cam=false;
  }

}

