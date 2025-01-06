#!/usr/bin/python3
# File name   : spider_defense_mode.py
# Description : Modalità difesa per il robot ragno

import time
from Adafruit_PCA9685 import PCA9685

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

def move_leg(servo_name, position):
    """Muove un singolo servo a una posizione specifica."""
    if servo_name in servos:
        port = servos[servo_name]
        pwm.set_pwm(port, 0, position)
    else:
        print(f"Servo {servo_name} non trovato.")

def defensive_stance():
    """Posizione di difesa: solleva alcune gambe e abbassa altre."""
    for leg in ['FLB', 'FRB', 'HLB', 'HRB']:
        move_leg(leg, max_pwm)  # Solleva le gambe posteriori
    for leg in ['FLM', 'FRM', 'HLM', 'HRM']:
        move_leg(leg, min_pwm)  # Abbassa le gambe anteriori
    time.sleep(1)

def leg_thrust():
    """Movimento rapido delle gambe come "attacco" difensivo."""
    for _ in range(3):  # Numero di ripetizioni
        for leg in ['FLB', 'FRB', 'HLB', 'HRB']:
            move_leg(leg, min_pwm)  # Spingi in basso
        time.sleep(0.2)
        for leg in ['FLB', 'FRB', 'HLB', 'HRB']:
            move_leg(leg, max_pwm)  # Solleva rapidamente
        time.sleep(0.2)

def reset_posture():
    """Riporta tutti i servi alla posizione iniziale."""
    for servo_name, position in init_pwm.items():
        move_leg(servo_name, position)
    print("Postura resettata.")

def defense_mode():
    """Esegue la modalità difesa."""
    print("Inizio modalità difesa...")
    try:
        while True:
            defensive_stance()  # Assume posizione di difesa
            leg_thrust()  # Effettua movimenti di "attacco"
    except KeyboardInterrupt:
        print("Modalità difesa interrotta dall'utente.")
        reset_posture()

if __name__ == "__main__":
    defense_mode()
