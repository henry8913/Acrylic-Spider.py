#!/usr/bin/python3
# File name   : spider_stealth_mode.py
# Description : Modalità stealth per il robot ragno

import time
from rpi_ws281x import *
import Adafruit_PCA9685

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

    def dim_lights(self, brightness):
        for i in range(self.strip.numPixels()):
            color = Color(int(255 * brightness), int(255 * brightness), int(255 * brightness))
            self.strip.setPixelColor(i, color)
        self.strip.show()

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

min_pwm = 250  # Movimenti ridotti per modalità stealth
max_pwm = 350


def move_servo_incrementally(port, start_pos, end_pos, steps, delay):
    """Muove un servo incrementando la posizione gradualmente."""
    for step in range(steps + 1):
        position = start_pos + (end_pos - start_pos) * step // steps
        pwm.set_pwm(port, 0, position)
        time.sleep(delay)

def stealth_walk():
    """Muove le gambe con movimenti lenti e silenziosi usando incrementi."""
    steps = 20  # Numero di incrementi per movimento
    delay = 0.05  # Ritardo tra ogni incremento

    for servo_name, port in servos.items():
        start_pos = init_pwm.get(servo_name, 300)
        end_pos = max_pwm if start_pos < max_pwm else min_pwm

        # Muove il servo incrementando
        print(f"Movimento stealth: {servo_name} -> Da {start_pos} a {end_pos}")
        move_servo_incrementally(port, start_pos, end_pos, steps, delay)

        # Riporta il servo alla posizione iniziale
        move_servo_incrementally(port, end_pos, start_pos, steps, delay)

def stealth_mode(led1, led2):
    """Esegue la modalità stealth."""
    print("Inizio modalità stealth...")
    led1.dim_lights(0.1)  # Luci basse
    led2.dim_lights(0.1)

    try:
        while True:
            stealth_walk()
    except KeyboardInterrupt:
        print("Modalità stealth interrotta dall'utente.")
        # Ripristina i LED e i servi
        led1.set_color(0, 0, 0)
        led2.set_color(0, 0, 0)
        for servo_name, port in servos.items():
            pwm.set_pwm(port, 0, init_pwm.get(servo_name, 300))

if __name__ == '__main__':
    # Configura LED
    led1 = LEDStrip(16, 12)  # Prima striscia: 16 LED, GPIO 12
    led2 = LEDStrip(16, 18)  # Seconda striscia: 16 LED, GPIO 18

    # Avvia modalità stealth
    stealth_mode(led1, led2)
