from time import sleep
from machine import Pin
import time

#================= Variables =============

MORSE_EN = {
    'A': '.-',    'B': '-...',   'C': '-.-.', 
    'D': '-..',   'E': '.',      'F': '..-.',
    'G': '--.',   'H': '....',   'I': '..',
    'J': '.---',  'K': '-.-',    'L': '.-..',
    'M': '--',    'N': '-.',     'O': '---',
    'P': '.--.',  'Q': '--.-',   'R': '.-.',
    'S': '...',   'T': '-',      'U': '..-',
    'V': '...-',  'W': '.--',    'X': '-..-',
    'Y': '-.--',  'Z': '--..',
    '0': '-----', '1': '.----',  '2': '..---',
    '3': '...--', '4': '....-',  '5': '.....',
    '6': '-....', '7': '--...',  '8': '---..',
    '9': '----.',' ': ' '
}

MORSE = MORSE_EN
MORSE_REVERSED = {value: key for key, value in MORSE.items()}

DOT_TIME = 200
DASH_TIME_MIN = 200
DASH_TIME_MAX = 1000
SPACE_TIME = 600
END_TIME = 1000

LED_PIN = 18
BTN_PIN = 17

#============= Functions ==============

def dot():
    led = Pin(LED_PIN, Pin.OUT)
    led.value(1)
    sleep(0.2)
    led.value(0)
    sleep(0.2)


def dash():
    led = Pin(LED_PIN, Pin.OUT)
    led.value(1)
    sleep(0.6)
    led.value(0)
    sleep(0.2)


def verify_morse_code(morse_code):
    output = True
    for i in morse_code.split(" "):
        if i not in MORSE_REVERSED:
            output = False
    return output


def start_signals(string_arg):
    for letter in string_arg:
        for symbol in MORSE[letter.upper()]:
            if symbol == '-':
                dash()
            elif symbol == '.':
                dot()
            else:
                sleep(1.4)
        sleep(0.7)
    return None


def get_button_press_time():
    start_time = 0
    end_time = 0
    button = Pin(BTN_PIN, Pin.IN, Pin.PULL_DOWN)
    while True:
        # Check if the button is pressed
        if button.value() == 1:
            start_time = time.ticks_ms()  # Record press time
            while button.value() == 1:  # Wait until button is released
                pass
            end_time = time.ticks_ms()  # Record release time
            break
    return end_time - start_time


def get_button_idle_time():  # Idle time
    button = Pin(BTN_PIN, Pin.IN, Pin.PULL_DOWN)
    start_time = time.ticks_ms()
    while button.value() == 0:  # Wait until button is pressed
        pass
    end_time = time.ticks_ms()
    return end_time - start_time

#============= Functions for Options ==============

def to_morse(string_arg):
    return ''.join(MORSE.get(i.upper())+' ' for i in string_arg)
     


def from_morse(string_arg):
    return ''.join(MORSE_REVERSED.get(i) for i in string_arg.split())


def btn_input_to_morse():
    print("Enter Morse code.")
    print("Hold for one second and press again to confirm.")
    print("")
    morse_code = ""
    symbol = ""
    idle_time = 0
    while True:
        button_press_time = get_button_press_time()
        if button_press_time <= DOT_TIME:  # Milliseconds for "." < 200
            symbol += "."        
        elif DASH_TIME_MIN < button_press_time < DASH_TIME_MAX:  # Milliseconds for "-" > 200 < 1000
            symbol += "-"
        
        idle_time = get_button_idle_time()
        if idle_time > SPACE_TIME:
            symbol += " "
            morse_code += symbol
            symbol = ""
        
        if button_press_time >= END_TIME:  # Over 1000 milliseconds = "end"
            return morse_code


def morse_code_to_text():
    print()
    while True:
        morse_code = input("Morse code: ")
        if verify_morse_code(morse_code):
            text = from_morse(morse_code)
            print("Text: " + text)
            input()
            break
        else:
            print("Invalid Morse code input:")
            print(MORSE)


def text_to_morse_code():
    print()
    text = input("Text: ")
    morse_code = to_morse(text)
    print("Morse code: " + morse_code)
    start_signals(text)


def morse_code_from_button():
    morse_code = btn_input_to_morse()
    text = from_morse(morse_code)
    print()
    print("Message: {} ( {})".format(text, morse_code))
    print("1) Execute message.")
    print("2) New message.")
    option = input("Choose '1' or '2': ")
    if option == "1":
        start_signals(text)        
    elif option == "2":
        pass
    else:  # Against tricksters
        for_tricksters(option)


def for_tricksters(option):
    print("Hey trickster. I said choose a numeric option, not {}.".format(option))
    print("Try again.")
    input()


#================ Main ============

option = None 
while True:
    print("1) Morse code to text. Example: ... --- ... => SOS")
    print("2) Text to Morse code. Example: SOS => ... --- ... (Sound and light signal.)")
    print("3) Morse code via button. Example: ... --- ... => SOS (Sound and light signal.)")
    
    option = input("Choose '1', '2' or '3': ") 
    if option == "1":  # Morse code to text
        morse_code_to_text()
    elif option == "2":  # Text to Morse code
        text_to_morse_code()
    elif option == "3":
        morse_code_from_button()
    else:  # Against tricksters
        for_tricksters(option)
