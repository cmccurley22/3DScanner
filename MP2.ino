#include <Servo.h>

Servo panX;
Servo tiltY;
const uint8_t IR_SENS = A0;

const uint8_t PAN_INCREMENT = 1; // increment of pan angle in degrees
const uint8_t TILT_INCREMENT = 1; // increment of tilt angle in degrees
const uint8_t NUM_READINGS = 3; // number of readings taken at each point
const uint32_t DELAY = 50; // delay in ms between servo movements

int sum = 0; // for averaging sensor values
int a;

bool scanning = 1;

void setup() {
  panX.attach(7);
  tiltY.attach(8);

  pinMode(IR_SENS, INPUT);

  Serial.begin(9600);

  delay(5000); // time to start python script
}

void loop() {
  while(scanning) {
    // go through all tilt angles
    panX.write(70);
    for(int i = 120; i >= 90; i--) {
      tiltY.write(i);
      // go through all pan angles
        for(int j = 45; j <= 95; j++) {
          // check if moving left or right (for scanning back and forth)
          if(i % 2 == 0) {
            a = j;
          }
          else {
            a = 140 - j;
          }

          panX.write(a);
  
          delay(DELAY * 3); // wait briefly before taking data
  
          // take NUM_READINGS readings from the sensor and average them
          for(int n = 0; n < NUM_READINGS; n++) {
            sum += analogRead(IR_SENS);
          }
  
          // send angles and sensor data to Python
          Serial.println(String(i) + ", " + String(a) + ", " + String(sum / NUM_READINGS));

          sum = 0;
      }
    }
    Serial.println("end"); // let Python know the scan is complete
    scanning = 0; // stop moving Servos / taking data once scan is complete
  }
}
