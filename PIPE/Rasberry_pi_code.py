import RPi.GPIO as GPIO
import time
import random
import threading


led_pins = {'white1': 4, 'white2': 17, 'blue1': 27, 'blue2': 5,
            'red1': 13, 'red2': 22, 'green1': 6, 'green2': 19,
            'yellow1': 26, 'yellow2': 16, 'green_indicator': 12,
            'yellow_indicator': 25, 'red_indicator': 24}
button_pin = 23
buzzer_pin = 21
start_button_pin = 18


GPIO.setmode(GPIO.BCM)


for pin in led_pins.values():
    GPIO.setup(pin, GPIO.OUT)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buzzer_pin, GPIO.OUT)
GPIO.setup(start_button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

morse_code = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
              'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
              }


def generate_pronounceable_sequence(length=5):
    vowels = 'AEIOU'
    consonants = 'BCDFGHJKLMNPQRSTVWXYZ'
    sequence = ''
    for i in range(length):
        sequence += random.choice(consonants) if i % 2 == 0 else random.choice(vowels)
    return sequence


def flash_morse(code, led_pin):
    for symbol in code:
        GPIO.output(led_pin, GPIO.HIGH)
        time.sleep(0.2 if symbol == '.' else 0.5)
        GPIO.output(led_pin, GPIO.LOW)
        time.sleep(0.2)
    time.sleep(0.6)


def play_buzzer(duration):
    GPIO.output(buzzer_pin, GPIO.HIGH)
    time.sleep(duration)
    GPIO.output(buzzer_pin, GPIO.LOW)


def count_button_presses(timeout=5):
    count = 0
    start_time = time.time()
    while time.time() - start_time < timeout:
        if GPIO.input(button_pin) == GPIO.LOW:
            count += 1
            time.sleep(0.3)
    return count


def validate_guess(expected_presses):
    presses = count_button_presses()
    if presses == expected_presses:
        GPIO.output(led_pins['green_indicator'], GPIO.HIGH)
        play_buzzer(0.2)
        time.sleep(1)
        GPIO.output(led_pins['green_indicator'], GPIO.LOW)
    else:
        GPIO.output(led_pins['red_indicator'], GPIO.HIGH)
        play_buzzer(0.5)
        time.sleep(1)
        GPIO.output(led_pins['red_indicator'], GPIO.LOW)


def game_round():
    word = generate_pronounceable_sequence()
    for char in word.upper():
        if char in morse_code:
            flash_morse(morse_code[char], led_pins['yellow2'])
            validate_guess(morse_code[char].count('.') + morse_code[char].count('-'))



def blink_indicator():
    while game_running:
        GPIO.output(led_pins['yellow_indicator'], GPIO.HIGH)
        time.sleep(0.3)
        GPIO.output(led_pins['yellow_indicator'], GPIO.LOW)
        time.sleep(0.3)

game_running = False
indicator_thread = None

try:
    while True:
        if GPIO.input(start_button_pin) == GPIO.LOW:
            game_running = True
            start_time = time.time()
            indicator_thread = threading.Thread(target=blink_indicator)
            indicator_thread.start()
            while game_running and time.time() - start_time < 120:
                game_round()
                time.sleep(2)
            game_running = False
            if indicator_thread is not None:
                indicator_thread.join()
            GPIO.output(led_pins['green_indicator'], GPIO.HIGH)
            time.sleep(1)
            GPIO.output(led_pins['green_indicator'], GPIO.LOW)
            play_buzzer(1)

except KeyboardInterrupt:
    game_running = False
    if indicator_thread is not None and indicator_thread.is_alive():
        indicator_thread.join()
    GPIO.cleanup()
