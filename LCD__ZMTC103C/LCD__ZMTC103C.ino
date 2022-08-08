int currentPin = A0;

void setup(){
  Serial.begin(9600);
}

void loop(){
  float current = 0;
  current = analogRead(currentPin);
  if(current > 0){ 
    Serial.println(current); 
  }
  else{
    Serial.println(current);
  }
  delay(1000);
}
