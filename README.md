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
Each tuple (R, G, B) represents one LED’s color.

✅ Perfect for testing before buying LEDs.

*🔌 2. Running With Arduino + LEDs*

1️⃣ Upload arduino_led.ino to Arduino
2️⃣ In led.py, set the COM port:
 Run:
```python
COM_PORT = "COM5"
 ```

---
3️⃣ Enable serial data:

```python
SEND_SERIAL = True
 ```

---
4️⃣ Connect WS2812B data line to pin defined in code (default D6)

##🧮 How LED Position Calculation Works

Goal:
Each LED must match the average color of a small zone of the screen edge.

So the screen is cut into slices.

✅ Example for top LEDs:
 
```python
x1 = int((i / TOP_LEDS) * width)
x2 = int(((i + 1) / TOP_LEDS) * width)
region = screen.crop((x1, 0, x2, EDGE_THICKNESS)
 ```

---
*Explanation:*
| Variable |Description |
|----------|---------|
| i  |LED index (0 → last LED)) |
| width | Full screen width |
| EDGE_THICKNESS| Number of pixels to capture from the top edge|
| (x1, 0, x2, EDGE_THICKNESS)| Rectangular slice for that LED |

 >LED 0 = first slice,
 >LED 1 = next slice,
 >Continues across entire edge.

Same logic repeats for:


- Bottom  
- Left
- Right 

Finally, all LED colors are stored in a list and sent to Arduino.

##🧩 Arduino Code

arduino_led.ino:

Listens to serial

Each LED receives 3 bytes: R G B

Writes colors to WS2812B strip using Adafruit NeoPixel

#📜 License

MIT — free to modify and improve.
