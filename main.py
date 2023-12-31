def get_keyboard_position(char):
    keyboard_layout = {
        '1': (0, 1), '2': (0, 2), '3': (0, 3), '4': (0, 4), '5': (0, 5), '6': (0, 6), '7': (0, 7), '8': (0, 8), '9': (0, 9), '0': (0, 10),
        'q': (1, 0), 'w': (1, 1), 'e': (1, 2), 'r': (1, 3), 't': (1, 4), 'y': (1, 5), 'u': (1, 6), 'i': (1, 7), 'o': (1, 8), 'p': (1, 9),
        'a': (2, 0), 's': (2, 1), 'd': (2, 2), 'f': (2, 3), 'g': (2, 4), 'h': (2, 5), 'j': (2, 6), 'k': (2, 7), 'l': (2, 8),
        'z': (3, 0), 'x': (3, 1), 'c': (3, 2), 'v': (3, 3), 'b': (3, 4), 'n': (3, 5), 'm': (3, 6),
        'Q': (1, 0), 'W': (1, 1), 'E': (1, 2), 'R': (1, 3), 'T': (1, 4), 'Y': (1, 5), 'U': (1, 6), 'I': (1, 7), 'O': (1, 8), 'P': (1, 9),  '[': (1, 10), '{': (1, 10), ']': (1, 11), '}': (1, 11), '\\': (1, 12), '|': (1, 12),
        'A': (2, 0), 'S': (2, 1), 'D': (2, 2), 'F': (2, 3), 'G': (2, 4), 'H': (2, 5), 'J': (2, 6), 'K': (2, 7), 'L': (2, 8), ';': (2, 9), ':': (2, 9), "'": (2, 10), '"': (2, 10),
        'Z': (3, 0), 'X': (3, 1), 'C': (3, 2), 'V': (3, 3), 'B': (3, 4), 'N': (3, 5), 'M': (3, 6), ',': (3, 7), '<': (3, 7), '.': (3, 8), '>': (3,8), '/': (3, 9), '?': (3, 9),
        '`': (0, 0), '~': (0, 0), '!': (0, 1), '@': (0, 2), '#': (0, 3), '$': (0, 4), '%': (0, 5), '^': (0, 6), '&': (0, 7), '*': (0, 8), '(': (0, 9),')':(0,10),'_':(0,11),'-':(0,11),'+':(0,12),'=':(0,12),
        ' ': (4,0)
    }

    if char in keyboard_layout:
        return keyboard_layout[char]
    else:
        return None

character = input("Enter a character: ")
position = get_keyboard_position(character)
if position:
    print("Position on the keyboard:", position)
else:
    print("Character not found on the keyboard.")
