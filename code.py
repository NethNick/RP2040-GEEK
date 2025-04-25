#import os
import time
import board
import busio
import sdcardio
#import digitalio
import storage
from fourwire import FourWire
from adafruit_display_text import label
import terminalio
import displayio
from adafruit_st7789 import ST7789
import math
import usb_hid
from adafruit_hid.keyboard import Keyboard
#from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from keyboard_layout_win_it import KeyboardLayout
from adafruit_hid.keycode import Keycode
import supervisor
from adafruit_bitmap_font import bitmap_font
from adafruit_display_text import label
supervisor.runtime.autoreload = True

print("\n\n\n\n\n\n\n\n\n\n\n")

SD_SCK = board.GP18
SD_MOSI = board.GP19
SD_MISO = board.GP20
cs = board.GP23

spi = busio.SPI(SD_SCK, SD_MOSI, SD_MISO)

try:  
    sdcard = sdcardio.SDCard(spi, cs)
    vfs = storage.VfsFat(sdcard)
    storage.mount(vfs, "/sd")
    error = "SD-Card not mounted"
    with open("/pay.txt", "r") as p:
       pay = p.readline().replace("\r","")
       p.close()
    storage.umount("/sd")

except OSError as exc:
    error = exc.errno
    if error == "no SD-Card":
        print(error)

display = board.DISPLAY

# Set text, font, and color
font = bitmap_font.load_font("/lib/Helvetica-Bold-16.bdf")
color = 0xFF00FF

# Create the tet label
text = "WAIT"
text_area = label.Label(font, text=text, color=color)

# Set the location
text_area.x = 20
text_area.y = 20

# Show it
display.root_group = text_area
        
kbd = Keyboard(usb_hid.devices)
#layout = KeyboardLayoutUS(kbd)        
layout = KeyboardLayout(kbd)             
        
kbd.press(Keycode.GUI, Keycode.R)
time.sleep(0.5)
kbd.release_all()
time.sleep(0.5)

layout.write(pay)
time.sleep(0.5)

kbd.press(Keycode.ENTER)
kbd.release_all()
time.sleep(0.5)

#Since prank calls a web site, we want it full screen
kbd.press(Keycode.F11)
kbd.release_all()

# Set text, font, and color
color = 0xFF00FF

# Create the tet label
text = "OK"
text_area = label.Label(font, text=text, color=color)

# Set the location
text_area.x = 20
text_area.y = 20

# Show it
display.root_group = text_area

print("\n\n\n\n\n\n\n\n\n\n\n")

while True:
    time.sleep(86400)        
