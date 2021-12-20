#include <Servo.h>
Servo ESC;     // create servo object to control the ESC
int potValue; 

int c = 0;
int rpm = 0;
int d = 0;
int prev = 1;
volatile bool bFlag = false;

void setup() {

  cli();
  TCCR4A = 0;// set entire TCCR1A register to 0
  TCCR4B = 0;// same for TCCR1B
  TCNT4  = 0;//initialize counter value to 0
  // set compare match register for 1hz increments
  OCR4A = 62499;// = (16*10^6) / (1*1024) - 1 (must be <65536)
  // turn on CTC mode
  TCCR4B |= (1 << WGM42);
  // Set CS10 and CS32 bits for 1024 prescaler
  TCCR4B |= (1 << CS42) | (1 << CS40); 
  // enable timer compare interrupt
  TIMSK4 |= (1 << OCIE4A);

  sei();

  pinMode(A0, INPUT);
  pinMode(4, INPUT);
  Serial.begin(9600);
  ESC.attach(9,1000,2000);

}

void loop() {
  potValue = analogRead(A0);   // reads the value of the potentiometer (value between 0 and 1023)
  potValue = map(potValue, 0, 1023, 0, 180);   // scale it to use it with the servo library (value between 0 and 180)
  ESC.write(potValue);
  //Serial.println(analogRead(A0));
  if(analogRead(A0)>600 && prev <600){
    c+=1;
  }
  prev=analogRead(A0);
  if (bFlag){
    //Serial.print("RPM ");
    Serial.println(c*0.4);
    c = 0;
    bFlag = false;
  }
}

ISR(TIMER4_COMPA_vect){
  bFlag = true;
}
