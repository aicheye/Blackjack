import libs.cards as cards
import libs.ui as ui

ui.load()


def begin():
    deck = cards.Deck()
    deck.shuffle()
    dealerHand = cards.Hand()
    playerHand = cards.Hand()

    dealerHand.clear_hand(deck)
    playerHand.clear_hand(deck)

    dealerHand.take_card(deck, True)
    playerHand.take_card(deck, True)
    dealerHand.take_card(deck, False)
    playerHand.take_card(deck, True)

    ui.display("""Welcome to the tutorial!
or SKIP if you already know how to play Blackjack""", ui.prompt_TutorialStart)
    choice = ui.user_selected[0]
    if choice == "S":
        return
    ui.display("Here, you will learn the basics of Blackjack.", ui.prompt_Dismiss)
    ui.display("""In Blackjack, each hand is assigned a value 
based on the sum of its cards values.

You will learn what a hand is later.""", ui.prompt_Dismiss)
    ui.display("""The value of each card is as follows:

for number cards (2-10), the face value,

the value of all royal cards is 10,

and the value of an ace is either 1 or 11, 
whichever is better.""", ui.prompt_Dismiss)
    demoHand = cards.Hand()
    demoHand.take_card(deck, True)
    demoHand.take_card(deck, True)
    ui.display(f"""Can you guess what the sum of this hand is?

{demoHand.gen_art()}""", "Enter the value:")
    if ui.user_in == str(demoHand.get_hand_value()):
        ui.display("""That's correct!
Good job!""", ui.prompt_Dismiss)
    else:
        ui.display("""That's not quite right.
Don't worry, you'll get better.""", ui.prompt_Dismiss)
    ui.display("""Ultimately, the goal of a Blackjack game is to have 
a hand so that this sum is close to but NOT OVER 21""", ui.prompt_Dismiss)
    ui.display(f"""The first part of a Blackjack game is the deal. 
Both you and the dealer will receive two cards.
These cards are called the hand.

You can only see one of the dealer's cards:

Dealer's Hand:
{dealerHand.gen_art()}

Your Hand (value: {playerHand.get_hand_value()}):
{playerHand.gen_art()}""", ui.prompt_Dismiss)
    ui.display(f"""After the first deal, you will be asked to either:
surrender (give up for half of your bet),
buy insurance (if the dealer has blackjack),
double down (double your bet),
or continue the game

*insurance is only an option if 
the dealer's first card is an ace

Try it out below!

Dealer's Hand:
{dealerHand.gen_art()}

Your Hand (value: {playerHand.get_hand_value()}):
{playerHand.gen_art()}""", (ui.prompt_InitialWithInsurance if dealerHand.cards[0].ace else ui.prompt_Initial))
    ui.display(f"""You chose to {ui.user_selected}.""", ui.prompt_Dismiss)
    ui.display("""After this initial choice, the game gets rolling!""", ui.prompt_Dismiss)
    ui.display("""You can either choose to hit (gain one card) 
or stand (keep your current hand)

There are two ways you can lose:
1. Your hand goes above 21 (a BUST)
2. The dealer has a better hand

There are two ways you can win:
1. The dealer's hand goes above 21 (a BUST)
2. You have a better hand

There is one way you can tie:
1. Both you and the dealer have equal hands.""", ui.prompt_Dismiss)
    ui.display(f"""A basic strategy is to: hit when your hand is less than 17,
and stand when your hand is at least 17

What should you do with this hand?

Dealer's Hand:
{dealerHand.gen_art()}

Your Hand (value: {playerHand.get_hand_value()}):
{playerHand.gen_art()}""", ui.prompt_Default)
    choice = ui.user_selected[0]
    if playerHand.get_hand_value() >= 17 and choice == "S":
        ui.display("Nice! That's right! Usually, you should stand in this situation.", ui.prompt_Dismiss)
    elif playerHand.get_hand_value() < 17 and choice == "H":
        ui.display("Good job! Hitting with this hand is a smart choice.", ui.prompt_Dismiss)
    else:
        ui.display("""Unless you really know what you're doing, 
you shouldn't make that move.""", ui.prompt_Dismiss)
    ui.display("""After you have finished hitting,
the dealer will make moves automatically.""", ui.prompt_Dismiss)
    ui.display("""At the end of the game, whoever has the higher hand
WITHOUT going over 21, wins the bet.""", ui.prompt_Dismiss)
    ui.display("""You're now ready to play the game! 
Continue whenever you're ready.""", ui.prompt_Dismiss)
