#define sensor_1 10
#define sensor_2 9

int lmPin = 0;
int fan = 12;
int led = 13;

int counter = 0;

void increment(){
  counter++;
  delay(2000);
}

void decrement() {
  if(counter == 0)
    return;
  counter--;
  delay(2000);
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  analogReference(INTERNAL);
  pinMode(lmPin,INPUT);
  pinMode(fan,OUTPUT);
  pinMode(led,OUTPUT);
  pinMode(sensor_1,INPUT);
  pinMode(sensor_2,INPUT);
}

void loop() 
{
  if(!digitalRead(sensor_1)) {
    Serial.print("1st:");
    Serial.print(digitalRead(sensor_1));
    Serial.println();
    increment();
  }
  if(!digitalRead(sensor_2)) {
    Serial.print("2nd:");
    Serial.print(digitalRead(sensor_2));
    decrement();
  }
  float temp = findTemperature();
  if(temp >= 32.0 and counter > 0) {
    digitalWrite(fan,HIGH);
  } else {
    digitalWrite(fan,LOW); 
  }
  delay(3000);

  if(counter <=0)
  {
    Serial.println("No person");
  }
  Serial.print("Counter:"); 
  Serial.print(counter);
  Serial.println();
}


float findTemperature() {
  float temp = analogRead(lmPin);
  temp = temp/9.31;
  Serial.print("Temperature is:");
  Serial.print(temp);
  Serial.println();
  return temp;
}


