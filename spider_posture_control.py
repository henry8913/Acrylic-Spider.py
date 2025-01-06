#!/usr/bin/python3
# File name   : spider_posture_control.py
# Description : Controllo della postura per il robot ragno

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


def set_servo_position(servo_name, position):
    """Imposta la posizione di un servo."""
    if servo_name in servos:
        port = servos[servo_name]
        pwm.set_pwm(port, 0, position)
    else:
        print(f"Servo {servo_name} non trovato.")


def adjust_posture(pitch, roll, height):
    """Regola la postura del robot in base a pitch (inclinazione), roll (rotazione) e altezza."""
    # Altezza base e correzioni per pitch e roll
    base_height = 300
    pitch_correction = pitch * 10
    roll_correction = roll * 10

    # Aggiorna posizioni dei servi
    for leg, offset in zip(['FLM', 'FRM', 'HLM', 'HRM'], [1, -1, -1, 1]):
        corrected_height = base_height + (offset * pitch_correction)
        set_servo_position(leg, int(corrected_height + height))

    for leg, offset in zip(['FLB', 'FRB', 'HLB', 'HRB'], [1, -1, -1, 1]):
        corrected_height = base_height + (offset * roll_correction)
        set_servo_position(leg, int(corrected_height + height))

    print(f"Postura aggiornata: Pitch={pitch}, Roll={roll}, Altezza={height}")


def reset_posture():
    """Riporta il robot alla postura iniziale."""
    for servo_name, position in init_pwm.items():
        set_servo_position(servo_name, position)
    print("Postura resettata.")


if __name__ == "__main__":
    try:
        print("Inizio controllo della postura...")
        while True:
            # Esempio: Simula la regolazione della postura
            adjust_posture(pitch=5, roll=-3, height=-20)
            time.sleep(2)

            adjust_posture(pitch=-5, roll=3, height=20)
            time.sleep(2)

            reset_posture()
            time.sleep(2)

    except KeyboardInterrupt:
        print("Controllo interrotto dall'utente.")
        reset_posture()
