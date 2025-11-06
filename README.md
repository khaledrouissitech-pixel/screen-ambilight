# 💡 Screen Ambilight (Python + Arduino)
A simple Ambilight-style system for laptops and monitors.  
The Python script captures the screen, divides it into edge regions, calculates the dominant colors, and sends them to an Arduino driving a WS2812B LED strip.

Even without hardware, the project can run in "simulation mode" and prints the LED colors directly in the terminal.

---

## ✅ Features
- Live screen capture and color extraction
- Configurable LED layout (top, bottom, left, right)
- Works with any screen size
- Arduino receiver code included
- Can run without LEDs (debug mode)

---

## 🖥 Hardware Requirements
- Arduino (Uno, Nano, or similar)
- WS2812B or NeoPixel LED strip  
- USB cable to PC
- Power supply for LEDs 

> For demonstration, this project was tested **without** a real LED strip.  
> The Python script prints LED data to confirm it works even without hardware.

---

## 📌 Screen Size Used in Example
Laptop screen: **35 cm x 23.5 cm**

The LED strip would normally go around the edges like this:

- Top: 20 LEDs  
- Bottom: 20 LEDs  
- Left: 10 LEDs  
- Right: 10 LEDs  
- Total LEDs in example: **60**

The exact number depends on the LED density (30 LEDs/meter, 60 LEDs/meter, etc.)

---

## 🧮 How LED Positions Are Calculated
The screen is divided into segments matching the number of LEDs on each edge.

Example for the top strip (`TOP_LEDS = 20`):
```python
x1 = int((i / TOP_LEDS) * width)
x2 = int(((i + 1) / TOP_LEDS) * width)
region = screen.crop((x1, 0, x2, EDGE_THICKNESS))
