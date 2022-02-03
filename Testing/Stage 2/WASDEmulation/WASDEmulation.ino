String pressedKeys;
int button1 = 13; // W
int enable1 = 8;  // W   - Enable
int button2 = 12; // A
int enable2 = 7;  // A   - Enable
int button3 = 11; // S
int enable3 = 6;  // S   - Enable
int button4 = 10; // D
int enable4 = 5;  // D   - Enable
int button5 = 9;  // Esc
int enable5 = 4;  // Esc - Enable
String enable;

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

  if (digitalRead(enable1) == HIGH)
  {
    enable = enable + "1 ";
    if (digitalRead(button1) == HIGH)
    {
      pressedKeys = pressedKeys + "0 ";
    }
  }
  else
  {
    enable = enable + "0 ";
  }
  if (digitalRead(enable2) == HIGH)
  {
    enable = enable + "1 ";
    if (digitalRead(button2) == HIGH)
    {
      pressedKeys = pressedKeys + "1 ";
    }
  }
  else
  {
    enable = enable + "0 ";
  }
  if (digitalRead(enable3) == HIGH)
  {
    enable[2] = 1;
    if (digitalRead(button3) == HIGH)
    {
      pressedKeys = pressedKeys + "2 ";
    }
  }
  else
  {
    enable = enable + "0 ";
  }
  if (digitalRead(enable4) == HIGH)
  {
    enable = enable + "1 ";
    if (digitalRead(button4) == HIGH)
    {
      pressedKeys = pressedKeys + "3 ";
    }
  }
  else
  {
    enable = enable + "0 ";
  }
  if (digitalRead(enable5) == HIGH)
  {
    enable = enable + "1 ";
    if (digitalRead(button5) == HIGH)
    {
      pressedKeys = pressedKeys + "4 ";
    }
  }
  else
  {
    enable = enable + "0 ";
  }

  Serial.println(pressedKeys);
  pressedKeys = "";
  Serial.println(enable)
      delay(10);
}
