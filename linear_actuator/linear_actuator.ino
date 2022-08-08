byte Speed = 0; // Intialize Varaible for the speed of the motor (0-255);
int IN1 = 9; // 왼쪽 줄이기
int IN2 = 8; // 왼쪽 늘리기
int IN3 = 7; //오른쪽 줄이기
int IN4 = 6; //오른쪽 늘리기

void setup() {
pinMode(IN1, OUTPUT);
pinMode(IN2, OUTPUT);
pinMode(IN3, OUTPUT);
pinMode(IN4, OUTPUT);

}

void loop() {
  // Extend Actuator at Full Speed
  Speed = 255;
  analogWrite(IN1, 0);
  analogWrite(IN2, Speed);
  analogWrite(IN3, 0);
  analogWrite(IN4, Speed);

  delay(3000);
  analogWrite(IN1, Speed);
  analogWrite(IN2, 0);
  analogWrite(IN3, Speed);
  analogWrite(IN4, 0);
  delay(3000);
}
