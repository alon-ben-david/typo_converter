import subprocess
from pynput import keyboard

def on_press(key):
    try:

            if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
            # Store that Ctrl key is pressed
                on_press.ctrl_pressed = True
            elif on_press.ctrl_pressed and key.char == '1':
            # Check if Ctrl + 1 is pressed
                english_to_hebrew()
            elif on_press.ctrl_pressed and key.char == '2':
                # Check if Ctrl + 2 is pressed
                hebrew_to_english()
    except AttributeError:
        print('special key {0} pressed'.format(key))

def on_release(key):

    if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
        # Reset the Ctrl key pressed flag
        on_press.ctrl_pressed = False
    if key == keyboard.Key.esc:
        # Stop listener
        return False
def process_selected_text_english_to_hebrew():
    english_to_hebrew = {
        'a': 'ש',
        'b': 'נ',
        'c': 'ב',
        'd': 'ג',
        'e': 'ק',
        'f': 'כ',
        'g': 'ע',
        'h': 'י',
        'i': 'ן',
        'j': 'ח',
        'k': 'ל',
        'l': 'ך',
        'm': 'צ',
        'n': 'מ',
        'o': 'ם',
        'p': 'פ',
        'q': '/',
        'r': 'ר',
        's': 'ד',
        't': 'א',
        'u': 'ו',
        'v': 'ה',
        'w': 'ס',
        'x': 'ס',
        'y': 'ט',
        'z': 'ז',
        'A': 'ש',
        'B': 'נ',
        'C': 'ב',
        'D': 'ג',
        'E': 'ק',
        'F': 'כ',
        'G': 'ע',
        'H': 'י',
        'I': 'ן',
        'J': 'ח',
        'K': 'ל',
        'L': 'ך',
        'M': 'צ',
        'N': 'מ',
        'O': 'ם',
        'P': 'פ',
        'Q': '/',
        'R': 'ר',
        'S': 'ד',
        'T': 'א',
        'U': 'ו',
        'V': 'ה',
        'W': 'ס',
        'X': 'ס',
        'Y': 'ט',
        ',': 'ת',
        ';': 'ף',
        '.': 'ץ',
        'Z': 'ז'
    }

    selected_text = subprocess.run(["pbpaste"], capture_output=True, text=True).stdout.strip()

    processed_text = ''
    for letter in selected_text:
        if letter in english_to_hebrew:
            processed_text += english_to_hebrew[letter]
        else:
            processed_text += letter

    return processed_text
def process_selected_text_hebrew_to_english():
    hebrew_to_english = {
        'ש': 'a',
        'נ': 'b',
        'ב': 'c',
        'ג': 'd',
        'ק': 'e',
        'כ': 'f',
        'ע': 'g',
        'י': 'h',
        'ן': 'i',
        'ח': 'j',
        'ל': 'k',
        'ך': 'l',
        'צ': 'm',
        'מ': 'n',
        'ם': 'o',
        'פ': 'p',
        '/': 'q',
        'ר': 'r',
        'ד': 's',
        'א': 't',
        'ו': 'u',
        'ה': 'v',
        'ס': 'w',
        'ז': 'z',
        'ט': 'y',
        'ת': ',',
        'ף': ';',
        'ץ': '.'
    }

    selected_text = subprocess.run(["pbpaste"], capture_output=True, text=True).stdout.strip()

    processed_text = ''
    for letter in selected_text:
        if letter in hebrew_to_english:
            processed_text += hebrew_to_english[letter]
        else:
            processed_text += letter

    return processed_text

def english_to_hebrew():
    processed_text = process_selected_text_english_to_hebrew()
    subprocess.run(["pbcopy"], input=processed_text, text=True)
    print("Processed text copied to clipboard.")

def hebrew_to_english():
    processed_text = process_selected_text_hebrew_to_english()
    subprocess.run(["pbcopy"], input=processed_text, text=True)
    print("Processed text copied to clipboard.")

if __name__ == "__main__":
    print("Instruction:")
    print("To convert text from Hebrew to English, copy the requested text and click on Ctrl + 2, then paste it back.")
    print("To convert text from English to Hebrew, copy the requested text and click on Ctrl + 1, then paste it back.")
    print("To close the program, press esc.")
    # Initialize the Ctrl key pressed flag

    on_press.ctrl_pressed = False

    # Collect events until released
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()