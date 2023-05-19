import json
import os
import selector
import centeredinputs

minWidth = 55
cols = minWidth


def clear():
    os.system("clear")


def load():
    global cols
    with open("sys.json", "r") as read_file:
        cols = json.load(read_file)["cols"]
        if cols < minWidth:
            cols = minWidth


def get_bank():
    with open("data.json", "r") as read_file:
        return json.load(read_file)["bank"]


def get_bet():
    with open("data.json", "r") as read_file:
        return json.load(read_file)["bet"]


def get_dealer_hand_art():
    with open("hands.json", "r") as read_file:
        return json.load(read_file)["dealerHand"]["art"]


def get_dealer_hand_value():
    with open("hands.json", "r") as read_file:
        return json.load(read_file)["dealerHand"]["value"]


def get_player_hand_art():
    with open("hands.json", "r") as read_file:
        return json.load(read_file)["playerHand"]["art"]


def get_player_hand_value():
    with open("hands.json", "r") as read_file:
        return json.load(read_file)["playerHand"]["value"]


selected = ""
user_in = ""


def display(content, instructions=None):
    global selected
    global user_in

    container_width = cols if cols < 100 else 100

    sel = False
    if type(instructions) is list:
        sel = True

    clear()

    small = """╔══╗──────╔╗──────╔╗──
║╔╗╠╗╔═╗╔═╣╠╦╦═╗╔═╣╠╗─
║╔╗║╚╣╬╚╣═╣═╬╣╬╚╣═╣═╣─
╚══╩═╩══╩═╩╬╝╠══╩═╩╩╝─
───────────╚═╝────────"""

    big = """██████╗ ██╗      █████╗  ██████╗██╗  ██╗     ██╗ █████╗  ██████╗██╗  ██╗
██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝     ██║██╔══██╗██╔════╝██║ ██╔╝
██████╔╝██║     ███████║██║     █████╔╝      ██║███████║██║     █████╔╝ 
██╔══██╗██║     ██╔══██║██║     ██╔═██╗ ██   ██║██╔══██║██║     ██╔═██╗ 
██████╔╝███████╗██║  ██║╚██████╗██║  ██╗╚█████╔╝██║  ██║╚██████╗██║  ██╗
╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝"""

    title = small if cols <= 80 else big

    screen = ""

    for line in title.splitlines():
        screen += line.center(cols) + "\n"

    screen += ("╔" + "═" * (container_width - 2) + "╗").center(cols) + "\n" + \
              ("║" + " " * (container_width - 2) + "║").center(cols) + "\n"

    for line in content.splitlines():
        screen += ("║" + line.center(container_width - 2) + "║").center(cols) + "\n"

    screen += ("║" + " " * (container_width - 2) + "║").center(cols) + "\n"

    if instructions is None:
        screen += "╚" + "═" * (container_width - 2) + "╝"
        print(screen, end="")


    elif instructions is not None and not sel:
        centeredinputs.instructions = instructions
        centeredinputs.input_field = ""
        centeredinputs.user_in = ""
        while True:
            clear()
            print(screen, end="")
            print(("╚" + ("╤" + "═" * 21 + "╤").center(container_width - 2, "═") + "╝").center(cols))
            if centeredinputs.main(cols):
                user_in = centeredinputs.user_in
                break

    elif instructions is not None and sel:
        selector.options = instructions
        selector.cursor_position = 0
        while True:
            clear()
            print(screen, end="")
            print(("╚" + ("╤" + "═" * 21 + "╤").center(container_width - 2, "═") + "╝").center(cols))
            selected = selector.main(cols)
            if selected in instructions:
                break


prompt_TutorialStart = ["BEGIN tutorial", "SKIP"]
prompt_Bet = "Enter your bet:"
prompt_Dismiss = ["CONTINUE"]
prompt_Initial = ["SURRENDER", "DOUBLE DOWN", "CONTINUE"]
prompt_InitialWithInsurance = ["SURRENDER", "BUY INSURANCE", "DOUBLE DOWN", "CONTINUE"]
prompt_Default = ["HIT", "STAND"]

table_Default = ""
table_DealerShown = ""
table_PlayerWon = ""
table_PlayerBlackjack = ""
broke = ""
welcome = ""
alert_AllIn = ""
alert_Surrender = ""
alert_InsuranceSucceeded = ""
alert_InsuranceFailed = ""
alert_DoubleDown = ""
alert_DoubleDownAllIn = ""
alert_DoubleDownFailed = ""
loss_PlayerBusted = ""
loss_PlayerWorseHand = ""
win_PlayerBlackjack = ""
win_PlayerBetterHand = ""
win_DealerBusted = ""
tie_PlayerBlackjack = ""
tie_SameHand = ""


def refresh():
    global table_Default
    global table_DealerShown
    global table_PlayerWon
    global broke
    global welcome
    global alert_AllIn
    global alert_Surrender
    global alert_InsuranceSucceeded
    global alert_InsuranceFailed
    global alert_DoubleDown
    global alert_DoubleDownAllIn
    global alert_DoubleDownFailed
    global loss_PlayerBusted
    global table_PlayerBlackjack
    global win_PlayerBlackjack
    global tie_PlayerBlackjack
    global win_DealerBusted
    global loss_PlayerWorseHand
    global win_PlayerBetterHand
    global tie_SameHand
    table_Default = f"""┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄
Your Balance: ${get_bank() :0,.2f}
Your Bet: ${get_bet() :0,.2f}
┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄

Dealer's Hand:
{get_dealer_hand_art()}

Your Hand (value: {get_player_hand_value()}):
{get_player_hand_art()}"""

    table_DealerShown = f"""┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄
Your Balance: ${get_bank() :0,.2f}
Your Bet: ${get_bet() :0,.2f}
┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄

Dealer's Hand (value: {get_dealer_hand_value()}):
{get_dealer_hand_art()}

Your Hand (value: {get_player_hand_value()}):
{get_player_hand_art()}"""

    table_PlayerWon = f"""┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄
Your Balance: ${get_bank() :0,.2f} (+ ${get_bet() * 1.5:0,.2f})
Your Bet: ${get_bet() :0,.2f}
┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄

Dealer's Hand (value: {get_dealer_hand_value()}):
{get_dealer_hand_art()}
Your Hand (value: {get_player_hand_value()}):
{get_player_hand_art()}

░▒█░░▒█░▒█▀▀▀█░▒█░▒█░░░▒█░░▒█░▀█▀░▒█▄░▒█░█
░▒▀▄▄▄▀░▒█░░▒█░▒█░▒█░░░▒█▒█▒█░▒█░░▒█▒█▒█░▀
░░░▒█░░░▒█▄▄▄█░░▀▄▄▀░░░▒▀▄▀▄▀░▄█▄░▒█░░▀█░▄"""

    broke = """┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄
Your Balance: $0.00
┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄

  ▄▄▄▄    ██▀███   ▒█████   ▀██ ▄█▀▓█████ ▐██▌ 
 ▓█████▄ ▓██ ▒ ██▒▒██▒  ██▒  ██▄█▒ ▓█   ▀ ▐██▌ 
 ▒██▒ ▄██▓██ ░▄█ ▒▒██░  ██▒ ▓███▄░ ▒███   ▐██▌ 
 ▒██░█▀  ▒██▀▀█▄  ▒██   ██░ ▓██ █▄ ▒▓█  ▄ ▓██▒ 
▒░▓█  ▀█▓░██▓ ▒██▒░ ████▓▒░ ▒██▒ █▄░▒████ ▒▄▄  
░░▒▓███▀▒░ ▒▓ ░▒▓░░ ▒░▒░▒░  ▒ ▒▒ ▓▒░░ ▒░  ░▀▀▒ 
░▒░▒   ░   ░▒ ░ ▒░  ░ ▒ ▒░  ░ ░▒ ▒░ ░ ░   ░  ░ 
  ░    ░    ░   ░ ░ ░ ░ ▒   ░ ░░ ░    ░      ░ 
░ ░         ░         ░ ░   ░  ░      ░   ░    

You're BROKE! Try going to Gamblers Anonymous...
Maybe Blackjack isn't for you!"""

    welcome = f"""Welcome to Blackjack!
Your current balance is: ${get_bank() :0,.2f}"""

    alert_AllIn = f"""┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄
Your Balance: $0.00
Your Bet: ${get_bet() :0,.2f}
┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄


░█████╗░██╗░░░░░██╗░░░░░  ██╗███╗░░██╗██╗██╗██╗
██╔══██╗██║░░░░░██║░░░░░  ██║████╗░██║██║██║██║
███████║██║░░░░░██║░░░░░  ██║██╔██╗██║██║██║██║
██╔══██║██║░░░░░██║░░░░░  ██║██║╚████║╚═╝╚═╝╚═╝
██║░░██║███████╗███████╗  ██║██║░╚███║██╗██╗██╗
╚═╝░░╚═╝╚══════╝╚══════╝  ╚═╝╚═╝░░╚══╝╚═╝╚═╝╚═╝

You're all in on this hand! Play wisely!"""

    alert_Surrender = f"""You got half of your initial bet back (${get_bet() / 2:0,.2f}).
Thanks for playing, better luck next time!"""

    alert_InsuranceSucceeded = f"""┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄
Your Balance: ${get_bank() :0,.2f} (+ ${get_bet() * 2:0,.2f})
Your Bet: ${get_bet() :0,.2f}
┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄

Dealer's Hand (value: {get_dealer_hand_value}):
{get_dealer_hand_art}

░██▄░█▒░▒▄▀▄░▄▀▀░█▄▀░░▒█▒▄▀▄░▄▀▀░█▄▀░█
▒█▄█▒█▄▄░█▀█░▀▄▄░█▒█░▀▄█░█▀█░▀▄▄░█▒█░▄

Because you bought insurance, you get all your money back."""

    alert_InsuranceFailed = """The dealer's hand was not 21.
You lost your insurance money!"""

    alert_DoubleDown = f"""┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄
Your Balance: ${get_bank() :0,.2f} (-${get_bet() :0,.2f})
Your Bet: ${get_bet() :0,.2f} (x2)
┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄

╔═══╗╔═══╗╔╗ ╔╗╔══╗ ╔╗   ╔═══╗    ╔═══╗╔═══╗╔╗╔╗╔╗╔═╗ ╔╗╔╗
╚╗╔╗║║╔═╗║║║ ║║║╔╗║ ║║   ║╔══╝    ╚╗╔╗║║╔═╗║║║║║║║║║╚╗║║║║
 ║║║║║║ ║║║║ ║║║╚╝╚╗║║   ║╚══╗     ║║║║║║ ║║║║║║║║║╔╗╚╝║║║
 ║║║║║║ ║║║║ ║║║╔═╗║║║ ╔╗║╔══╝     ║║║║║║ ║║║╚╝╚╝║║║╚╗║║╚╝
╔╝╚╝║║╚═╝║║╚═╝║║╚═╝║║╚═╝║║╚══╗    ╔╝╚╝║║╚═╝║╚╗╔╗╔╝║║ ║║║╔╗
╚═══╝╚═══╝╚═══╝╚═══╝╚═══╝╚═══╝    ╚═══╝╚═══╝ ╚╝╚╝ ╚╝ ╚═╝╚╝

DOUBLE DOWN! You must be confident in this hand."""

    alert_DoubleDownAllIn = f"""┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄
Your Balance: $0.00
Your Bet: ${get_bet() :0,.2f} (+ ${get_bank() :0,.2f})
┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄

░█████╗░██╗░░░░░██╗░░░░░  ██╗███╗░░██╗██╗██╗██╗
██╔══██╗██║░░░░░██║░░░░░  ██║████╗░██║██║██║██║
███████║██║░░░░░██║░░░░░  ██║██╔██╗██║██║██║██║
██╔══██║██║░░░░░██║░░░░░  ██║██║╚████║╚═╝╚═╝╚═╝
██║░░██║███████╗███████╗  ██║██║░╚███║██╗██╗██╗
╚═╝░░╚═╝╚══════╝╚══════╝  ╚═╝╚═╝░░╚══╝╚═╝╚═╝╚═╝

You're all in on this hand! Play wisely!"""

    alert_DoubleDownFailed = "You don't have enough money to double down on this hand!"

    loss_PlayerBusted = f"""{table_DealerShown}

▄▄▄▄· ▄• ▄▌.▄▄ · ▄▄▄▄▄▄      
▐█ ▀█▪█▪██▌▐█ ▀. ▀•██ ▀      
▐█▀▀█▄█▌▐█▌▄▀▀▀█▄  ▐█.▪      
██▄▪▐█▐█▄█▌▐█▄▪▐█  ▐█▌·      
·▀▀▀▀  ▀▀▀  ▀▀▀▀   ▀▀▀ ▀ ▀ ▀ 

Better luck next time!"""

    table_PlayerBlackjack = f"""{table_Default}

░██▄░█▒░▒▄▀▄░▄▀▀░█▄▀░░▒█▒▄▀▄░▄▀▀░█▄▀░█
▒█▄█▒█▄▄░█▀█░▀▄▄░█▒█░▀▄█░█▀█░▀▄▄░█▒█░▄"""

    win_PlayerBlackjack = f"""{table_PlayerWon}

░██▄░█▒░▒▄▀▄░▄▀▀░█▄▀░░▒█▒▄▀▄░▄▀▀░█▄▀░█
▒█▄█▒█▄▄░█▀█░▀▄▄░█▒█░▀▄█░█▀█░▀▄▄░█▒█░▄

CONGRATULATIONS! You won this round!"""

    tie_PlayerBlackjack = f"""┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄
Your Balance: ${get_bank() :0,.2f} (+ ${get_bet() :0,.2f})
Your Bet: ${get_bet() :0,.2f}
┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄

Dealer's Hand (value: {get_dealer_hand_value()}):
{get_dealer_hand_art()}

Your Hand (value: {get_player_hand_value()}):
{get_player_hand_art()}

░██▄░█▒░▒▄▀▄░▄▀▀░█▄▀░░▒█▒▄▀▄░▄▀▀░█▄▀░█
▒█▄█▒█▄▄░█▀█░▀▄▄░█▒█░▀▄█░█▀█░▀▄▄░█▒█░▄

It's a tie! Both you and the dealer got Blackjack!
Your bet has been returned."""

    win_DealerBusted = f"""{table_PlayerWon}

The dealer busted, so you've won this round! Good job!"""

    loss_PlayerWorseHand = f"""{table_DealerShown}

░▒█░░▒█░▄▀▀▄░█░▒█░░░█░░▄▀▀▄░█▀▀░█▀▀░░░░░░░░░
░▒▀▄▄▄▀░█░░█░█░▒█░░░█░░█░░█░▀▀▄░█▀▀░▄▄░▄▄░▄▄
░░░▒█░░░░▀▀░░░▀▀▀░░░▀▀░░▀▀░░▀▀▀░▀▀▀░▀▀░▀▀░▀▀

The dealer has a better hand. Too bad!
Better luck next time!"""

    win_PlayerBetterHand = f"""{table_PlayerWon}
You win! Your hand was better than the dealer!"""

    tie_SameHand = f"""┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄
Your Balance: ${get_bank() :0,.2f} (+ ${get_bet() :0,.2f})
Your Bet: ${get_bet() :0,.2f}
┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄

Dealer's Hand (value: {get_dealer_hand_value()}):
{get_dealer_hand_art()}

Your Hand (value: {get_player_hand_value()}):
{get_player_hand_art()}

__ __|_)        |
   |   |   _ \  |
   |   |   __/ _|
  _|  _| \___| _)

Tie game! You and the dealer had the same hand. 
Your bet has been returned to you."""
