import readchar

options = []
cursor_position = 0


def display_options(cols):
    print("╚" + ("╤" + "═" * 21 + "╤").center(cols - 2, "═") + "╝")
    for i, option in enumerate(options):
        if i == cursor_position:
            print(("│ ⮞" + f"─{option}─".center(17) + "⮜ │").center(cols))
        else:
            print(("│" + f"{option}".center(21) + "│").center(cols))
    print(("╰" + "─" * 21 + "╯").center(cols))


def move_cursor_up():
    global cursor_position
    cursor_position = (cursor_position - 1) % len(options)


def move_cursor_down():
    global cursor_position
    cursor_position = (cursor_position + 1) % len(options)


def main(cols):
    display_options(cols)
    key = readchar.readkey()

    if key == readchar.key.UP:
        move_cursor_up()
    elif key == readchar.key.DOWN:
        move_cursor_down()
    elif key == readchar.key.ENTER:
        return options[cursor_position]
