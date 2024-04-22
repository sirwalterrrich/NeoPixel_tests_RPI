import time
import random
from rpi_ws281x import PixelStrip, Color

# LED strip configuration:
LED_COUNT = 8       # Number of LED pixels.
LED_PIN = 18         # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 5          # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255 # Set to 0 for darkest and 255 for brightest
LED_INVERT = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0      # set to '1' for GPIOs 13, 19, 41, 45 or 53

# Initialize LED strip
strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()

def displayVUMeter(strip, level):
    """Displays the VU meter level on the LED strip."""
    # Clear all LEDs
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(0, 0, 0))
    
    # Set LEDs up to the current level
    for i in range(level):
        if i < LED_COUNT // 3:
            strip.setPixelColor(i, Color(0, 255, 0))  # Green
        elif i < LED_COUNT * 2 // 3:
            strip.setPixelColor(i, Color(255, 140, 0))  # Orange
        else:
            strip.setPixelColor(i, Color(255, 0, 0))  # Red
    
    strip.show()

print('Simulating VU Meter (press Ctrl-C to quit)...')
try:
    while True:
        # Simulate audio level (you would replace this with actual audio level computation)
        simulatedLevel = random.randint(0, LED_COUNT)
        displayVUMeter(strip, simulatedLevel)
        time.sleep(0.1)
except KeyboardInterrupt:
    # Clear strip on exit
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(0, 0, 0))
    strip.show()
    print('Simulation ended.')
