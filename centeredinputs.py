import readchar


input_field = ""
instructions = ""
user_in = ""
prefix = "$"


def main(cols):
    global input_field
    global instructions
    global user_in

    print("╚" + ("╤" + "═" * 21 + "╤").center(cols - 2, "═") + "╝")
    print(("│" + instructions.center(21) + "│").center(cols))
    print(("│" + prefix + input_field.center(21) + "│").center(cols))
    print(("╰" + "─" * 21 + "╯").center(cols))

    key = readchar.readkey()

    if key == readchar.key.ENTER:
        user_in = input_field
        return True
    elif key == readchar.key.BACKSPACE:
        input_field = input_field[:-1]
    elif len(input_field) < 15:
        input_field += key
