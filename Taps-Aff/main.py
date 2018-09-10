### Author: hibby <d@vehibberd.com>
### Description: Scottish Consulate Weather Report
### Category: Other
### License: BSD 3

import http_client
import json
import ugfx
import wifi
import dialogs
import pyb

ugfx.init()
ugfx.clear()
ugfx.set_default_font(ugfx.FONT_NAME)

# fuck me it's hoat, get aht tap aff loun!
def screen_taps_aff():
        ugfx.clear(ugfx.html_color(0xffffff))
        ugfx.text(5, 5, "TAPS AFF", ugfx.RED)
# if it's caul, get yer tap oan laddie
def screen_taps_oan():
        ugfx.clear(ugfx.html_color(0xffffff))
        ugfx.text(5, 5, "TAPS OAN", ugfx.BLUE)

def screen_wifi_connect():
        ugfx.clear(ugfx.html_color(0xffffff))
        ugfx.text(5, 5, "Connecting", ugfx.RED)

def screen_wifi_fail():
        ugfx.clear(ugfx.html_color(0xffffff))
        ugfx.text(5, 5, "No Wifi", ugfx.RED)

screen_wifi_connect()
wifi.connect()

try:
    if wifi.nic().is_connected():
            weatherdata =
            http_client.get('http://api.openweathermap.org/data/2.5/weather?q=ledbury&appid=cf393818afa8569d6abe90ec921b64b2').raise_for_status().json()['main']['temp']
            realtemp = weatherdata-273.15
            print(realtemp)
        
except OSError as e:
    print("Query failed " + str(e))

while True:
 
        if realtemp >= 19:
                screen_taps_aff()
        else:
                screen_taps_oan()

        pyb.delay(10000)
