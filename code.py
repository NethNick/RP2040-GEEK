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
#    with open("/sd/logger.txt", "r") as f:
#        string = f.readline()
#        f.close()
    with open("/pay.txt", "r") as p:
       pay = p.readline().replace("\r","")
       p.close()
    storage.umount("/sd")

except OSError as exc:
    error = exc.errno
    if error == "no SD-Card":
        print(error)
    if error == 2:
        print("File: logger.txt missing!")


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
        
#with open("/sd/logger.txt", "w") as f:
#    f.write("x")
#    f.close()
#

# Display initialize
#lcd_cs=board.GP9
#lcd_dc=board.GP8
#lcd_reset=board.GP12
# Release any resources currently in use for the displays
#displayio.release_displays()

#display_bus = FourWire(spi, command=lcd_dc, chip_select=lcd_cs, reset=lcd_reset)
#display = ST7789(display_bus, rotation=270, width=240, height=135, rowstart=40, colstart=53)

# Make the display context
#splash = displayio.Group()
#display.root_group = splash

# Make a background color fill
#color_palette = displayio.Palette(1)
#color_palette[0] = 0x0000ff  # Colore nero per pulire lo schermo
#color_bitmap = displayio.Bitmap(display.width, display.height, 1)
#bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
#splash.append(bg_sprite)

## Draw a label
#text_area = label.Label(font=terminalio.FONT, text="WAIT", color=0xFFFF00, scale=2, line_spacing=1 )
#text_group = displayio.Group(x=15, y=20)
#text_group.append(text_area)  # Subgroup for text scaling
#splash.append(text_group)
