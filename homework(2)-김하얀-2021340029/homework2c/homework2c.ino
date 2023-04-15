int leds[] = {2, 3, 4, 5, 6, 7, 8, 9}; // LED가 연결된 핀 번호


void setup() {
  Serial.begin(9600);
  for(int i=0; i<8; i++) {
    pinMode(leds[i], OUTPUT); // 각각의 LED 핀을 출력 모드로 설정
  }
}
//성공 확인
void base(){
  for(int j=0; j<3; j++) {
    for(int i=0; i<8; i++) {
      digitalWrite(leds[i], HIGH);
      delay(50);  
      digitalWrite(leds[i], LOW);
    }

    for(int i=7; i>=0; i--) {
      digitalWrite(leds[i], HIGH);
      delay(50); 
      digitalWrite(leds[i], LOW);
    }  
  }   
}
//성공 확인
void jumping(){
  for(int i=0;i<8;i+=2){
    digitalWrite(leds[i], HIGH);
    delay(50);
    digitalWrite(leds[i], LOW);
  }
}
//성공 확인
void acceleration(int speed, int accel){
  while(speed >=300){
    for(int i=0;i<8;i++){
     digitalWrite(leds[i], HIGH);
     delay(speed);
     digitalWrite(leds[i], LOW);
     speed = speed - accel;
    }
  }  
}
//성공 확인
void decceleration(int speed, int delaytime){
  while(speed <1000){
    for(int i=0;i<8;i++){
     digitalWrite(leds[i], HIGH);
     delay(speed);
     digitalWrite(leds[i], LOW);
     speed = speed + delaytime;
    }  
  }
}
//성공 확인
void randomplay() {
  for (int i=0;i<12;i++){
    int pin = random(0, 7);
    int delaytime = 50;
    digitalWrite(leds[pin], HIGH);
    delay(delaytime);
    digitalWrite(leds[pin], LOW);
    delay(50);
  }

}

void goingmid(){
  for (int i=0; i<4;i++){
    digitalWrite(leds[i], HIGH);
    digitalWrite(leds[7-i], HIGH);
    delay(50);
  }
  delay(500);
  for (int i=3; i>=0;i++){
  digitalWrite(leds[i], LOW);
  digitalWrite(leds[7-i], LOW);
  delay(500);   
  }
}

void loop(){
  base();
  delay(50);
  jumping();
  delay(50);
  base();
  acceleration(1000,100);
  delay(50);
  base();
  decceleration(300,120);
  delay(50);
  base();
  randomplay();
  delay(50);
  base();
  goingmid();
  exit(0);
}
