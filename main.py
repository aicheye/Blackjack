import time
import libs.cards as cards
import libs.ui as ui
import json
import os
import tutorial

size = os.get_terminal_size()
cols = size.columns


def load_json():
    with open("data.json", "w") as write_file:
        json.dump(
            {
                "cols": cols,
                "bank": 10_000,
                "bet": 0,
                "dealerHand":
                    {
                        "art": "",
                        "value": 0
                    },
                "playerHand":
                    {
                        "art": "",
                        "value": 0
                    },
                "profit": 0,
                "wins": 0,
                "losses": 0
            },
            write_file,
            indent=2
        )
    ui.refresh()


def update():
    with open("data.json", "w") as write_file:
        json.dump(
            {
                "cols": cols,
                "bank": bank,
                "bet": bet,
                "dealerHand":
                    {
                        "art": dealerHand.gen_art(),
                        "value": dealerHand.get_hand_value()
                    },
                "playerHand":
                    {
                        "art": playerHand.gen_art(),
                        "value": playerHand.get_hand_value()
                    },
                "profit": stats["profit"],
                "wins": stats["wins"],
                "losses": stats["losses"]
            },
            write_file,
            indent=2
        )
    ui.refresh()


load_json()
ui.load()
tutorial.begin()

stats = {"profit": 0, "wins": 0, "losses": 0}

bank = 10_000
bet = 0
dealerHand = cards.Hand()
playerHand = cards.Hand()

update()

global deck, rounds, running, in_game, in_round


def take_bets():
    global bank, bet, in_game, in_round

    if bank == 0:
        in_game = False
        return
    ui.display(ui.welcome, ui.prompt_Bet)
    bet = ui.user_in

    try:
        float(bet)
    except ValueError:
        if "k" in bet:
            bet = float(bet[:-1]) * 1_000
        elif bet == "all":
            bet = bank
        else:
            take_bets()
            return

    if float(bet) > bank or float(bet) <= 0:
        take_bets()
        return
    bet = float(bet)
    update()

    if bet == bank > 0:
        ui.display(ui.alert_AllIn, ui.prompt_Dismiss)

    bank -= bet
    update()


def initial_choice():
    global bank, bet, in_game, dealerHand, playerHand, in_round

    if not dealerHand.cards[0].ace:
        ui.display(ui.table_Default, ui.prompt_Initial)
        choice = ui.user_selected[0]
    else:
        ui.display(ui.table_Default, ui.prompt_InitialWithInsurance)
        choice = ui.user_selected[0]
    if choice == "S":
        ui.display(ui.alert_Surrender, ui.prompt_Dismiss)
        bank += (bet * 100) // 2 / 100
        update()
        in_game = False
        in_round = False
        return
    elif choice == "B":
        bank -= bet
        update()
        if dealerHand.get_hand_value() == 21:
            dealerHand.show_cards()
            update()
            ui.display(ui.alert_InsuranceSucceeded, ui.prompt_Dismiss)
            bank += bet * 2
            update()
            in_game = False
            in_round = False
            return
        else:
            ui.display(ui.alert_InsuranceFailed, ui.prompt_Dismiss)
    elif choice == "D":
        if bank > bet:
            ui.display(ui.alert_DoubleDown, ui.prompt_Dismiss)
            bank -= bet
            bet *= 2
            update()
        elif bank == bet:
            ui.display(ui.alert_DoubleDownAllIn, ui.prompt_Dismiss)
            bank = 0
            bet *= 2
            update()
        else:
            ui.display(ui.alert_DoubleDownFailed, ui.prompt_Dismiss)
            initial_choice()
            return


def deposit():
    global rounds, running

    ui.display(ui.deposit, ui.prompt_Deposit)
    choice = ui.user_selected[0]
    if choice == "D":
        main()
    elif choice == "E":
        ui.display(ui.stats_final, ui.prompt_Exit)
        choice = ui.user_selected[0]
        if choice == "E":
            running = False
            return "exit"
        elif choice == "B":
            deposit()


def new_round():
    global bank, bet, in_game, deck, dealerHand, playerHand, stats, in_round

    in_round = True

    take_bets()
    initial_choice()

    while in_round:
        ui.display(ui.table_Default, ui.prompt_Default)
        choice = ui.user_selected[0]
        if choice == "H":
            playerHand.take_card(deck, True)
            update()
            if playerHand.get_hand_value() > 21:
                dealerHand.show_cards()
                update()
                ui.display(ui.loss_PlayerBusted, ui.prompt_Dismiss)
                stats["losses"] += 1
                update()
                in_round = False
                in_game = False
                break
            elif playerHand.get_hand_value() == 21:
                ui.display(ui.table_PlayerBlackjack)
                time.sleep(2)
                dealerHand.show_cards()
                update()
                if dealerHand.get_hand_value() != 21:
                    bank += bet * 2
                    update()
                    ui.display(ui.win_PlayerBlackjack, ui.prompt_Dismiss)
                    stats["wins"] += 1
                    update()
                    in_round = False
                    in_game = False
                    break
                else:
                    bank += bet
                    update()
                    ui.display(ui.tie_SameBlackjack, ui.prompt_Dismiss)
                    in_round = False
                    in_game = False
                    break
        else:
            dealerHand.show_cards()
            update()
            while dealerHand.get_hand_value() < 17:
                ui.display(ui.table_DealerShown)
                time.sleep(2)
                dealerHand.take_card(deck, True)
                update()
                if dealerHand.get_hand_value() > 21:
                    ui.display(ui.win_DealerBusted, ui.prompt_Dismiss)
                    stats["wins"] += 1
                    update()
                    bank += bet * 2
                    update()
                    in_round = False
                    in_game = False
                    break
            if playerHand.get_hand_value() < dealerHand.get_hand_value() <= 21:
                ui.display(ui.loss_PlayerWorseHand, ui.prompt_Dismiss)
                stats["losses"] += 1
                update()
                in_round = False
                in_game = False
                break
            elif 21 >= playerHand.get_hand_value() > dealerHand.get_hand_value():
                ui.display(ui.win_PlayerBetterHand, ui.prompt_Dismiss)
                stats["wins"] += 1
                update()
                bank += bet * 2
                update()
                in_round = False
                in_game = False
                break
            elif playerHand.get_hand_value() == dealerHand.get_hand_value():
                ui.display(ui.tie_SameHand, ui.prompt_Dismiss)
                bank += bet
                update()
                in_round = False
                in_game = False
                break


def main():
    global bank, running, bet, deck, dealerHand, playerHand, in_game, rounds, stats

    deck = cards.Deck()
    deck.shuffle()
    dealerHand = cards.Hand()
    playerHand = cards.Hand()
    bank = 10_000
    bet = 0
    disabledTimer = 0
    rounds = 0

    update()
    stop = False
    if not stop:
        running = True
    while running:
        if bank == 0:
            stats["profit"] -= 10_000
            update()
            ui.display(ui.broke, ui.prompt_Dismiss)
            if deposit() == "exit":
                running = False
                stop = True
                break

        if rounds > 0 and (disabledTimer == 0 or disabledTimer > 4):
            ui.display(ui.cash_out, ui.prompt_CashOut)
            choice = ui.user_selected[1]
            if choice == "A":
                stats["profit"] += bank - 10_000
                update()
                if deposit() == "exit":
                    running = False
                    stop = True
                    break
            elif choice == "I":
                disabledTimer = 1

        rounds += 1

        if disabledTimer >= 1:
            disabledTimer += 1

        dealerHand.clear_hand(deck)
        playerHand.clear_hand(deck)

        dealerHand.take_card(deck, True)
        playerHand.take_card(deck, True)
        dealerHand.take_card(deck, False)
        playerHand.take_card(deck, True)

        update()

        in_game = True
        while in_game:
            new_round()


if __name__ == "__main__":
    main()
