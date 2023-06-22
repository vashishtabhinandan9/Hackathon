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
#define ANALOG_THRESHOLD  1000//threshold of ldr 
#define RADAR  18
bool radardetect =false;//radar has detected something
bool val= false;//to read current value of radar
int p=0;//to store value of val 

#define TRIG_PIN 23 // ESP32 pin GIOP23 connected to Ultrasonic Sensor's TRIG pin
#define ECHO_PIN 13 // ESP32 pin GIOP13 connected to Ultrasonic Sensor's ECHO pin
bool  cam = false;

float duration_us, distance_cm;

void setup() {

   Serial.begin (9600);
   pinMode(LED_PIN, OUTPUT); // set ESP32 pin to output mode for ldr
  // pinMode(LED_PIN2, OUTPUT); // set ESP32 pin to output mode for ldr
   
  pinMode (RADAR, INPUT);
}

void loop() {
  int analogValue = analogRead(LIGHT_SENSOR_PIN); // read the value on analog pin //takes in the input od ldr sensor 
  // Serial.println(analogValue);
  //if (analogValue > ANALOG_THRESHOLD) // digitalWrite(LED_PIN2, HIGH);
   // else digitalWrite(LED_PIN2, LOW);



  if (Serial.available() > 0){
     if (Serial.read() == 'x')cam =true;
  } 
  else if (Serial.read() == 'y') cam =false;

    if (analogValue > ANALOG_THRESHOLD){ 


      val = digitalRead(RADAR);//radar do it works 
      Serial.println("radar read ");
      Serial.println(val);

      if(val==1){
     // p=val;
     if (Serial.available() > 0){
        while(Serial.available() > 0){ 
            digitalWrite(LED_PIN, HIGH);
            delay(2000);
       }
        digitalWrite(LED_PIN, LOW);
      
  }
  else  {
     Serial.println("turn off due camera")
    digitalWrite(LED_PIN, LOW);

  }
    
      } // turn on LED// some movement is detected near light
      
      else{//flag=0; 
        Serial.println("turn off due radar");//no person is around the light // false reading by US
        digitalWrite(LED_PIN, LOW);
        }
      }
    //else{digitalWrite(LED_PIN, LOW);}//person exits 11111111111111111111

  

  
  
else{
   digitalWrite(LED_PIN, LOW); 
   Serial.println(" => turn off due ldr");
   cam=false;
}

}

