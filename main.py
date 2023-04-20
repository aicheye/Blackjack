import random
import time
import os


def clear():
    os.system("clear")


class Card:
    def __init__(self, number, suit):
        if 0 > number or number > 14:
            raise ValueError("The number of a card must be between 1 and 13, inclusive.")
        suits = ["Spades", "Diamonds", "Clubs", "Hearts"]
        if suit not in suits:
            raise ValueError("The suit of a card can only be Spades, Diamonds, Clubs, or Hearts.")
        self.number = number
        self.value = number
        self.suit = suit
        if self.number == 1:
            self.ace = True
        else:
            self.ace = False

        if 1 < self.number < 11:
            self.name = str(self.number)
        elif self.number == 1:
            self.name = "Ace"
        elif self.number == 11:
            self.name = "Jack"
            self.value = 10
        elif self.number == 12:
            self.name = "Queen"
            self.value = 10
        else:
            self.name = "King"
            self.value = 10

    def __eq__(self, other):
        if other.number == self.number and \
                other.suit == self.suit:
            return True
        else:
            return False

    def __str__(self):
        return f"{self.name} of {self.suit}"

    def genCardArt(self, shown):
        suits = {"Spades": "♠", "Diamonds": "♢", "Clubs": "♣", "Hearts": "♡"}
        if self.name != "10":
            icon = self.name[0]
            shownCard = f"""┌───────┐
│ {icon}     │
│       │
│   {suits[self.suit]}   │
│       │
│     {icon} │
└───────┘"""
        else:
            icon = self.name
            shownCard = f"""┌───────┐
│ {icon}    │
│       │
│   {suits[self.suit]}   │
│       │
│    {icon} │
└───────┘"""
        hiddenCard = """┌───────┐
│░░░░░░░│
│░░░░░░░│
│░░░░░░░│
│░░░░░░░│
│░░░░░░░│
└───────┘"""
        if shown:
            return shownCard
        if not shown:
            return hiddenCard


class Deck:
    def __init__(self, packs=1):
        self.packs = packs
        self.stack = []
        suits = ["Spades", "Diamonds", "Clubs", "Hearts"]
        for p in range(self.packs):
            for s in suits:
                for n in range(1, 14):
                    self.stack.append(Card(n, s))
        self.cards = {"Spades": [self.packs] * 13,
                      "Diamonds": [self.packs] * 13,
                      "Clubs": [self.packs] * 13,
                      "Hearts": [self.packs] * 13}

    def __str__(self):
        return str([str(c) for c in self.stack])

    def shuffle(self):
        random.shuffle(self.stack)

    def drawCard(self):
        if len(self.stack) == 0:
            raise IndexError("There are no more cards in the deck.")
        taken = self.stack.pop()
        self.cards[taken.suit][taken.number - 1] -= 1
        return taken

    def insertCard(self, card):
        if self.stack.count(card) > self.packs:
            raise ValueError(f"A card cannot occur more than {self.packs} time(s) within this deck.")
        self.stack.insert(0, card)
        self.cards[card.suit][card.number - 1] += 1

    def isComplete(self):
        suits = ["Spades", "Diamonds", "Clubs", "Hearts"]
        for s in suits:
            for n in range(13):
                if self.cards[s][n] != self.packs:
                    return False
        return True


class Hand:
    def __init__(self):
        self.cards = []
        self.shown = []

    def __str__(self):
        return str([str(c) for c in self.cards])

    def addCard(self, c, s):
        self.cards.append(c)
        self.shown.append(s)

    def takeCard(self, d, s):
        newCard = d.drawCard()
        self.cards.append(newCard)
        self.shown.append(True) if s else self.shown.append(False)

    def returnCard(self, d, c):
        i = self.cards.index(c)
        self.cards.remove(c)
        self.shown.pop(i)
        d.insertCard(c)

    def clearHand(self, d):
        for c in self.cards:
            d.insertCard(c)
        self.cards = []
        self.shown = []

    def showCards(self):
        self.shown = [True] * len(self.cards)

    def getHandValue(self):
        aces = 0
        v = 0
        for c in self.cards:
            v += c.value
            if c.ace:
                aces += 1
                v += 10
        while v > 21:
            if aces == 0:
                break
            v -= 10
            aces -= 1
        return v

    def genHandArt(self):
        cardArts = []
        for n, c in enumerate(self.cards):
            cardArts.append(c.genCardArt(self.shown[n]).split("\n"))
        art = ""
        for line in range(len(cardArts[0])):
            for c in cardArts:
                art += c[line]
                art += " "
            art += "\n" if line != len(cardArts[0]) - 1 else ""
        return art


def display(content, instructions=None):
    clear()
    lines = content.split("\n")
    screen = """                   ┏━━┓━┏┓━━━━━━━━━━┏┓━━━━━━━━━━━━━━┏┓━━
                   ┃┏┓┃━┃┃━━━━━━━━━━┃┃━━━┏┓━━━━━━━━━┃┃━━
                   ┃┗┛┗┓┃┃━┏━━┓━┏━━┓┃┃┏┓━┗┛┏━━┓━┏━━┓┃┃┏┓
                   ┃┏━┓┃┃┃━┗━┓┃━┃┏━┛┃┗┛┛━┏┓┗━┓┃━┃┏━┛┃┗┛┛
                   ┃┗━┛┃┃┗┓┃┗┛┗┓┃┗━┓┃┏┓┓━┃┃┃┗┛┗┓┃┗━┓┃┏┓┓
                   ┗━━━┛┗━┛┗━━━┛┗━━┛┗┛┗┛━┃┃┗━━━┛┗━━┛┗┛┗┛
                   ━━━━━━━━━━━━━━━━━━━━━┏┛┃━━━━━━━━━━━━━
                   ━━━━━━━━━━━━━━━━━━━━━┗━┛━━━━━━━━━━━━━
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║"""
    for line in lines:
        screen += "\n║"
        screen += line.center(75)
        screen += "║"

    screen += """\n║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝"""
    if instructions is not None:
        screen += f"\n{instructions}"
        screen += "\n> "
    print(screen, end="")


deck = Deck()
deck.shuffle()
dealerHand = Hand()
playerHand = Hand()
bank = 200

running = True
while running:
    dealerHand.clearHand(deck)
    playerHand.clearHand(deck)

    dealerHand.takeCard(deck, True)
    playerHand.takeCard(deck, True)
    dealerHand.takeCard(deck, False)
    playerHand.takeCard(deck, True)

    inGame = True
    while inGame:
        display(f"Welcome to Blackjack!\nYour current balance is: {bank}", "What is your bet on this round?")
        bet = input()
        try:
            float(bet)
        except ValueError:
            inGame = False
            break
        if float(bet) > bank:
            inGame = False
            break
        bet = float(bet)
        bank -= bet

        initial = f"""┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈
Your Balance: {bank}
┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈

Dealer's Hand:
{dealerHand.genHandArt()}

Your Hand (value: {playerHand.getHandValue()}):
{playerHand.genHandArt()}"""

        display(initial, "Would you like to (s)urrender, buy (i)nsurance, or (c)ontinue?")
        choice = input().upper()
        if choice == "S":
            display(f"You got half of your initial bet back ({bet / 2}).\n Thanks for playing, better luck next time!",
                    "Press anything to continue")
            input()
            inGame = False
            break
        elif choice == "I":
            bank -= bet
            if dealerHand.getHandValue() == 21:
                dealerHand.showCards()
                display(f"""┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈
Your Balance: {bank} (+ {bet * 2})
┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈

Dealer's Hand (value: {dealerHand.getHandValue()}):
{dealerHand.genHandArt()}

░██▄░█▒░▒▄▀▄░▄▀▀░█▄▀░░▒█▒▄▀▄░▄▀▀░█▄▀░█
▒█▄█▒█▄▄░█▀█░▀▄▄░█▒█░▀▄█░█▀█░▀▄▄░█▒█░▄
Because you bought insurance, you get all your money back.""", "Press enter to continue")
                input()
                bank += bet * 2
                inGame = False
                break
            else:
                display("The dealer's hand was not 21.\nYou lost your insurance money!", "Press enter to continue")
                input()

        playing = True
        while playing:
            table = f"""┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈
Your Balance: {bank}
┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈

Dealer's Hand:
{dealerHand.genHandArt()}

Your Hand (value: {playerHand.getHandValue()}):
{playerHand.genHandArt()}"""
            display(table, "Would you like to (h)it or (s)tand?")
            choice = input().upper()
            if choice == "H":
                playerHand.takeCard(deck, True)
                if playerHand.getHandValue() > 21:
                    dealerHand.showCards()
                    table = f"""┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈
Your Balance: {bank}
┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈

Dealer's Hand (value: {dealerHand.getHandValue()}):
{dealerHand.genHandArt()}

Your Hand (value: {playerHand.getHandValue()}):
{playerHand.genHandArt()}

▄▄▄▄· ▄• ▄▌.▄▄ · ▄▄▄▄▄▄      
▐█ ▀█▪█▪██▌▐█ ▀. ▀•██ ▀      
▐█▀▀█▄█▌▐█▌▄▀▀▀█▄  ▐█.▪      
██▄▪▐█▐█▄█▌▐█▄▪▐█  ▐█▌·      
·▀▀▀▀  ▀▀▀  ▀▀▀▀   ▀▀▀ ▀ ▀ ▀ 

Better luck next time!"""
                    display(table, "Press enter to continue")
                    input()
                    playing = False
                    inGame = False
                    break
                elif playerHand.getHandValue() == 21:
                    table = f"""┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈
Your Balance: {bank}
┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈

Dealer's Hand (value: {dealerHand.getHandValue()}):
{dealerHand.genHandArt()}

Your Hand (value: {playerHand.getHandValue()}):
{playerHand.genHandArt()}

░██▄░█▒░▒▄▀▄░▄▀▀░█▄▀░░▒█▒▄▀▄░▄▀▀░█▄▀░█
▒█▄█▒█▄▄░█▀█░▀▄▄░█▒█░▀▄█░█▀█░▀▄▄░█▒█░▄"""
                    display(table)
                    time.sleep(1)
                    dealerHand.showCards()
                    if dealerHand.getHandValue() != 21:
                        table = f"""┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈
Your Balance: {bank} (+ {bet * 1.5})
┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈

Dealer's Hand (value: {dealerHand.getHandValue()}):
{dealerHand.genHandArt()}

Your Hand (value: {playerHand.getHandValue()}):
{playerHand.genHandArt()}

░██▄░█▒░▒▄▀▄░▄▀▀░█▄▀░░▒█▒▄▀▄░▄▀▀░█▄▀░█
▒█▄█▒█▄▄░█▀█░▀▄▄░█▒█░▀▄█░█▀█░▀▄▄░█▒█░▄

CONGRATULATIONS! You won this round! You won {bet * 1.5}"""
                        bank += bet * 1.5
                        display(table, "Press enter to continue")
                        input()
                        playing = False
                        inGame = False
                        break
                    else:
                        table = f"""┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈
Your Balance: {bank} (+ {bet})
┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈

Dealer's Hand (value: {dealerHand.getHandValue()}):
{dealerHand.genHandArt()}

Your Hand (value: {playerHand.getHandValue()}):
{playerHand.genHandArt()}

░██▄░█▒░▒▄▀▄░▄▀▀░█▄▀░░▒█▒▄▀▄░▄▀▀░█▄▀░█
▒█▄█▒█▄▄░█▀█░▀▄▄░█▒█░▀▄█░█▀█░▀▄▄░█▒█░▄

It's a tie! Both you and the dealer got Blackjack!
Your bet has been returned."""
                        bank += bet
                        display(table, "Press enter to continue")
                        input()
                        playing = False
                        inGame = False
                        break
            else:
                dealerHand.showCards()
                while dealerHand.getHandValue() < 17:
                    table = f"""┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈
Your Balance: {bank}
┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈

Dealer's Hand (value: {dealerHand.getHandValue()}):
{dealerHand.genHandArt()}

Your Hand (value: {playerHand.getHandValue()}):
{playerHand.genHandArt()}"""
                    display(table)
                    time.sleep(1.5)
                    dealerHand.takeCard(deck, True)
                    if dealerHand.getHandValue() > 21:
                        table = f"""┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈
Your Balance: {bank} (+ {bet * 1.5})
┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈

Dealer's Hand (value: {dealerHand.getHandValue()}):
{dealerHand.genHandArt()}

Your Hand (value: {playerHand.getHandValue()}):
{playerHand.genHandArt()}

░▒█░░▒█░▒█▀▀▀█░▒█░▒█░░░▒█░░▒█░▀█▀░▒█▄░▒█░█
░▒▀▄▄▄▀░▒█░░▒█░▒█░▒█░░░▒█▒█▒█░▒█░░▒█▒█▒█░▀
░░░▒█░░░▒█▄▄▄█░░▀▄▄▀░░░▒▀▄▀▄▀░▄█▄░▒█░░▀█░▄

The dealer busted, so you've won this round! Good job!"""
                        display(table, "Press enter to continue")
                        input()
                        bank += bet * 1.5
                        playing = False
                        inGame = False
                        break
                if playerHand.getHandValue() < dealerHand.getHandValue() <= 21:
                    table = f"""┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈
Your Balance: {bank}
┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈

Dealer's Hand (value: {dealerHand.getHandValue()}):
{dealerHand.genHandArt()}

Your Hand (value: {playerHand.getHandValue()}):
{playerHand.genHandArt()}

░▒█░░▒█░▄▀▀▄░█░▒█░░░█░░▄▀▀▄░█▀▀░█▀▀░░░░░░░░░
░▒▀▄▄▄▀░█░░█░█░▒█░░░█░░█░░█░▀▀▄░█▀▀░▄▄░▄▄░▄▄
░░░▒█░░░░▀▀░░░▀▀▀░░░▀▀░░▀▀░░▀▀▀░▀▀▀░▀▀░▀▀░▀▀

The dealer has a better hand. Too bad!
Better luck next time!"""
                    display(table, "Press enter to continue")
                    input()
                    playing = False
                    inGame = False
                    break
                elif 21 >= playerHand.getHandValue() > dealerHand.getHandValue():
                    table = f"""┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈
Your Balance: {bank} (+ {bet * 1.5})
┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈

Dealer's Hand (value: {dealerHand.getHandValue()}):
{dealerHand.genHandArt()}

Your Hand (value: {playerHand.getHandValue()}):
{playerHand.genHandArt()}

░▒█░░▒█░▒█▀▀▀█░▒█░▒█░░░▒█░░▒█░▀█▀░▒█▄░▒█░█
░▒▀▄▄▄▀░▒█░░▒█░▒█░▒█░░░▒█▒█▒█░▒█░░▒█▒█▒█░▀
░░░▒█░░░▒█▄▄▄█░░▀▄▄▀░░░▒▀▄▀▄▀░▄█▄░▒█░░▀█░▄

You win! Your hand was better than the dealer!"""
                    display(table, "Press enter to continue")
                    input()
                    bank += bet * 1.5
                    playing = False
                    inGame = False
                    break
                elif playerHand.getHandValue() == dealerHand.getHandValue():
                    table = f"""┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈
Your Balance: {bank} (+ {bet})
┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈

Dealer's Hand (value: {dealerHand.getHandValue()}):
{dealerHand.genHandArt()}

Your Hand (value: {playerHand.getHandValue()}):
{playerHand.genHandArt()}

__ __|_)        |
   |   |   _ \  |
   |   |   __/ _|
  _|  _| \___| _)

Tie game! You and the dealer had the same hand. 
Your bet has been returned to you."""
                    display(table, "Press enter to continue")
                    input()
                    bank += bet
                    playing = False
                    inGame = False
                    break
