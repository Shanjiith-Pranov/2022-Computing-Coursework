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
int enable[] = {1,1,1,1,1};

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
  if (digitalRead(button1) == LOW){
    pressedKeys = pressedKeys + "0 ";
  }
  if (digitalRead(button2) == LOW){
    pressedKeys = pressedKeys + "1 ";
  }
  if (digitalRead(enable3) == LOW){
    
  }
  if (digitalRead(button3) == LOW){
    pressedKeys = pressedKeys + "2 ";
  }
  if (digitalRead(button4) == LOW){
    pressedKeys = pressedKeys + "3 ";
  }
  if (digitalRead(button5) == LOW){
    pressedKeys = pressedKeys + "4 ";
  }
  

  Serial.println(pressedKeys);
  pressedKeys = "";
  delay(10);

}
