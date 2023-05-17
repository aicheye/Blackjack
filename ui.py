import json
import os


def getBank():
    with open("data.json", "r") as read_file:
        return json.load(read_file)["bank"]


def getBet():
    with open("data.json", "r") as read_file:
        return json.load(read_file)["bet"]


def getDealerHandArt():
    with open("hands.json", "r") as read_file:
        return json.load(read_file)["dealerHand"]["art"]


def getDealerHandVal():
    with open("hands.json", "r") as read_file:
        return json.load(read_file)["dealerHand"]["value"]


def getPlayerHandArt():
    with open("hands.json", "r") as read_file:
        return json.load(read_file)["playerHand"]["art"]


def getPlayerHandVal():
    with open("hands.json", "r") as read_file:
        return json.load(read_file)["playerHand"]["value"]


def clear():
    os.system("clear")


def display(content, instructions=None):
    clear()
    lines = content.split("\n")
    screen = """
  ██████╗ ██╗      █████╗  ██████╗██╗  ██╗     ██╗ █████╗  ██████╗██╗  ██╗
  ██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝     ██║██╔══██╗██╔════╝██║ ██╔╝
  ██████╔╝██║     ███████║██║     █████╔╝      ██║███████║██║     █████╔╝ 
  ██╔══██╗██║     ██╔══██║██║     ██╔═██╗ ██   ██║██╔══██║██║     ██╔═██╗ 
  ██████╔╝███████╗██║  ██║╚██████╗██║  ██╗╚█████╔╝██║  ██║╚██████╗██║  ██╗
  ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║"""
    for line in lines:
        screen += "\n║"
        screen += line.center(75)
        screen += "║"

    screen += """\n║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝"""
    if instructions is not None:
        screen += f"\n{instructions}\n> "
    print(screen, end="")


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
alert_DoubleDownImpossible = ""
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
    global alert_DoubleDownImpossible
    global loss_PlayerBusted
    global table_PlayerBlackjack
    global win_PlayerBlackjack
    global tie_PlayerBlackjack
    global win_DealerBusted
    global loss_PlayerWorseHand
    global win_PlayerBetterHand
    global tie_SameHand
    table_Default = f"""┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄
Your Balance: ${getBank():0,.2f}
Your Bet: ${getBet():0,.2f}
┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄

Dealer's Hand:
{getDealerHandArt()}

Your Hand (value: {getPlayerHandVal()}):
{getPlayerHandArt()}"""

    table_DealerShown = f"""┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄
Your Balance: ${getBank():0,.2f}
Your Bet: ${getBet():0,.2f}
┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄

Dealer's Hand (value: {getDealerHandVal()}):
{getDealerHandArt()}

Your Hand (value: {getPlayerHandVal()}):
{getPlayerHandArt()}"""

    table_PlayerWon = f"""┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄
Your Balance: ${getBank():0,.2f} (+ ${getBet() * 1.5:0,.2f})
Your Bet: ${getBet():0,.2f}
┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄

Dealer's Hand (value: {getDealerHandVal()}):
{getDealerHandArt()}

Your Hand (value: {getPlayerHandVal()}):
{getPlayerHandArt()}

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

You're BROKE! Try making an appointment at Gamblers Anonymous...
Maybe Blackjack isn't for you!"""

    welcome = f"""Welcome to Blackjack!
Your current balance is: ${getBank():0,.2f}"""

    alert_AllIn = f"""┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄
Your Balance: $0.00
Your Bet: ${getBet():0,.2f}
┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄


░█████╗░██╗░░░░░██╗░░░░░  ██╗███╗░░██╗██╗██╗██╗
██╔══██╗██║░░░░░██║░░░░░  ██║████╗░██║██║██║██║
███████║██║░░░░░██║░░░░░  ██║██╔██╗██║██║██║██║
██╔══██║██║░░░░░██║░░░░░  ██║██║╚████║╚═╝╚═╝╚═╝
██║░░██║███████╗███████╗  ██║██║░╚███║██╗██╗██╗
╚═╝░░╚═╝╚══════╝╚══════╝  ╚═╝╚═╝░░╚══╝╚═╝╚═╝╚═╝

You're all in on this hand! Play wisely!"""

    alert_Surrender = f"""You got half of your initial bet back (${getBet() / 2:0,.2f}).
Thanks for playing, better luck next time!"""

    alert_InsuranceSucceeded = f"""┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄
Your Balance: ${getBank():0,.2f} (+ ${getBet() * 2:0,.2f})
Your Bet: ${getBet():0,.2f}
┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄

Dealer's Hand (value: {getDealerHandVal}):
{getDealerHandArt}

░██▄░█▒░▒▄▀▄░▄▀▀░█▄▀░░▒█▒▄▀▄░▄▀▀░█▄▀░█
▒█▄█▒█▄▄░█▀█░▀▄▄░█▒█░▀▄█░█▀█░▀▄▄░█▒█░▄
Because you bought insurance, you get all your money back."""

    alert_InsuranceFailed = """The dealer's hand was not 21.
You lost your insurance money!"""

    alert_DoubleDown = f"""┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄
Your Balance: ${getBank():0,.2f} (-${getBet():0,.2f})
Your Bet: ${getBet():0,.2f} (x2)
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
Your Bet: ${getBet():0,.2f} (+ ${getBank():0,.2f})
┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄


░█████╗░██╗░░░░░██╗░░░░░  ██╗███╗░░██╗██╗██╗██╗
██╔══██╗██║░░░░░██║░░░░░  ██║████╗░██║██║██║██║
███████║██║░░░░░██║░░░░░  ██║██╔██╗██║██║██║██║
██╔══██║██║░░░░░██║░░░░░  ██║██║╚████║╚═╝╚═╝╚═╝
██║░░██║███████╗███████╗  ██║██║░╚███║██╗██╗██╗
╚═╝░░╚═╝╚══════╝╚══════╝  ╚═╝╚═╝░░╚══╝╚═╝╚═╝╚═╝

You're all in on this hand! Play wisely!"""

    alert_DoubleDownImpossible = "You don't have enough money to double down on this hand!"

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

    win_PlayerBlackjack = f"""{table_PlayerBlackjack}

CONGRATULATIONS! You won this round!"""

    tie_PlayerBlackjack = f"""{table_PlayerBlackjack}

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
Your Balance: ${getBank():0,.2f} (+ ${getBet():0,.2f})
Your Bet: ${getBet():0,.2f}
┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄

Dealer's Hand (value: {getDealerHandVal()}):
{getDealerHandArt()}

Your Hand (value: {getPlayerHandVal()}):
{getPlayerHandArt()}

__ __|_)        |
   |   |   _ \  |
   |   |   __/ _|
  _|  _| \___| _)

Tie game! You and the dealer had the same hand. 
Your bet has been returned to you."""
