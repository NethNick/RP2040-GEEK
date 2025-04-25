# RP2040-GEEK: HID Payload Injector (aka BADusb)

A small project for the Waveshare RP2040-GEEK board (with CircuitBoard firmware). It reads the first line of `pay.txt` file from the USB drive and simulates HID keyboard input. Great for quick automation, testing, or proof-of-concept demos.

## ⚙️ Hardware requirements

- Board: [Waveshare RP2040-GEEK](https://www.waveshare.com/rp2040-geek.htm)
- microSD card with SPI adapter
- Built-in display
- USB HID keyboard interface (virtual)

## 🐍 Installing CircuitPython

1. Go to [circuitpython.org](https://circuitpython.org/board/waveshare_rp2040_geek/)
2. Download the `.uf2` firmware (I've chosen ver. 9.x)
3. Connect the board while holding the **BOOTSEL** button
4. Drag and drop the `.uf2` file onto the new USB drive
5. After reboot, a `CIRCUITPY` drive will appear

## 📁 File Structure

With CircuitPython installed, you'll need in /lib some libraries (PLEASE: same version as CircuitPython, so 9.x):
- `adafruit_bitmap_font` from [libraries](https://circuitpython.org/libraries)
- `adafruit_display_text` (as above)
- `adafruit_hid` (as above)
- `adafruit_st7789.mpy` from [Adafruit_CircuitPython_ST7789](https://github.com/adafruit/Adafruit_CircuitPython_ST7789/releases)
- [Helvetica-Bold-16.bdf](https://github.com/dstieglitz/circuitpy-compass/blob/main/Helvetica-Bold-16.bdf)
- `keyboard_layout_win_it.mpy` from [Neradoc/Keyboard_Layouts](https://github.com/Neradoc/Circuitpython_Keyboard_Layouts/tree/main)
- `keycode_win_it.mpy` (as above)

Then in / of the RP2040 drive put:
- `pay.txt` (payload file only first line will be used)
- `code.py` (actually uses Italian Keyboard Layout)

Note: second payload in pay.txt will search a powershell named mimi.ps1 and executes it (move it to the first line to try), get some powershell scripts and have fun (in case remove the `kbd.press(Keycode.F11)` in line 89 of code.py.

## 🔐 Disclamer and security notice

This project simulates automated keyboard input: **use only on devices you control**. Not intended for malicious use.
