#!/usr/bin/python3
# File name   : spider_exploration_mode.py
# Description : Modalità esplorazione per il robot ragno

import time
from Adafruit_PCA9685 import PCA9685
import random

# Configurazione PCA9685
try:
    pwm = PCA9685()
    pwm.set_pwm_freq(50)
except Exception as e:
    print("Errore durante l'inizializzazione del PCA9685:", e)
    exit(1)

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

min_pwm = 200
max_pwm = 400

# Movimenti casuali per esplorazione
def move_leg(servo_name, position):
    """Muove un singolo servo a una posizione specifica."""
    if servo_name in servos:
        port = servos[servo_name]
        pwm.set_pwm(port, 0, position)
    else:
        print(f"Servo {servo_name} non trovato.")

def random_walk():
    """Genera movimenti casuali per l'esplorazione."""
    for _ in range(4):  # Numero di passi
        for leg_group in [['FLM', 'FRM'], ['HLM', 'HRM']]:
            for leg in leg_group:
                random_position = random.randint(min_pwm, max_pwm)
                move_leg(leg, random_position)
                time.sleep(0.1)

        time.sleep(0.5)  # Pausa tra i cicli

    # Ripristina alla posizione iniziale
    for servo_name, position in init_pwm.items():
        move_leg(servo_name, position)

def exploration_mode():
    """Esegue la modalità esplorazione."""
    print("Inizio modalità esplorazione...")
    try:
        while True:
            random_walk()
    except KeyboardInterrupt:
        print("Modalità esplorazione interrotta dall'utente.")
        # Ripristina alla posizione iniziale
        for servo_name, position in init_pwm.items():
            move_leg(servo_name, position)

if __name__ == "__main__":
    exploration_mode()
