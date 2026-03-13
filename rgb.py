from openrgb import OpenRGBClient
from openrgb.utils import RGBColor

client = OpenRGBClient()
devices = client.devices

for device in devices:
    print(f"Turning on: {device.name}")
    for led in device.leds:
        led.set_color(RGBColor(255, 255, 255))  # White
