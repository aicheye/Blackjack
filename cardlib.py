import random


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
        self.shown = []

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
        for n, c in enumerate(self.cards):
            if not self.shown[n]:
                self.shown[n] = True
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
