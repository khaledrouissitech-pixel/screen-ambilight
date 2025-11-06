# 💡 Screen Ambilight System (Python + Arduino)

This project creates an Ambilight-style effect for any monitor or laptop.  
A Python script captures the screen, detects the dominant colors along the edges, and sends them to an Arduino controlling a WS2812B (NeoPixel) LED strip.

Even without a physical LED strip, the project works in **simulation mode**, printing LED color values in the terminal so anyone can test the setup.

---

## ✅ Features
- Real-time screen color capture
- Divides the screen into LED segments
- Calculates average RGB color for each segment
- Sends data to Arduino over Serial
- Can run without LEDs (prints RGB output)

---

## 🖥 Hardware Requirements
| Component | Details |
|----------|---------|
| Arduino board | Uno / Nano / Mega (any with serial) |
| LED Strip | WS2812B / NeoPixel |
| Power | 5V power supply (depending on LED count) |
| USB Cable | Connects PC ↔ Arduino |

> **Note:** This repository was developed and tested **without a real LED strip**.  
> The software is fully functional and ready for hardware connection.

---

## 🧪 Example Screen
Laptop size used for calculations:  
**35 cm × 23.5 cm**

A typical LED layout:
- Top: 20 LEDs  
- Bottom: 20 LEDs  
- Left: 10 LEDs  
- Right: 10 LEDs  
➡ **Total: 60 LEDs**

The layout depends on strip LED density (30/meter, 60/meter, etc.)

---

## 📦 Python Dependencies

| Library | Purpose |
|---------|---------|
| **mss** | Captures the screen efficiently in real-time |
| **Pillow (PIL)** | Image manipulation and cropping |
| **numpy** | Fast averaging of pixel colors |
| **pyserial** | Sends RGB values to Arduino |

Install them with:

```bash
pip install mss pillow numpy pyserial 
 ```

---
Pillow → Used to capture and crop screen images

pyserial → Sends RGB data to Arduino

## ▶️ Running the Python Script
*1. Simulation Mode (No Arduino Needed)*
Inside led.py, set:
```python
SEND_SERIAL = False
 ```

---

Run:
```python
python led.py
 ```

---
Output example:
```css
[(62, 59, 52), (44, 56, 63), (80, 62, 56), ...]

 ```

---
