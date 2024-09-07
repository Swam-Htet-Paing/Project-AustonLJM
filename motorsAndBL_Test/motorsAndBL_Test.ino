#include "Servo.h"

Servo s1,s2;

void drive_motors(double val);
void drive_motors_backwards(double val);
short int pan_angle = 90;
short int tilt_angle = 0; 
void setup() {
  // put your setup code here, to run once:
  pinMode(9,OUTPUT);
  pinMode(5,OUTPUT);
  pinMode(6,OUTPUT);
  pinMode(11,OUTPUT);
  pinMode(7,OUTPUT);
  pinMode(8,OUTPUT);
  pinMode(12,OUTPUT);
  s1.attach(10); //Pan
  s2.attach(3);  //tilt
  s1.write(pan_angle);
  delay(3000);
  s2.write(tilt_angle);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available() > 0){
    char msg = Serial.read();
    if(msg == 'p')
      digitalWrite(12,HIGH);
    else if(msg == 'o')
      digitalWrite(12,LOW);  
    else if(msg == 'i'){
      tilt_angle++;
      s2.write(tilt_angle);
    }
    else if(msg == 'k'){
      tilt_angle--;
      s2.write(tilt_angle);    
    }
    else if(msg == 'j'){
      pan_angle++;
      s1.write(pan_angle);
    }
    else if(msg == 'l'){
      pan_angle--;
      s1.write(pan_angle);
    }
  }
  
}

void drive_motors_backwards(double val){
  analogWrite(9,val);
  digitalWrite(5,LOW);
  digitalWrite(6,HIGH);
  analogWrite(11,val);
  digitalWrite(7,LOW);
  digitalWrite(8,HIGH);
}

void drive_motors(double val){
  analogWrite(9,val);
  digitalWrite(5,HIGH);
  digitalWrite(6,LOW);
  analogWrite(11,val);
  digitalWrite(7,HIGH);
  digitalWrite(8,LOW);
  }
