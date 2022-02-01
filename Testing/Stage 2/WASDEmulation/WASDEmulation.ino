String pressedKeys;
int button1 = 13; //W
int button2 = 12; //A
int button3 = 11; //S
int enable3 = 8;  //S - Enable
int button4 = 10; // D
int button5 = 9;  // Esc
int enable[] = {1,1,1,1,1};

void setup()
{
  Serial.begin(115200);
  pinMode(button1, INPUT); //W
  pinMode(button2, INPUT); //A
  pinMode(button3, INPUT); //S
  pinMode(enable3, INPUT); //S enable
  pinMode(button4, INPUT); //D
  pinMode(button5, INPUT); //esc
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
