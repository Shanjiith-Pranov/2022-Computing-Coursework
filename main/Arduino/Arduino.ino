String pressedKeys;
int button1 = 13; // W
int button2 = 12; // A
int button3 = 11; // S
int button4 = 10; // D
int button5 = 9;  // Esc

void setup()
{
  Serial.begin(115200);
  pinMode(button1, INPUT);
  pinMode(button2, INPUT);
  pinMode(button3, INPUT);
  pinMode(enable3, INPUT);
  pinMode(button4, INPUT);
  pinMode(button5, INPUT);
}

void loop()
{
  if (digitalRead(button1) == HIGH)
  {
    pressedKeys = pressedKeys + "0 ";
  }
  if (digitalRead(button2) == HIGH)
    {
      pressedKeys = pressedKeys + "1 ";
    }
  if (digitalRead(button3) == HIGH)
  {
    pressedKeys = pressedKeys + "2 ";
  }
  if (digitalRead(button4) == HIGH)
    {
      pressedKeys = pressedKeys + "3 ";
    }
  if (digitalRead(button5) == HIGH)
  {
    pressedKeys = pressedKeys + "4 ";
  }
  Serial.println(pressedKeys);
  pressedKeys = "";
  Serial.println(enable)
      delay(10);
}
