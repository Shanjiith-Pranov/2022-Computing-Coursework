void setup()
{
  Serial.begin(115200);
  pinMode(13, INPUT);
  pinMode(12, INPUT);
  pinMode(13, INPUT);
  pinMode(10, INPUT);
}

void loop()
{
  if (digitalRead(13) == HIGH){
    Serial.println("W");
  }else if (digitalRead(12) == HIGH){
    Serial.println("A");
  }else if (digitalRead(11) == HIGH){
    Serial.println("S");
  }else if (digitalRead(10) == HIGH){
    Serial.println("D");
  }else{
      continue
  }
}