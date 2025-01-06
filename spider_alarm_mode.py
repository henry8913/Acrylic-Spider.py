#!/usr/bin/python3
# File name   : spider_alarm_mode.py
# Description : Modalità di allarme per il robot ragno

import time
from rpi_ws281x import *
import Adafruit_PCA9685
import random

# Configurazione PCA9685
try:
    pwm = Adafruit_PCA9685.PCA9685()
    pwm.set_pwm_freq(50)
except Exception as e:
    print("Errore durante l'inizializzazione del PCA9685:", e)
    exit(1)

# Configurazione LED
class LEDStrip:
    def __init__(self, led_count, led_pin, led_freq_hz=800000, led_dma=10, led_brightness=255, led_invert=False, led_channel=0):
        self.strip = Adafruit_NeoPixel(led_count, led_pin, led_freq_hz, led_dma, led_invert, led_brightness, led_channel)
        self.strip.begin()

    def set_color(self, R, G, B):
        color = Color(R, G, B)
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, color)
        self.strip.show()

    def flashing_effect(self, color1, color2, flash_count, delay):
        for _ in range(flash_count):
            self.set_color(*color1)
            time.sleep(delay)
            self.set_color(*color2)
            time.sleep(delay)

# Configurazione dei servi
servos = {
    'FLB': 0, 'FLM': 1, 'FLE': 2,
    'FRB': 6, 'FRM': 7, 'FRE': 8,
    'HLB': 3, 'HLM': 4, 'HLE': 5,
    'HRB': 9, 'HRM': 10, 'HRE': 11
}

init_pwm = {
    'FLB': 313, 'FLM': 305, 'FLE': 313,
    'FRB': 325, 'FRM': 281, 'FRE': 301,
    'HLB': 312, 'HLM': 287, 'HLE': 260,
    'HRB': 305, 'HRM': 195, 'HRE': 340
}

min_pwm = 200  # Riduzione del range per movimenti più limitati
max_pwm = 400

def random_leg_movement():
    """Genera movimenti casuali delle gambe per simulare un comportamento di allarme."""
    for servo_name, port in servos.items():
        # Scegli una posizione casuale tra minimo e massimo
        position = random.choice([min_pwm, max_pwm])
        print(f"Movimento casuale: {servo_name} -> Posizione: {position}")
        pwm.set_pwm(port, 0, position)
        time.sleep(0.05)

    # Riporta i servi alla posizione iniziale
    for servo_name, port in servos.items():
        pwm.set_pwm(port, 0, init_pwm.get(servo_name, 300))
        time.sleep(0.1)

def alarm_mode(led1, led2):
    """Esegue la modalità allarme con movimenti e luci."""
    print("Inizio modalità allarme...")
    try:
        while True:
            # Effetti lampeggianti con i LED
            led1.flashing_effect((255, 0, 0), (0, 0, 255), 5, 0.1)  # Rosso e blu lampeggiante
            led2.flashing_effect((255, 0, 0), (0, 0, 255), 5, 0.1)

            # Movimenti casuali delle gambe
            random_leg_movement()
    except KeyboardInterrupt:
        print("Modalità allarme interrotta dall'utente.")
        # Spegni i LED e riporta i servi alla posizione iniziale
        led1.set_color(0, 0, 0)
        led2.set_color(0, 0, 0)
        for servo_name, port in servos.items():
            pwm.set_pwm(port, 0, init_pwm.get(servo_name, 300))

if __name__ == '__main__':
    # Configura LED
    led1 = LEDStrip(16, 12)  # Prima striscia: 16 LED, GPIO 12
    led2 = LEDStrip(16, 18)  # Seconda striscia: 16 LED, GPIO 18

    # Avvia modalità allarme
    alarm_mode(led1, led2)
