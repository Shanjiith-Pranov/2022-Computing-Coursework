void setup()
{
  Serial.begin(115200);
  pinMode(13, INPUT); #W
  pinMode(12, INPUT); #A
  pinMode(13, INPUT); #S
  pinMode(10, INPUT); #D
}

void loop()
{
  if (digitalRead(13) == HIGH){
    Serial.println("w");
  }else if (digitalRead(12) == HIGH){
    Serial.println("a");
  }else if (digitalRead(11) == HIGH){
    Serial.println("s");
  }else if (digitalRead(10) == HIGH){
    Serial.println("d");
  }else{
      continue
  }
}