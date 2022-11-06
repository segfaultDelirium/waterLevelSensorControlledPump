//#import <math.h>

#define FULLY_SUBMERGED 415
#define DRY 562
#define PUMP_PIN 2

#define DEFAULT_SUBMERSION_PERCENTAGE 50

// x is reading
int readingToPercentage(int x){
    float pow5 = -1.87999508 * pow(10, -8) * pow(x, 5);
    float pow4 = 4.65073582 * pow(10, -5) * pow(x, 4);
    float pow3 = -4.60101228 * pow(10, -2) * pow(x, 3);
    float pow2 = 2.27579576 * 10 * pow(x, 2); 
    float pow1 = -5.62915049 *pow(10, 3) * x;
    float pow0 = 5.57155616 * pow(10, 5); 
    return pow5 + pow4 + pow3 + pow2 + pow1 + pow0;
}



int receiveSubmersionCommand(int previousSetting){
    if(Serial.available() <= 0) return previousSetting;
    int submersionPercentageSet = Serial.readString().toInt();
    return submersionPercentageSet;
}

// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);

  int sensorValue = analogRead(A0);
  int submersionPercentageReading = readingToPercentage(sensorValue);
  int submersionPercentageSet = receiveSubmersionCommand(DEFAULT_SUBMERSION_PERCENTAGE);

  while(true){
    sensorValue = analogRead(A0);
    submersionPercentageReading = readingToPercentage(sensorValue);
    submersionPercentageSet = receiveSubmersionCommand(submersionPercentageSet);
    
    Serial.print("sensorValue: ");
    Serial.println(sensorValue);
    
    Serial.print("current percentage of submersion: ");
    Serial.println(submersionPercentageReading);
    
    Serial.print("Required percentage of submersion: ");
    Serial.println(submersionPercentageSet);
    
    if(submersionPercentageReading < submersionPercentageSet ){
      digitalWrite(PUMP_PIN, HIGH);
    }else{
      digitalWrite(PUMP_PIN, LOW);
    }
    
    delay(500);  
    
    
  }
  
}




void loop() {
  
}
