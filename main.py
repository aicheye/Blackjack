import time
import cardlib
import ui
import json


def updateData():
    global bank
    global bet
    with open("data.json", "w") as write_file:
        json.dump({"bank": bank, "bet": bet}, write_file, indent=2)
    ui.refresh()


def updateHands():
    global dealerHand
    global playerHand
    with open("hands.json", "w") as write_file:
        json.dump(
            {
                "dealerHand":
                    {
                        "art": dealerHand.genHandArt(),
                        "value": dealerHand.getHandValue()
                    },
                "playerHand":
                    {
                        "art": playerHand.genHandArt(),
                        "value": playerHand.getHandValue()
                    }
            },
            write_file,
            indent=2
        )
    ui.refresh()


deck = cardlib.Deck()
deck.shuffle()
dealerHand = cardlib.Hand()
playerHand = cardlib.Hand()
bank = 10_000
bet = 0

updateData()

running = True
while running:
    if bank == 0:
        ui.display(ui.broke)
        running = False
        break

    dealerHand.clearHand(deck)
    playerHand.clearHand(deck)

    dealerHand.takeCard(deck, True)
    playerHand.takeCard(deck, True)
    dealerHand.takeCard(deck, False)
    playerHand.takeCard(deck, True)

    updateHands()

    inGame = True
    while inGame:
        if bank == 0:
            inGame = False
            playing = False
            break
        ui.display(ui.welcome, "What is your bet on this round?")
        bet = input()
        try:
            float(bet)
        except ValueError:
            inGame = False
            break
        if float(bet) > bank or float(bet) < 0:
            inGame = False
            break
        bet = float(bet)
        updateData()

        if bet == bank > 0:
            ui.display(ui.alert_AllIn, "Press enter to continue")
            input()

        bank -= bet
        updateData()

        ui.display(ui.table_Default, "Would you like to (s)urrender, buy (i)nsurance, (d)ouble down or (c)ontinue?")
        choice = input().upper()
        while choice != "S" and choice != "I" and choice != "D" and choice != "C":
            ui.display(ui.table_Default, "Would you like to (s)urrender, buy (i)nsurance, (d)ouble down or (c)ontinue?")
            choice = input().upper()
        if choice == "S":
            ui.display(ui.alert_Surrender, "Press enter to continue")
            input()
            bank += bet / 2
            updateData()
            inGame = False
            break
        elif choice == "I":
            bank -= bet
            if dealerHand.getHandValue() == 21:
                dealerHand.showCards()
                updateHands()
                ui.display(ui.alert_InsuranceSucceeded, "Press enter to continue")
                input()
                bank += bet * 2
                updateData()
                inGame = False
                break
            else:
                ui.display(ui.alert_InsuranceFailed, "Press enter to continue")
                input()
        elif choice == "D":
            if bank > bet:
                ui.display(ui.alert_DoubleDown, "Press enter to continue")
                bank -= bet
                bet *= 2
                updateData()
                input()
            elif 0 < bank <= bet:
                ui.display(ui.alert_DoubleDownAllIn, "Press enter to continue")
                bank -= 0
                bet += bank
                updateData()
                input()
            else:
                ui.display(ui.alert_DoubleDownImpossible, "Press enter to continue")
                input()
        playing = True
        while playing:
            ui.display(ui.table_Default, "Would you like to (h)it or (s)tand?")
            choice = input().upper()
            while choice != "H" and choice != "S":
                ui.display(ui.table_Default, "Would you like to (h)it or (s)tand?")
                choice = input().upper()
            if choice == "H":
                playerHand.takeCard(deck, True)
                updateHands()
                if playerHand.getHandValue() > 21:
                    dealerHand.showCards()
                    updateHands()
                    ui.display(ui.loss_PlayerBusted, "Press enter to continue")
                    input()
                    playing = False
                    inGame = False
                    break
                elif playerHand.getHandValue() == 21:
                    ui.display(ui.table_PlayerBlackjack)
                    time.sleep(2)
                    dealerHand.showCards()
                    updateHands()
                    if dealerHand.getHandValue() != 21:
                        bank += bet * 1.5
                        updateData()
                        ui.display(ui.win_PlayerBlackjack, "Press enter to continue")
                        input()
                        playing = False
                        inGame = False
                        break
                    else:
                        bank += bet
                        updateData()
                        ui.display(ui.tie_PlayerBlackjack, "Press enter to continue")
                        input()
                        playing = False
                        inGame = False
                        break
            else:
                dealerHand.showCards()
                updateHands()
                while dealerHand.getHandValue() < 17:
                    ui.display(ui.table_DealerShown)
                    time.sleep(2)
                    dealerHand.takeCard(deck, True)
                    updateHands()
                    if dealerHand.getHandValue() > 21:
                        ui.display(ui.win_DealerBusted, "Press enter to continue")
                        input()
                        bank += bet * 1.5
                        updateData()
                        playing = False
                        inGame = False
                        break
                if playerHand.getHandValue() < dealerHand.getHandValue() <= 21:
                    ui.display(ui.loss_PlayerWorseHand, "Press enter to continue")
                    input()
                    playing = False
                    inGame = False
                    break
                elif 21 >= playerHand.getHandValue() > dealerHand.getHandValue():
                    ui.display(ui.win_PlayerBetterHand, "Press enter to continue")
                    input()
                    bank += bet * 1.5
                    updateData()
                    playing = False
                    inGame = False
                    break
                elif playerHand.getHandValue() == dealerHand.getHandValue():
                    ui.display(ui.tie_SameHand, "Press enter to continue")
                    input()
                    bank += bet
                    updateData()
                    playing = False
                    inGame = False
                    break
