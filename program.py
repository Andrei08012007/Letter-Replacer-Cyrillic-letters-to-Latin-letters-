# Mapping dictionary from Cyrillic letters to Latin letters
translation_map = {
    'ф': 'A', 
    'и': 'B', 
    'с': 'C', 
    'в': 'D', 
    'у': 'E', 
    'а': 'F', 
    'п': 'G',
    'р': 'H', 
    'ш': 'I', 
    'о': 'J', 
    'л': 'K', 
    'д': 'L', 
    'ь': 'M', 
    'т': 'N',
    'щ': 'O', 
    'з': 'P', 
    'й': 'Q', 
    'к': 'R', 
    'ы': 'S', 
    'е': 'T', 
    'г': 'U',
    'м': 'V', 
    'ц': 'W', 
    'ч': 'X', 
    'н': 'Y', 
    'я': 'Z',
    'ж': ':',
    '№': '#',
    'Б': '<',
    'Ю': '>',
    'б': ',',
    'ю': '.',
}

def translate_text(input_text):
    translated_text = ''.join(translation_map.get(char, char) for char in input_text)
    return translated_text

# Welcome Message 
print("This code only works with Ossetic Russian Letters.")
print("This code doesn't support translating UPPER CASE letters.\nAka it will only translate in upper case letters.\n")

# This code cannot replace upper case letters and all, because it will loop otherwise. Tried to test and all and doesn't work, loops and breaks the replacer, making it useless. So yeah ¯\_(ツ)_/¯

# Loop pana cand se inchide programul
while True:
    # Get user input
    user_input = input("Input: ").lower()  # Get user input and convert to lowercase
    
    # Translate input 
    translated_output = translate_text(user_input)
    
    # Translated output
    print("Output:", translated_output)
    print()  # Print empty line for separation or formatting

    # Optiune pt a iesi din program 
    exit_command = input("Type 'n' to quit, or press Enter to continue.\n")
    if exit_command.lower() == 'n':
        break  
