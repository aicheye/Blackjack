import json
import os
import libs.selector_handler as selector_handler
import libs.input_handler as input_handler

minWidth = 65
cols = minWidth


def clear():
    os.system("cls")


def load():
    global cols
    with open("data.json", "r") as read_file:
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
    with open("data.json", "r") as read_file:
        return json.load(read_file)["dealerHand"]["art"]


def get_dealer_hand_value():
    with open("data.json", "r") as read_file:
        return json.load(read_file)["dealerHand"]["value"]


def get_player_hand_art():
    with open("data.json", "r") as read_file:
        return json.load(read_file)["playerHand"]["art"]


def get_player_hand_value():
    with open("data.json", "r") as read_file:
        return json.load(read_file)["playerHand"]["value"]


def get_profit():
    with open("data.json", "r") as read_file:
        return json.load(read_file)["profit"]


def get_wins():
    with open("data.json", "r") as read_file:
        return json.load(read_file)["wins"]


def get_losses():
    with open("data.json", "r") as read_file:
        return json.load(read_file)["losses"]


user_selected = ""
user_in = ""


def display(content, instructions=None):
    global user_selected
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
        screen += ("╚" + "═" * (container_width - 2) + "╝").center(cols)
        print(screen, end="")

    elif instructions == prompt_Bet:
        input_handler.instructions = instructions
        input_handler.input_field = ""
        input_handler.user_in = ""
        while True:
            clear()
            print(screen, end="")
            print(("╚" + ("╤" + "═" * 21 + "╤").center(container_width - 2, "═") + "╝").center(cols))
            if input_handler.main(cols):
                user_in = input_handler.user_in
                break

    elif instructions is not None and not sel:
        input_handler.instructions = instructions
        input_handler.input_field = ""
        input_handler.user_in = ""
        while True:
            clear()
            print(screen, end="")
            print(("╚" + ("╤" + "═" * 21 + "╤").center(container_width - 2, "═") + "╝").center(cols))
            if input_handler.generic(cols):
                user_in = input_handler.user_in
                break

    elif instructions is not None and sel:
        selector_handler.options = instructions
        selector_handler.cursor_position = 0
        while True:
            clear()
            print(screen, end="")
            print(("╚" + ("╤" + "═" * 21 + "╤").center(container_width - 2, "═") + "╝").center(cols))
            user_selected = selector_handler.main(cols)
            if user_selected in instructions:
                break


prompt_TutorialStart = ["BEGIN tutorial", "SKIP"]
prompt_Bet = "Enter your bet:"
prompt_Initial = ["CONTINUE", "DOUBLE DOWN", "SURRENDER"]
prompt_InitialWithInsurance = ["CONTINUE", "DOUBLE DOWN", "BUY INSURANCE", "SURRENDER"]
prompt_Default = ["HIT", "STAND"]
prompt_CashOut = ["CONTINUE", "CASH OUT", "DISABLE"]
prompt_Deposit = ["DEPOSIT", "EXIT"]
prompt_Exit = ["BACK", "EXIT"]
prompt_Dismiss = ["CONTINUE"]

global stats
global stats_final

global table_Default
global table_DealerShown
global table_PlayerBlackjack
global table_PlayerWon

global welcome
global cash_out
global deposit
global broke

global alert_AllIn
global alert_Surrender
global alert_InsuranceFailed
global alert_InsuranceSucceeded
global alert_DoubleDown
global alert_DoubleDownAllIn
global alert_DoubleDownFailed

global win_PlayerBlackjack
global win_PlayerBetterHand
global win_DealerBusted

global loss_PlayerBusted
global loss_PlayerWorseHand

global tie_SameBlackjack
global tie_SameHand


def refresh():
    global stats
    global stats_final

    global table_Default
    global table_DealerShown
    global table_PlayerBlackjack
    global table_PlayerWon

    global welcome
    global cash_out
    global deposit
    global broke

    global alert_AllIn
    global alert_Surrender
    global alert_InsuranceFailed
    global alert_InsuranceSucceeded
    global alert_DoubleDown
    global alert_DoubleDownAllIn
    global alert_DoubleDownFailed

    global win_PlayerBlackjack
    global win_PlayerBetterHand
    global win_DealerBusted

    global loss_PlayerBusted
    global loss_PlayerWorseHand

    global tie_SameBlackjack
    global tie_SameHand

    if get_profit() >= 0:
        stats = """YOUR STATS
┌─────────────────────────┐
│""" + f"Profit: ${get_profit():0,.2f}".center(25) + "│\n" + \
                "│" + f"Wins: {get_wins()}".center(25) + "│\n" + \
                "│" + f"Losses: {get_losses()}".center(25) + "│\n" + \
                "└─────────────────────────┘"
    else:
        stats = """YOUR STATS
┌─────────────────────────┐
│""" + f"Profit: -${abs(get_profit()):0,.2f}".center(25) + "│\n" + \
                "│" + f"Wins: {get_wins()}".center(25) + "│\n" + \
                "│" + f"Losses: {get_losses()}".center(25) + "│\n" + \
                "└─────────────────────────┘"

    stats_final = stats.replace("┌", "╔")
    stats_final = stats_final.replace("┐", "╗")
    stats_final = stats_final.replace("┘", "╝")
    stats_final = stats_final.replace("└", "╚")
    stats_final = stats_final.replace("─", "═")
    stats_final = stats_final.replace("│", "║")

    table_Default = f"""┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄
Your Balance: ${get_bank():0,.2f}
Your Bet: ${get_bet():0,.2f}
┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄

Dealer's Hand:
{get_dealer_hand_art()}

Your Hand (value: {get_player_hand_value()}):
{get_player_hand_art()}"""

    table_DealerShown = f"""┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄
Your Balance: ${get_bank():0,.2f}
Your Bet: ${get_bet():0,.2f}
┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄

Dealer's Hand (value: {get_dealer_hand_value()}):
{get_dealer_hand_art()}

Your Hand (value: {get_player_hand_value()}):
{get_player_hand_art()}"""

    table_PlayerBlackjack = f"""{table_Default}

░██▄░█▒░▒▄▀▄░▄▀▀░█▄▀░░▒█▒▄▀▄░▄▀▀░█▄▀░█
▒█▄█▒█▄▄░█▀█░▀▄▄░█▒█░▀▄█░█▀█░▀▄▄░█▒█░▄"""

    table_PlayerWon = f"""┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄
Your Balance: ${get_bank():0,.2f} (+ ${get_bet() * 2:0,.2f})
Your Bet: ${get_bet():0,.2f}
┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄

Dealer's Hand (value: {get_dealer_hand_value()}):
{get_dealer_hand_art()}

Your Hand (value: {get_player_hand_value()}):
{get_player_hand_art()}"""

    welcome = f"""{stats}

Welcome to Blackjack!
Your current balance is: ${get_bank():0,.2f}.

Place your bet on this round below.
(Type "all" to go all in)"""

    cash_out = f"""┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄
Your Balance: ${get_bank():0,.2f}
┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄

Would you like to cash out your balance now
or continue to play?

Select DISABLE to disable this prompt
for 3 rounds"""

    deposit = f"""{stats}

Would you like to deposit another $10,000 to
continue playing?"""

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

    alert_AllIn = f"""┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄
Your Balance: $0.00
Your Bet: ${get_bet():0,.2f}
┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄


░█████╗░██╗░░░░░██╗░░░░░  ██╗███╗░░██╗██╗██╗██╗
██╔══██╗██║░░░░░██║░░░░░  ██║████╗░██║██║██║██║
███████║██║░░░░░██║░░░░░  ██║██╔██╗██║██║██║██║
██╔══██║██║░░░░░██║░░░░░  ██║██║╚████║╚═╝╚═╝╚═╝
██║░░██║███████╗███████╗  ██║██║░╚███║██╗██╗██╗
╚═╝░░╚═╝╚══════╝╚══════╝  ╚═╝╚═╝░░╚══╝╚═╝╚═╝╚═╝

You're all in on this hand! Play wisely!"""

    alert_Surrender = f"""You got half of your initial bet back (${(get_bet() * 100) // 2 / 100:0,.2f}).
Thanks for playing, better luck next time!"""

    alert_InsuranceFailed = """The dealer's hand was not 21.
You lost your insurance money!"""

    alert_InsuranceSucceeded = f"""┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄
Your Balance: ${get_bank():0,.2f} (+ ${get_bet() * 2:0,.2f})
Your Bet: ${get_bet():0,.2f}
┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄

Dealer's Hand (value: {get_dealer_hand_value()}):
{get_dealer_hand_art()}

░██▄░█▒░▒▄▀▄░▄▀▀░█▄▀░░▒█▒▄▀▄░▄▀▀░█▄▀░█
▒█▄█▒█▄▄░█▀█░▀▄▄░█▒█░▀▄█░█▀█░▀▄▄░█▒█░▄

Because you bought insurance, you get all your money back."""

    alert_DoubleDown = f"""┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄
Your Balance: ${get_bank():0,.2f} (-${get_bet():0,.2f})
Your Bet: ${get_bet():0,.2f} (x2)
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
Your Bet: ${get_bet():0,.2f} (+ ${get_bank():0,.2f})
┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄

░█████╗░██╗░░░░░██╗░░░░░  ██╗███╗░░██╗██╗██╗██╗
██╔══██╗██║░░░░░██║░░░░░  ██║████╗░██║██║██║██║
███████║██║░░░░░██║░░░░░  ██║██╔██╗██║██║██║██║
██╔══██║██║░░░░░██║░░░░░  ██║██║╚████║╚═╝╚═╝╚═╝
██║░░██║███████╗███████╗  ██║██║░╚███║██╗██╗██╗
╚═╝░░╚═╝╚══════╝╚══════╝  ╚═╝╚═╝░░╚══╝╚═╝╚═╝╚═╝

You're all in on this hand! Play wisely!"""

    alert_DoubleDownFailed = "You don't have enough money to double down on this hand!"

    win_PlayerBlackjack = f"""{table_PlayerWon}

░██▄░█▒░▒▄▀▄░▄▀▀░█▄▀░░▒█▒▄▀▄░▄▀▀░█▄▀░█
▒█▄█▒█▄▄░█▀█░▀▄▄░█▒█░▀▄█░█▀█░▀▄▄░█▒█░▄

CONGRATULATIONS! You won this round!"""

    win_PlayerBetterHand = f"""{table_PlayerWon}

░▒█░░▒█░▒█▀▀▀█░▒█░▒█░░░▒█░░▒█░▀█▀░▒█▄░▒█░█
░▒▀▄▄▄▀░▒█░░▒█░▒█░▒█░░░▒█▒█▒█░▒█░░▒█▒█▒█░▀
░░░▒█░░░▒█▄▄▄█░░▀▄▄▀░░░▒▀▄▀▄▀░▄█▄░▒█░░▀█░▄

You win! Your hand was better than the dealer!"""

    win_DealerBusted = f"""{table_PlayerWon}

░▒█░░▒█░▒█▀▀▀█░▒█░▒█░░░▒█░░▒█░▀█▀░▒█▄░▒█░█
░▒▀▄▄▄▀░▒█░░▒█░▒█░▒█░░░▒█▒█▒█░▒█░░▒█▒█▒█░▀
░░░▒█░░░▒█▄▄▄█░░▀▄▄▀░░░▒▀▄▀▄▀░▄█▄░▒█░░▀█░▄

The dealer busted, so you've won this round! Good job!"""

    loss_PlayerBusted = f"""{table_DealerShown}

▄▄▄▄· ▄• ▄▌.▄▄ · ▄▄▄▄▄▄      
▐█ ▀█▪█▪██▌▐█ ▀. ▀•██ ▀      
▐█▀▀█▄█▌▐█▌▄▀▀▀█▄  ▐█.▪      
██▄▪▐█▐█▄█▌▐█▄▪▐█  ▐█▌·      
·▀▀▀▀  ▀▀▀  ▀▀▀▀   ▀▀▀ ▀ ▀ ▀ 

Better luck next time!"""

    loss_PlayerWorseHand = f"""{table_DealerShown}

░▒█░░▒█░▄▀▀▄░█░▒█░░░█░░▄▀▀▄░█▀▀░█▀▀░░░░░░░░░
░▒▀▄▄▄▀░█░░█░█░▒█░░░█░░█░░█░▀▀▄░█▀▀░▄▄░▄▄░▄▄
░░░▒█░░░░▀▀░░░▀▀▀░░░▀▀░░▀▀░░▀▀▀░▀▀▀░▀▀░▀▀░▀▀

The dealer has a better hand. Too bad!
Better luck next time!"""

    tie_SameBlackjack = f"""┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄
Your Balance: ${get_bank():0,.2f} (+ ${get_bet():0,.2f})
Your Bet: ${get_bet():0,.2f}
┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄

Dealer's Hand (value: {get_dealer_hand_value()}):
{get_dealer_hand_art()}

Your Hand (value: {get_player_hand_value()}):
{get_player_hand_art()}

░██▄░█▒░▒▄▀▄░▄▀▀░█▄▀░░▒█▒▄▀▄░▄▀▀░█▄▀░█
▒█▄█▒█▄▄░█▀█░▀▄▄░█▒█░▀▄█░█▀█░▀▄▄░█▒█░▄

It's a tie! Both you and the dealer got Blackjack!
Your bet has been returned."""

    tie_SameHand = f"""┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄
Your Balance: ${get_bank():0,.2f} (+ ${get_bet():0,.2f})
Your Bet: ${get_bet():0,.2f}
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
