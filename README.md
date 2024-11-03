# Morse Code Project with Raspberry Pi Pico



This project enables sending and receiving Morse code signals using the Raspberry Pi Pico. The board interprets button presses as Morse code, converts text to Morse signals, and controls an LED to display the Morse code through light signals.

## Requirements

- **Raspberry Pi Pico** board
- **LED** for visual representation of Morse code
- **Button** for inputting Morse code
- **Connecting wires** for the components

## Features

- **Text to Morse Code Conversion**: Converts any alphanumeric message into Morse code, displayed via light signals on the LED.
- **Morse Code to Text Conversion**: Decodes Morse code entered via button presses.
- **Interactive Mode**: Choose between translating Morse code to text, translating text to Morse code (with light signals), or inputting Morse code via button.

## Setup and Connections

<a href="https://ibb.co/JFRVdfZ"><img src="https://i.ibb.co/7NJPzwh/morse-pin-map.png" alt="morse-pin-map" border="0" /></a>

1. **Connect the LED**: Connect the anode (long leg) of the LED to GPIO pin 18 and the cathode to GND.
2. **Connect the Button**: Connect one end to GPIO pin 17 and the other end to GND with a pull-down resistor.

## Code Structure

- **MORSE_EN and MORSE_BG** dictionaries contain Morse code correspondences for the English and Bulgarian alphabets.
- **DOT_TIME, DASH_TIME_MIN, DASH_TIME_MAX** define the timing parameters for Morse symbols.
- **Functions**:
    - `dot()`: Activates the LED for the duration of a dot.
    - `dash()`: Activates the LED for the duration of a dash.
    - `start_signals(string_arg)`: Converts text to Morse code and displays it through LED signals.
    - `get_button_press_time()` and `get_button_idle_time()`: Record the button press time and idle time for interpreting Morse code.
    - `morse_code_to_text()` and `text_to_morse_code()`: Core options for converting Morse code to text and vice versa.

## Running the Code

1. **Upload the code** to the Pico using a MicroPython environment.
2. **Select an option**:
   - **1**: Convert Morse code to text.
   <br>
   <a href="https://ibb.co/bggJJY6"><img src="https://i.ibb.co/cccLLRy/morse-to-text.png" alt="morse-to-text" border="0" /></a>

    <br>

   
   - **2**: Convert text to Morse code and display it via LED.
   <br>
   
   <a href="https://ibb.co/cCDhgcK"><img src="https://i.ibb.co/vQZ4wxC/text-to-morse.png" alt="text-to-morse" border="0" /></a>

   <br>
   
   - **3**: Input Morse code via button and see the corresponding text.
   
   <br>
   <a href="https://ibb.co/f1RMZrC"><img src="https://i.ibb.co/QbB9hY6/morse-via-but.png" alt="morse-via-but" border="0" /></a>
   <br>
   
## Troubleshooting

- **Button and LED are not responding**: Check the pin connections and ensure the Pico board is powered.
- **Incorrect Morse output**: Verify that the button press timing matches the settings of `DOT_TIME` and `DASH_TIME_MAX`.
