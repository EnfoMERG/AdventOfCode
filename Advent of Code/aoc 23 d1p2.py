import re
def replace_words_with_numbers_in_string(input_string):
    # Dictionary, das Wortdarstellungen von Zahlen auf ihre numerischen Werte abbildet
    word_to_number = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        'zero': '0'
    }
    
    # Ersetze Wörter durch Zahlen im Text
    output_string = input_string
    for word, number in word_to_number.items():
        output_string = output_string.replace(word, number)
    
    return output_string

# Öffnen und Lesen der Textdatei
file_path = "C:\\Users\\TUFFTHYMEZ\\Desktop\\Python\\aoc 23 d1 input.txt"
with open(file_path, "r", encoding="utf-8") as file:
    file_content = file.read()

# Ersetzen der Wörter durch Zahlen im Text
output_text = replace_words_with_numbers_in_string(file_content)

# Ausgabe des verarbeiteten Text
output_text = output_text
print(output_text)

