with open("C:\\Users\\TUFFTHYMEZ\\Desktop\\aoc 23d3p1 input.txt") as fin:
    input = fin.read().strip().split("\n") # packt input.txt in ein 1d array und listet auf
# da jede Zeile gleiche Anzahl an char hat, print(len(lines) = 140 char
# lege input in ein Koordinatensystem y = row , x = column bzw. char
y_max_anzahl_rows = len(input) # anzahl rows 
x_max_länge_row = len(input[0]) # anzahl column, [0] erste line da das 2d-Grid quadratisch ist.

# prüfe Symbol , ignoriere "." und Zahlen
#                          y     x            
def erkenne_Sonderzeichen(row, char):
    if not (0 <= row < y_max_anzahl_rows and 0 <= char < x_max_länge_row): # verhindere out of range
        return False 
    return input[row][char] != "." and not input[row][char].isdigit() ## prüfe ob Symbol: ignoriere "." und Zahlen

Gesamtsumme = 0
# enumerate() geht jede row und jeden char einer row durch, nummeriert sie und setzt beide in relation
for row, value_char_in_row  in enumerate(input):
    pos_first_num = 0
    current_position_char_in_row = 0
    while current_position_char_in_row < x_max_länge_row: 
        pos_first_num = current_position_char_in_row
        num = "" # string , da ich den wert aus nem array nehmen will
        while current_position_char_in_row < x_max_länge_row and value_char_in_row[current_position_char_in_row].isdigit(): # .isdigit(), damit while nur bei einer Nummer greift
            num = num + value_char_in_row[current_position_char_in_row] # speichere zahl 
            current_position_char_in_row += 1 # rücke eins weiter

        if num == "":
            current_position_char_in_row += 1#
            continue # übersrpinge den code unten und setze schleife fort

        num = int(num) # erste zahlensequenz bestimmt
        print(num)     # prüfe ob Sonderzeichen benachbart sind

 # -----current_position_char_in_row = ist die letzte position der Zahl somit haben wir die range in der wir ein Sonderzeichen suchen müssen--------------------------------------
        if erkenne_Sonderzeichen(row, pos_first_num-1) or erkenne_Sonderzeichen(row, current_position_char_in_row):
            Gesamtsumme = Gesamtsumme + num    # links , rechts
            continue   # falls links oder rechts ein Sonderzeichen ist, überspringen wir mit continue und müssen obere und untere row nicht checken

        for c in range(pos_first_num-1, current_position_char_in_row+1):        #  unsere range innerhalb der row
            if erkenne_Sonderzeichen(row-1, c) or erkenne_Sonderzeichen(row+1, c):  # obere row-1 und utere row+1. hier ist enumerate wichtig!
                Gesamtsumme += num
                break 

print(Gesamtsumme)