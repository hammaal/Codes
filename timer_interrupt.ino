#include<Wire.h>

void setup() {
  cli();
  TCCR1A = 0;// set entire TCCR1A register to 0
  TCCR1B = 0;// same for TCCR1B
  TCNT1  = 0;//initialize counter value to 0
  // set compare match register for 1hz increments
  OCR1A = 1249;// = (16*10^6) / (1*1024) - 1 (must be <65536)
  // turn on CTC mode
  TCCR1B |= (1 << WGM12);
  // Set CS10 and CS12 bits for 1024 prescaler
  TCCR1B |= (1 << CS11);  
  // enable timer compare interrupt
  TIMSK1 |= (1 << OCIE1A);

  sei();
  Serial.begin(115200);
  Wire.begin();
  Wire.setClock(400000);
  Wire.beginTransmission(0x53);
  Wire.write(0x2D);
  Wire.write(8);
  Wire.write(0x2C);
  Wire.write(0x0B);
  Wire.endTransmission();
  delay(10);
  
}

void loop() {
  // put your main code here, to run repeatedly:

}

ISR(TIMER1_COMPA_vect){
  Wire.beginTransmission(ADXL345);
  Wire.write(0x36);
  Wire.endTransmission(false);
  Wire.requestFrom(ADXL345, 2, true);
  Serial.println((Wire.read()|Wire.read() << 8));
}
