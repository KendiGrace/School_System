int RED=1;
int GREEN=2;
int ORANGE=7;

void setup()
{
  pinMode(RED, OUTPUT);
  pinMode(GREEN,OUTPUT);
  pinMode(ORANGE,OUTPUT);
}

void loop(){
  int j=1;
  while (j<=5)
  { digitalWrite(RED, HIGH);
  delay(1000); 
  digitalWrite(RED, LOW);
  delay(1000); 
   j++;
}
  int k=1;
   while(k<=3)
   { digitalWrite(GREEN,HIGH);
   delay(1000);
   digitalWrite(GREEN,LOW);
   delay(1000);
   k++;
  }
  int l=1;
   while(l<=4)
   {digitalWrite(ORANGE,HIGH);
   delay(1000);
   digitalWrite(ORANGE,LOW);
   delay(1000);
   l++;
  }
}