void drive_motors(double val);
void drive_motors_backwards(double val);

void setup() {
  // put your setup code here, to run once:
  pinMode(9,OUTPUT);
  pinMode(5,OUTPUT);
  pinMode(6,OUTPUT);
  pinMode(11,OUTPUT);
  pinMode(7,OUTPUT);
  pinMode(8,OUTPUT);
  pinMode(13,OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available() > 0){
    char msg = Serial.read();
    if(msg == 'p')
      digitalWrite(13,HIGH);
    else if(msg == 'o')
      digitalWrite(13,LOW);  
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
