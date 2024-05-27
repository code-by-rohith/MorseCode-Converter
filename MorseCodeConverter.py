# Dictionary representing the morse code chart
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--', '?': '..--..',
    "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.',
    '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.',
    ' ': '/'
}

# Reverse dictionary for decoding Morse code
REVERSE_MORSE_CODE_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}

def text_to_morse(text):
    """Convert text to Morse code."""
    morse_code = ""
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char] + " "
        else:
            morse_code += '? '
    return morse_code.strip()

def morse_to_text(morse_code):
    """Convert Morse code to text."""
    text = ""
    morse_words = morse_code.split(" / ")
    for morse_word in morse_words:
        morse_chars = morse_word.split()
        for morse_char in morse_chars:
            if morse_char in REVERSE_MORSE_CODE_DICT:
                text += REVERSE_MORSE_CODE_DICT[morse_char]
            else:
                text += '?'
        text += ' '
    return text.strip()

# Main function
if __name__ == "__main__":
    while True:
        # User choice
        choice = input("Choose an option:\n1. Text to Morse Code\n2. Morse Code to Text\n3. Exit\nEnter your choice: ")
        if choice == '1':
            user_input = input("Enter a string to convert to Morse code: ")
            morse_code = text_to_morse(user_input)
            print(f"Morse Code: {morse_code}")
        elif choice == '2':
            user_input = input("Enter Morse code to convert to text (use '/' for spaces between words): ")
            text = morse_to_text(user_input)
            print(f"Text: {text}")
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
