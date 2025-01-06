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

def test_servo(port, init_value):
    """Testa il movimento di un servo."""
    try:
        print(f"Testing servo on port {port}...")
        # Porta il servo al minimo
        pwm.set_pwm(port, 0, min_pwm)
        time.sleep(1)
        
        # Porta il servo al massimo
        pwm.set_pwm(port, 0, max_pwm)
        time.sleep(1)
        
        # Riporta il servo al valore iniziale
        pwm.set_pwm(port, 0, init_value)
        time.sleep(1)
        
        print(f"Servo {port} test completed successfully.")
    except Exception as e:
        print(f"Errore durante il test del servo {port}: {e}")

if __name__ == "__main__":
    print("Inizio test di tutti i servi...")
    for servo_name, port in servos.items():
        init_value = init_pwm.get(servo_name, 300)
        test_servo(port, init_value)
    print("Test completati.")
