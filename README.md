<h1 align="center">
    <img src="https://readme-typing-svg.herokuapp.com/?font=Iosevka&size=30&color=FF4500&center=true&vCenter=true&width=800&height=60&lines=Il+Robot+Ragno+in+Python+%F0%9F%A4%96&repeat=false" alt="Il Robot Ragno in Python">
</h1>

Acrylic-Spider.py è un progetto open-source che controlla un robot ragno dotato di un corpo fisico in acrilico. Questo robot è equipaggiato con **servomotori**, **sensori**, e un **mini PC Raspberry Pi** che funge da cervello per gestire i movimenti e le modalità operative. Grazie alla sua struttura modulare e al software avanzato, il robot può muoversi, esplorare, e interagire con l'ambiente in modo dinamico. 🚀

---

### Modalità Implementate

#### Modalità Stealth 🕶️
- **Descrizione:**
  Movimenti lenti e silenziosi per simulare un comportamento furtivo.
- **Caratteristiche:**
  - Luci dimmerate per un'operazione discreta.

#### Modalità Difesa 🛡️
- **Descrizione:**
  Posizione intimidatoria con movimenti di "attacco" rapidi delle gambe posteriori.
- **Caratteristiche:**
  - Raffiche di movimenti per spaventare potenziali minacce.

#### Modalità Esplorazione 🔍
- **Descrizione:**
  Movimenti casuali per simulare un comportamento esplorativo.
- **Caratteristiche:**
  - Movimento delle gambe per adattarsi all'ambiente.

#### Controllo della Postura 🤸‍♂️
- **Descrizione:**
  Regola l'inclinazione (pitch), rotazione (roll) e altezza per adattarsi a terreni diversi.
- **Caratteristiche:**
  - Stabilità migliorata grazie a calcoli dinamici.

#### Respiro con i LED 🌈
- **Descrizione:**
  Simula un effetto di respiro naturale utilizzando strisce LED WS2812.
- **Caratteristiche:**
  - Transizioni fluide di luminosità per un effetto realistico.

#### Danza Sincronizzata 🎵
- **Descrizione:**
  Esegue coreografie personalizzate con movimenti e luci.
- **Caratteristiche:**
  - Movimenti sincronizzati con effetti LED.2. **Modalità Difesa 🛡️**
   - Posizione intimidatoria con movimenti di "attacco" rapidi delle gambe posteriori.

## 🛠️ Struttura del Repository

### File Principali
- **`spider_stealth_mode.py`**: Modalità furtiva con movimenti ridotti e luci basse.
- **`spider_defense_mode.py`**: Modalità di difesa con movimenti rapidi delle gambe.
- **`spider_exploration_mode.py`**: Modalità esplorativa con movimenti casuali.
- **`spider_posture_control.py`**: Controllo della postura per pitch, roll e altezza.
- **`led_breathing_effect.py`**: Effetto di respiro naturale utilizzando LED WS2812.
- **`servo_test.py`**: Script per testare il funzionamento dei servi.

### ⚙️ Hardware Richiesto
- **Raspberry Pi** (qualsiasi modello con GPIO supportati).
- **Adafruit PCA9685**: Controller PWM per i servi.
- **Servomotori**: Per i movimenti del robot.
- **Strisce LED WS2812**: Per effetti luminosi.

## 🛠️ Installazione

### Requisiti
- Python 3
- Librerie necessarie:
  ```bash
  pip install adafruit-pca9685 rpi-ws281x
  ```

### Clona il Repository
```bash
git clone https://github.com/henry8913/Acrylic-Spider.py.git
cd Acrylic-Spider.py
```

## 🚀 Uso
Esegui gli script per attivare le modalità:

- **Esempio Modalità Difesa:**
  ```bash
  python3 spider_defense_mode.py
  ```

- **Esempio Modalità Stealth:**
  ```bash
  python3 spider_stealth_mode.py
  ```

## 🤝 Contributi
Contributi, segnalazioni di bug e suggerimenti sono benvenuti! Per contribuire:
1. Fai un fork del repository.
2. Crea un branch per le tue modifiche.
3. Apri una pull request.

## 📜 Licenza
Questo progetto è distribuito sotto la licenza MIT. Vedi il file `LICENSE` per maggiori dettagli.

---

**Henry8913**  
[GitHub Repository](https://github.com/henry8913/Acrylic-Spider.py)
