#include <Servo.h>

Servo myservo;

void setup() {
  // put your setup code here, to run once:
  myservo.attach(4);
  pinMode(A0, INPUT);
  myservo.write(0);
}

void loop() {
  // put your main code here, to run repeatedly:
  int angle = map(analogRead(A0), 0,1023, 0,180);
  myservo.write(angle);
}
