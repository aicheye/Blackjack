import readchar

input_field = ""
instructions = ""
user_in = ""


def generic(cols, restriction=None):
    global input_field
    global instructions
    global user_in

    print(("│" + instructions.center(21) + "│").center(cols))
    print(("│" + input_field.center(21) + "│").center(cols))
    print(("╰" + "─" * 21 + "╯").center(cols))

    key = readchar.readkey()

    if key == readchar.key.ENTER:
        user_in = input_field
        return True
    elif key == readchar.key.BACKSPACE:
        input_field = input_field[:-1]
    elif restriction is None:
        input_field += key
    elif key in restriction:
        input_field += key


def main(cols):
    global input_field
    global instructions
    global user_in

    try:
        int(input_field)
    except ValueError:
        try:
            float(input_field)
        except ValueError:
            if "k" in input_field:
                display = f"${int(input_field[:-1]):0,}k"
            else:
                display = input_field
        else:
            display = f"${float(input_field):0,.2f}"
    else:
        display = f"${int(input_field):0,}"

    print(("│" + instructions.center(21) + "│").center(cols))
    print(("│" + display.center(21) + "│").center(cols))
    print(("╰" + "─" * 21 + "╯").center(cols))

    key = readchar.readkey()

    if key == readchar.key.ENTER:
        user_in = input_field
        return True
    elif key == readchar.key.BACKSPACE:
        input_field = input_field[:-1]

    elif len(input_field) < 14:
        if key in "0123456789":
            if "." not in input_field and "k" not in input_field and "a" not in input_field:
                input_field += key

            elif "." in input_field:
                if len(input_field.split(".")[1]) < 2:
                    input_field += key

        elif key == ".":
            if len(input_field) > 0 and "." not in input_field and "k" not in input_field and "a" not in input_field:
                input_field += key

        elif key == "k":
            try:
                int(input_field)
            except ValueError:
                pass
            else:
                input_field += key

        elif key in "all":
            if key == "a" and input_field == "":
                input_field += key
            elif key == "l" and (input_field == "a" or input_field == "al"):
                input_field += key
