void setup()
{
  Serial.begin(115200);  
  pinMode(12, INPUT);
}

void loop()
{
  if (digitalRead(12) == HIGH){
    Serial.println("On");
  } else {
    Serial.println("Off");
  }
  
    delay(40);
}
