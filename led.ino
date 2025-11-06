#include <Adafruit_NeoPixel.h>

#define LED_PIN 6
#define NUM_LEDS 60
Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUM_LEDS, LED_PIN, NEO_GRB + NEO_KHZ800);

void setup()
{
  Serial.begin(115200);
  strip.begin();
  strip.show();
}

void loop()
{
  if (Serial.available() > 0)
  {
    if (Serial.read() == 255)
    { // start byte
      for (int i = 0; i < NUM_LEDS; i++)
      {
        while (Serial.available() < 3)
          ; // wait for R G B
        int r = Serial.read();
        int g = Serial.read();
        int b = Serial.read();
        strip.setPixelColor(i, strip.Color(r, g, b));
      }
      strip.show();
    }
  }
}
