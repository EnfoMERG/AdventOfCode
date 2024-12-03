def sum_benachbart_numbers(schematic): # definiere die Richtungen indem geprüft werden soll horizontal vertikal und Diagonal!
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    
    def is_valid_position(x, y):
        return 0 <= x < len(schematic[0]) and 0 <= y < len(schematic)

    def is_symbol(x, y):
        return schematic[y][x] != '.'

    def is_number(x, y):
        return schematic[y][x].isdigit()
    def is_adjacent_to_symbol(x, y):
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid_position(nx, ny) and is_symbol(nx, ny):
                return True
        return False
    total = 0
    for y in range(len(schematic)):
        for x in range(len(schematic[0])):
            if is_number(x, y) and is_adjacent_to_symbol(x, y):
                total += int(schematic[y][x])
    return total

# Example engine schematic
schematic = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598.."
]

# Calculate the sum of adjacent numbers
result = sum_benachbart_numbers(schematic)
print("Sum of all part numbers:", result)
