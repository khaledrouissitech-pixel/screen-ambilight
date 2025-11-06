import serial
import time
import numpy as np
import mss
from PIL import Image

# ----- CONFIG -----
COM_PORT = "COM5"       # change if needed
BAUDRATE = 115200
TOP_LEDS = 21
SIDE_LEDS = 14
FPS = 30
SEND_SERIAL = False       # set False to test without Arduino
# -------------------

TOTAL_LEDS = (TOP_LEDS * 2) + (SIDE_LEDS * 2)


mon = mss.mss().monitors[1]
screen_w = mon["width"]
screen_h = mon["height"]

# region width/height for LEDs
top_region_w = screen_w / TOP_LEDS
side_region_h = screen_h / SIDE_LEDS


def get_dominant_color(img):
    arr = np.asarray(img)
    r = int(np.mean(arr[:, :, 0]))
    g = int(np.mean(arr[:, :, 1]))
    b = int(np.mean(arr[:, :, 2]))
    return r, g, b


def capture_led_colors():
    with mss.mss() as sct:
        colors = []

        # BOTTOM (left→right)
        for i in range(TOP_LEDS):
            x1 = int(i * top_region_w)
            y1 = screen_h - 40
            x2 = int((i+1) * top_region_w)
            y2 = screen_h
            img = sct.grab(
                {"left": x1, "top": y1, "width": x2 - x1, "height": y2 - y1})
            colors.append(get_dominant_color(
                Image.frombytes("RGB", img.size, img.rgb)))

        # RIGHT (bottom→top)
        for i in range(SIDE_LEDS):
            x1 = screen_w - 40
            y1 = int(screen_h - (i+1) * side_region_h)
            x2 = screen_w
            y2 = int(screen_h - i * side_region_h)
            img = sct.grab(
                {"left": x1, "top": y1, "width": 40, "height": y2 - y1})
            colors.append(get_dominant_color(
                Image.frombytes("RGB", img.size, img.rgb)))

        # TOP (right→left)
        for i in range(TOP_LEDS):
            x1 = int(screen_w - (i+1) * top_region_w)
            y1 = 0
            x2 = int(screen_w - i * top_region_w)
            y2 = 40
            img = sct.grab(
                {"left": x1, "top": y1, "width": x2 - x1, "height": y2 - y1})
            colors.append(get_dominant_color(
                Image.frombytes("RGB", img.size, img.rgb)))

        # LEFT (top→bottom)
        for i in range(SIDE_LEDS):
            x1 = 0
            y1 = int(i * side_region_h)
            x2 = 40
            y2 = int((i+1) * side_region_h)
            img = sct.grab(
                {"left": x1, "top": y1, "width": 40, "height": y2 - y1})
            colors.append(get_dominant_color(
                Image.frombytes("RGB", img.size, img.rgb)))

        return colors


def send_serial(colors):
    data = bytearray([255])  
    for r, g, b in colors:
        data.extend([r, g, b])
    ser.write(data)


if SEND_SERIAL:
    ser = serial.Serial(COM_PORT, BAUDRATE, timeout=1)
    time.sleep(2)

while True:
    colors = capture_led_colors()

    if SEND_SERIAL:
        send_serial(colors)
    else:
        print(colors)

    time.sleep(1 / FPS)
