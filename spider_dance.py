import time
import Adafruit_PCA9685

# Inizializzazione del modulo PCA9685
try:
    pwm = Adafruit_PCA9685.PCA9685()
    pwm.set_pwm_freq(50)
except Exception as e:
    print("Errore durante l'inizializzazione del PCA9685:", e)
    exit(1)

# Mappatura dei servi
servos = {
    'FLB': 0, 'FLM': 1, 'FLE': 2,
    'FRB': 6, 'FRM': 7, 'FRE': 8,
    'HLB': 3, 'HLM': 4, 'HLE': 5,
    'HRB': 9, 'HRM': 10, 'HRE': 11,
    'P': 12, 'T': 13
}

# Valori iniziali e limiti dei PWM
init_pwm = {
    'FLB': 313, 'FLM': 305, 'FLE': 313,
    'FRB': 325, 'FRM': 281, 'FRE': 301,
    'HLB': 312, 'HLM': 287, 'HLE': 260,
    'HRB': 305, 'HRM': 195, 'HRE': 340,
    'P': 300, 'T': 300
}

min_pwm = 100
max_pwm = 500

def set_servo_position(port, position):
    """Imposta il servo su una posizione specifica."""
    pwm.set_pwm(port, 0, position)

def spider_dance():
    """Esegue una coreografia complessa per il ragno."""
    print("Inizio la coreografia del ballo...")

    while True:
        # Movimento 1: Alzata delle zampe anteriori
        set_servo_position(servos['FLM'], max_pwm)
        set_servo_position(servos['FRM'], max_pwm)
        time.sleep(0.5)

        # Movimento 2: Inclinazione a sinistra
        set_servo_position(servos['FLB'], min_pwm)
        set_servo_position(servos['HLB'], min_pwm)
        time.sleep(0.5)

        # Movimento 3: Inclinazione a destra
        set_servo_position(servos['FRB'], min_pwm)
        set_servo_position(servos['HRB'], min_pwm)
        time.sleep(0.5)

        # Movimento 4: Zampe posteriori in aria
        set_servo_position(servos['HLM'], max_pwm)
        set_servo_position(servos['HRM'], max_pwm)
        time.sleep(0.5)

        # Movimento 5: Sollevamento e rotazione
        set_servo_position(servos['FLM'], init_pwm['FLM'] - 50)
        set_servo_position(servos['FRM'], init_pwm['FRM'] + 50)
        set_servo_position(servos['HLM'], init_pwm['HLM'] - 50)
        set_servo_position(servos['HRM'], init_pwm['HRM'] + 50)
        time.sleep(0.5)

        # Movimento 6: Oscillazione in avanti e indietro
        for _ in range(3):
            set_servo_position(servos['FLB'], max_pwm)
            set_servo_position(servos['FRB'], max_pwm)
            time.sleep(0.3)
            set_servo_position(servos['FLB'], min_pwm)
            set_servo_position(servos['FRB'], min_pwm)
            time.sleep(0.3)

        # Movimento 7: Salti alternati
        set_servo_position(servos['FLM'], max_pwm)
        set_servo_position(servos['HRM'], max_pwm)
        time.sleep(0.5)
        set_servo_position(servos['FLM'], init_pwm['FLM'])
        set_servo_position(servos['HRM'], init_pwm['HRM'])
        set_servo_position(servos['FRM'], max_pwm)
        set_servo_position(servos['HLM'], max_pwm)
        time.sleep(0.5)
        set_servo_position(servos['FRM'], init_pwm['FRM'])
        set_servo_position(servos['HLM'], init_pwm['HLM'])

        # Movimento 8: Reset alle posizioni iniziali
        for servo, port in servos.items():
            set_servo_position(port, init_pwm.get(servo, 300))
        time.sleep(1)

        print("Ripetizione della coreografia...")

if __name__ == "__main__":
    try:
        spider_dance()
    except KeyboardInterrupt:
        print("Coreografia interrotta dall'utente.")
        for servo, port in servos.items():
            set_servo_position(port, init_pwm.get(servo, 300))
        print("Posizioni ripristinate.")
