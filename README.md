# Resistance Colour Code Calculator

A simple Python GUI tool that calculates resistor values based on colour bands. Designed with Tkinter and PIL, this allows users to select band colours and get real-time resistance values.

---

 ## Features

- Supports **4-band and 5-band** resistor calculations
- Dropdown interface to select colour bands
- Displays **tolerance**, **multiplier**, and calculated **resistance**
- Dynamic screen transitions with themed backgrounds
- Easy-to-use interface built in Tkinter
- Error handling for incomplete selections

---

##  How It Works

1. User is greeted with a welcome screen.
2. On clicking **“Let’s Go!”**, the user selects the number of bands present in the resistor before them.
3. Based on the selection, the app shows dropdown menus to select band colours.
4. The user then selects the colour of each band.
5. The resistor value is calculated and displayed using backend logic.

---

##  Getting Started

###  Requirements

- Python 3.7+
- `tkinter` (comes with standard Python)
- `Pillow` (`pip install pillow`)

### ▶️ To Run the App:

```bash
python resistance_calculator_gui.py