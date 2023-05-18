import time
import cards
import ui
import json
import os
import tutorial

size = os.get_terminal_size()
cols = size.columns

with open("sys.json", "w") as write_file:
    json.dump({"cols": cols}, write_file, indent=2)

ui.load()

tutorial.begin()


def update_data():
    global bank
    global bet
    with open("data.json", "w") as write_file:
        json.dump({"bank": bank, "bet": bet}, write_file, indent=2)
    ui.refresh()


def update_hands():
    global dealerHand
    global playerHand
    with open("hands.json", "w") as write_file:
        json.dump(
            {
                "dealerHand":
                    {
                        "art": dealerHand.gen_art(),
                        "value": dealerHand.get_hand_value()
                    },
                "playerHand":
                    {
                        "art": playerHand.gen_art(),
                        "value": playerHand.get_hand_value()
                    }
            },
            write_file,
            indent=2
        )
    ui.refresh()


if __name__ == "__main__":
    deck = cards.Deck()
    deck.shuffle()
    dealerHand = cards.Hand()
    playerHand = cards.Hand()
    bank = 10_000
    bet = 0

    update_data()

    running = True
    while running:
        if bank == 0:
            ui.display(ui.broke)
            running = False
            break

        dealerHand.clear_hand(deck)
        playerHand.clear_hand(deck)

        dealerHand.take_card(deck, True)
        playerHand.take_card(deck, True)
        dealerHand.take_card(deck, False)
        playerHand.take_card(deck, True)

        update_hands()

        inGame = True
        while inGame:
            if bank == 0:
                inGame = False
                playing = False
                break
            ui.display(ui.welcome, ui.prompt_Bet)
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
            update_data()

            if bet == bank > 0:
                ui.display(ui.alert_AllIn, ui.prompt_Dismiss)

            bank -= bet
            update_data()

            if not dealerHand.cards[0].ace:
                ui.display(ui.table_Default, ui.prompt_Initial)
                choice = ui.selected[0]
            else:
                ui.display(ui.table_Default, ui.prompt_InitialWithInsurance)
                choice = ui.selected[0]
            if choice == "S":
                ui.display(ui.alert_Surrender, ui.prompt_Dismiss)
                bank += bet / 2
                update_data()
                inGame = False
                break
            elif choice == "B":
                bank -= bet
                update_data()
                if dealerHand.get_hand_value() == 21:
                    dealerHand.show_cards()
                    update_hands()
                    ui.display(ui.alert_InsuranceSucceeded, ui.prompt_Dismiss)
                    bank += bet * 2
                    update_data()
                    inGame = False
                    break
                else:
                    ui.display(ui.alert_InsuranceFailed, ui.prompt_Dismiss)
            elif choice == "D":
                if bank > bet:
                    ui.display(ui.alert_DoubleDown, ui.prompt_Dismiss)
                    bank -= bet
                    bet *= 2
                    update_data()
                elif bank == bet:
                    ui.display(ui.alert_DoubleDownAllIn, ui.prompt_Dismiss)
                    bank = 0
                    bet *= 2
                    update_data()
                else:
                    ui.display(ui.alert_DoubleDownFailed, ui.prompt_Dismiss)
            playing = True
            while playing:
                ui.display(ui.table_Default, ui.prompt_Default)
                choice = ui.selected[0]
                if choice == "H":
                    playerHand.take_card(deck, True)
                    update_hands()
                    if playerHand.get_hand_value() > 21:
                        dealerHand.show_cards()
                        update_hands()
                        ui.display(ui.loss_PlayerBusted, ui.prompt_Dismiss)
                        playing = False
                        inGame = False
                        break
                    elif playerHand.get_hand_value() == 21:
                        ui.display(ui.table_PlayerBlackjack)
                        time.sleep(2)
                        dealerHand.show_cards()
                        update_hands()
                        if dealerHand.get_hand_value() != 21:
                            bank += bet * 1.5
                            update_data()
                            ui.display(ui.win_PlayerBlackjack, ui.prompt_Dismiss)
                            playing = False
                            inGame = False
                            break
                        else:
                            bank += bet
                            update_data()
                            ui.display(ui.tie_PlayerBlackjack, ui.prompt_Dismiss)
                            playing = False
                            inGame = False
                            break
                else:
                    dealerHand.show_cards()
                    update_hands()
                    while dealerHand.get_hand_value() < 17:
                        ui.display(ui.table_DealerShown)
                        time.sleep(2)
                        dealerHand.take_card(deck, True)
                        update_hands()
                        if dealerHand.get_hand_value() > 21:
                            ui.display(ui.win_DealerBusted, ui.prompt_Dismiss)
                            bank += bet * 1.5
                            update_data()
                            playing = False
                            inGame = False
                            break
                    if playerHand.get_hand_value() < dealerHand.get_hand_value() <= 21:
                        ui.display(ui.loss_PlayerWorseHand, ui.prompt_Dismiss)
                        playing = False
                        inGame = False
                        break
                    elif 21 >= playerHand.get_hand_value() > dealerHand.get_hand_value():
                        ui.display(ui.win_PlayerBetterHand, ui.prompt_Dismiss)
                        bank += bet * 1.5
                        update_data()
                        playing = False
                        inGame = False
                        break
                    elif playerHand.get_hand_value() == dealerHand.get_hand_value():
                        ui.display(ui.tie_SameHand, ui.prompt_Dismiss)
                        bank += bet
                        update_data()
                        playing = False
                        inGame = False
                        break
