#include <TM1637Display.h>

const int CLK = 9; //minutes
const int DIO = 8; //seconds

int minutes = 10; 
int seconds = 0;
long millis_value=0;

TM1637Display display(CLK, DIO);

void setup()
{
  display.clear();
  display.setBrightness(0x0f);
}

void loop()
{
  displayTime(); //분과 초로 나누어져 시계에 표시됨. 현재 시각
  long start = millis();
  delay(1000);
  long end = millis();
  millis_value += (end - start);

  if (minutes == 0 && seconds == 0)
  {
    display.showNumberDec(millis_value); //밀리초단위, 10진수
    while (true);
  }
}

void displayTime()
{
  if (seconds == 0)
  {
    seconds = 59;
    minutes--;
  }
  else
  {
    seconds--;
  }
  display.showNumberDecEx(minutes * 100 + seconds);
}