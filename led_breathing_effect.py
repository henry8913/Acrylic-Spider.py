#!/usr/bin/python3
# File name   : LED_breathing_effect.py
# Description : Simula il respiro del ragno con l'effetto di luce WS2812

import time
from rpi_ws281x import *

class LEDStrip:
    def __init__(self, led_count, led_pin, led_freq_hz=800000, led_dma=10, led_brightness=255, led_invert=False, led_channel=0):
        """Configura una striscia LED WS2812."""
        self.strip = Adafruit_NeoPixel(led_count, led_pin, led_freq_hz, led_dma, led_invert, led_brightness, led_channel)
        self.strip.begin()

    def set_color(self, R, G, B, brightness=1.0):
        """Imposta il colore per tutti i LED con una specifica luminosità."""
        color = Color(int(R * brightness), int(G * brightness), int(B * brightness))
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, color)
        self.strip.show()

    def breathing_effect(self, R, G, B, inspiratory_time, expiratory_time, pause_time):
        """Crea un effetto di respiro con durata specificata."""
        steps_in = 100  # Numero di passi per l'inspirazione
        steps_out = 100  # Numero di passi per l'espirazione

        delay_in = inspiratory_time / steps_in
        delay_out = expiratory_time / steps_out

        # Inspirazione (fade in)
        for i in range(steps_in):
            brightness = i / steps_in
            self.set_color(R, G, B, brightness)
            time.sleep(delay_in)

        # Espirazione (fade out)
        for i in range(steps_out, 0, -1):
            brightness = i / steps_out
            self.set_color(R, G, B, brightness)
            time.sleep(delay_out)

        # Pausa
        self.set_color(0, 0, 0, 0)  # Spegni i LED durante la pausa
        time.sleep(pause_time)

if __name__ == '__main__':
    # Configurazione delle strisce LED
    led1 = LEDStrip(16, 12)  # Prima striscia: 16 LED, GPIO 12
    led2 = LEDStrip(16, 18)  # Seconda striscia: 16 LED, GPIO 18

    try:
        while True:
            # Effetto respiro naturale per entrambe le strisce
            print("Effetto respiro: Rosso")
            led1.breathing_effect(255, 0, 0, 1.5, 3.0, 0.5)  # Inspirazione 1.5s, espirazione 3.0s, pausa 0.5s
            led2.breathing_effect(255, 0, 0, 1.5, 3.0, 0.5)

            print("Effetto respiro: Verde")
            led1.breathing_effect(0, 255, 0, 1.5, 3.0, 0.5)
            led2.breathing_effect(0, 255, 0, 1.5, 3.0, 0.5)

            print("Effetto respiro: Blu")
            led1.breathing_effect(0, 0, 255, 1.5, 3.0, 0.5)
            led2.breathing_effect(0, 0, 255, 1.5, 3.0, 0.5)

    except KeyboardInterrupt:
        # Spegni i LED in caso di interruzione manuale
        print("Interruzione manuale. Spegnimento dei LED...")
        led1.set_color(0, 0, 0, 0)
        led2.set_color(0, 0, 0, 0)
