import time
from rpi_ws281x import PixelStrip, Color

# LED strip configuration:
LED_COUNT = 8        # Number of LED pixels.
LED_PIN = 18         # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10         # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255 # Set to 0 for darkest and 255 for brightest
LED_INVERT = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0      # set to '1' for GPIOs 13, 19, 41, 45 or 53

# Create PixelStrip object with appropriate configuration.
strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()

def throbbingWhite(strip, pulse_count=3, step=5, wait_ms=20):
    """Throbs in white color by gradually changing the brightness."""
    print("Starting white throbbing...")
    for _ in range(pulse_count):
        # Fade in
        for brightness in range(0, 256, step):
            color = Color(brightness, brightness, brightness)  # White
            for i in range(strip.numPixels()):
                strip.setPixelColor(i, color)
            strip.show()
            time.sleep(wait_ms/1000.0)
        # Fade out
        for brightness in range(255, -1, -step):
            color = Color(brightness, brightness, brightness)  # White
            for i in range(strip.numPixels()):
                strip.setPixelColor(i, color)
            strip.show()
            time.sleep(wait_ms/1000.0)
    print("Completed white throbbing.")

print('Press Ctrl-C to quit.')
try:
    throbbingWhite(strip, pulse_count=3, step=10, wait_ms=10)  # Throbbing White
    throbbingWhite(strip, pulse_count=3, step=10, wait_ms=10)  # Throbbing White
    throbbingWhite(strip, pulse_count=3, step=10, wait_ms=10)  # Throbbing White
    throbbingWhite(strip, pulse_count=3, step=10, wait_ms=10)  # Throbbing White
except KeyboardInterrupt:
    # On Ctrl+C, turn off all the LEDs.
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(0, 0, 0))
    strip.show()
    strip.show()
    print('LEDs turned off.')
