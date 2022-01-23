String pressedKeys;

void setup()
{
  Serial.begin(115200);
  pinMode(13, INPUT); //W
  pinMode(12, INPUT); //A
  pinMode(11, INPUT); //S
  pinMode(10, INPUT); //D
}

void loop()
{

  if (digitalRead(13) == HIGH){
    pressedKeys = pressedKeys + "0 ";
  }
  if (digitalRead(12) == HIGH){
    pressedKeys = pressedKeys + "1 ";
  }
  if (digitalRead(11) == HIGH){
    pressedKeys = pressedKeys + "2 ";
  }
  if (digitalRead(10) == HIGH){
    pressedKeys = pressedKeys + "3 ";
  }
  Serial.println(pressedKeys);
  pressedKeys = "";

}
