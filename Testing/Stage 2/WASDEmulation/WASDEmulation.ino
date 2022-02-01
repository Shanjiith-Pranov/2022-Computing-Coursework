String pressedKeys;

void setup()
{
  Serial.begin(115200);
  pinMode(12, INPUT); //W
  pinMode(11, INPUT); //A
  pinMode(10, INPUT); //S
  pinMode(9, INPUT); //D
  pinMode(8, INPUT); //esc
}

void loop()
{

  if (digitalRead(12) == HIGH){
    pressedKeys = pressedKeys + "0 ";
  }
  if (digitalRead(11) == HIGH){
    pressedKeys = pressedKeys + "1 ";
  }
  if (digitalRead(10) == HIGH){
    pressedKeys = pressedKeys + "2 ";
  }
  if (digitalRead(9) == HIGH){
    pressedKeys = pressedKeys + "3 ";
  }
  if (digitalRead(8) == HIGH){
    pressedKeys = pressedKeys + "4 ";
  }
  Serial.println(pressedKeys);
  pressedKeys = "";
  delay(10);

}
