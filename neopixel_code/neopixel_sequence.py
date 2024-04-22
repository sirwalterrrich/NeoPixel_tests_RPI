import time
from rpi_ws281x import PixelStrip, Color

# LED strip configuration:
LED_COUNT = 8
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 255
LED_INVERT = False
LED_CHANNEL = 0

# Create PixelStrip object with appropriate configuration.
strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()

def pulseColor(strip, color, pulse_count=3, step=5, wait_ms=20, color_name=""):
    """Pulse a color by gradually changing the brightness."""
    print(f"Starting {color_name} pulsing...")
    for _ in range(pulse_count):
        # Fade in
        for brightness in range(0, 256, step):
            for i in range(strip.numPixels()):
                r = (color >> 16) & 255
                g = (color >> 8) & 255
                b = color & 255
                strip.setPixelColor(i, Color(r*brightness//255, g*brightness//255, b*brightness//255))
            strip.show()
            time.sleep(wait_ms/1000.0)
        # Fade out
        for brightness in range(255, -1, -step):
            for i in range(strip.numPixels()):
                r = (color >> 16) & 255
                g = (color >> 8) & 255
                b = color & 255
                strip.setPixelColor(i, Color(r*brightness//255, g*brightness//255, b*brightness//255))
            strip.show()
            time.sleep(wait_ms/1000.0)
    print(f"Completed {color_name} pulsing.")

def flashColor(strip, color, flash_count=2, wait_ms=50, color_name=""):
    """Flash a color for a specific number of times."""
    print(f"Starting {color_name} flashing...")
    for _ in range(flash_count):
        # Turn on
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)
        # Turn off
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(0, 0, 0))
        strip.show()
        time.sleep(wait_ms/1000.0)
    print(f"Completed {color_name} flashing.")

def steadyColor(strip, color, color_name=""):
    """Set the strip to a steady color."""
    print(f"Setting steady {color_name} color...")
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
    strip.show()

print('Animation Sequence Starting...')
try:
    pulseColor(strip, Color(255, 255, 255), pulse_count=3, step=10, wait_ms=10, color_name="white")  # Throbbing White
    flashColor(strip, Color(255, 0, 0), flash_count=2, wait_ms=100, color_name="red")                 # Red Flash
    pulseColor(strip, Color(255, 255, 0), pulse_count=2, step=10, wait_ms=10, color_name="yellow")    # Yellow Pulse
    flashColor(strip, Color(0, 255, 0), flash_count=3, wait_ms=100, color_name="green")               # Green Flash
    steadyColor(strip, Color(0, 255, 0), color_name="green")                                          # Steady Green
    print("Sequence complete. Now displaying steady green.")

except KeyboardInterrupt:
    # On Ctrl+C, turn off all the LEDs.
    steadyColor(strip, Color(0, 0, 0), color_name="off")
    print('Animation Sequence Ended. LEDs turned off.')
