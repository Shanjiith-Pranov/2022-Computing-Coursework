String pressedKeys;

void setup()
{
  Serial.begin(115200);
  pinMode(13, INPUT); //W
  pinMode(12, INPUT); //A
  pinMode(13, INPUT); //S
  pinMode(10, INPUT); //D
}

void loop()
{

  if (digitalRead(13) == HIGH){
    pressedKeys = pressedKeys + "w "
  }
  if (digitalRead(12) == HIGH){
    pressedKeys = pressedKeys + "a "
  }
  if (digitalRead(11) == HIGH){
    pressedKeys = pressedKeys + "s "
  }
  if (digitalRead(10) == HIGH){
    pressedKeys = pressedKeys + "d "
  }
  Serial.println(pressedKeys);
  pressedKeys = "";

}
