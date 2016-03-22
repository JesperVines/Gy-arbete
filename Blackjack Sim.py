import random

'''
Gymnasieprogram "Blackjack simulering"

This is a blackjack simulation. KappaRoss.

Reglerna som används i detta spel är följande:

Delaren (huset) spelar på allt som är lägre än sjutton. Så om delaren efter de två första korten har en sammanlagd
poäng av 16 eller lägre, kommer den ta ett till kort. Om den nya summan fortfarande är lägre än sjutton, tas ett till
kort osv. Vi använder oss också, för enkelhetens skull, av så kallad "hård" sjutton. Detta betyder att även om delaren
skulle kunna omvandla ett ess från elva poäng till ett, och därigenom få en summa lägre än sjutton, gör den inte det
utan står över ett till kort.

För att ändra spelarens algoritmer, och därigenom kunna studer vilket arbetssätt som är det optimala, ändrar man koden
i "bot_turn". Detta kommer ändra hur spelaren spelar men ingenting annat. Förhoppningsvis.

Vi som gjort detta är:

Kod och gnäll: Jesper Vines
Moralisk support: Emil Strömblad
Faktiskt arbete: Johan Widmark

(ditto) We (ditto) want (ditto) to (ditto) party (ditto)

Placera ytterligare fuktiga mejmejs här:

'''


def deck():

        deck_cards = []

        card = ["Ace of spades", 11]
        deck_cards.append(card)
        card = ["2 of spades", 2]
        deck_cards.append(card)
        card = ["3 of spades", 3]
        deck_cards.append(card)
        card = ["4 of spades", 4]
        deck_cards.append(card)
        card = ["5 of spades", 5]
        deck_cards.append(card)
        card = ["6 of spades", 6]
        deck_cards.append(card)
        card = ["7 of spades", 7]
        deck_cards.append(card)
        card = ["9 of spades", 8]
        deck_cards.append(card)
        card = ["9 of spades", 9]
        deck_cards.append(card)
        card = ["10 of spades", 10]
        deck_cards.append(card)
        card = ["Jack of spades", 10]
        deck_cards.append(card)
        card = ["Queen of spades", 10]
        deck_cards.append(card)
        card = ["King of spades", 10]
        deck_cards.append(card)
        card = ["Ace of hearts", 11]
        deck_cards.append(card)
        card = ["2 of hearts", 2]
        deck_cards.append(card)
        card = ["3 of hearts", 3]
        deck_cards.append(card)
        card = ["4 of hearts", 4]
        deck_cards.append(card)
        card = ["5 of hearts", 5]
        deck_cards.append(card)
        card = ["6 of hearts", 6]
        deck_cards.append(card)
        card = ["7 of hearts", 7]
        deck_cards.append(card)
        card = ["9 of hearts", 8]
        deck_cards.append(card)
        card = ["9 of hearts", 9]
        deck_cards.append(card)
        card = ["10 of hearts", 10]
        deck_cards.append(card)
        card = ["Jack of hearts", 10]
        deck_cards.append(card)
        card = ["Queen of hearts", 10]
        deck_cards.append(card)
        card = ["King of hearts", 10]
        deck_cards.append(card)
        card = ["Ace of clubs", 11]
        deck_cards.append(card)
        card = ["2 of clubs", 2]
        deck_cards.append(card)
        card = ["3 of clubs", 3]
        deck_cards.append(card)
        card = ["4 of clubs", 4]
        deck_cards.append(card)
        card = ["5 of clubs", 5]
        deck_cards.append(card)
        card = ["6 of clubs", 6]
        deck_cards.append(card)
        card = ["7 of clubs", 7]
        deck_cards.append(card)
        card = ["9 of clubs", 8]
        deck_cards.append(card)
        card = ["9 of clubs", 9]
        deck_cards.append(card)
        card = ["10 of clubs", 10]
        deck_cards.append(card)
        card = ["Jack of clubs", 10]
        deck_cards.append(card)
        card = ["Queen of clubs", 10]
        deck_cards.append(card)
        card = ["King of clubs", 10]
        deck_cards.append(card)
        card = ["Ace of diamonds", 11]
        deck_cards.append(card)
        card = ["2 of diamonds", 2]
        deck_cards.append(card)
        card = ["3 of diamonds", 3]
        deck_cards.append(card)
        card = ["4 of diamonds", 4]
        deck_cards.append(card)
        card = ["5 of diamonds", 5]
        deck_cards.append(card)
        card = ["6 of diamonds", 6]
        deck_cards.append(card)
        card = ["7 of diamonds", 7]
        deck_cards.append(card)
        card = ["9 of diamonds", 8]
        deck_cards.append(card)
        card = ["9 of diamonds", 9]
        deck_cards.append(card)
        card = ["10 of diamonds", 10]
        deck_cards.append(card)
        card = ["Jack of diamonds", 10]
        deck_cards.append(card)
        card = ["Queen of diamonds", 10]
        deck_cards.append(card)
        card = ["King of diamonds", 10]
        deck_cards.append(card)

        return deck_cards


def first_deal():

    new_deck1 = deck()
    new_dealer1 = 0
    ace_dealer1 = 0
    new_hand1 = 0
    ace_hand1 = 0

    card_h = random.choice(new_deck1)

    if card_h[1] == 11:
        ace_hand1 += 1

    new_hand1 += card_h[1]

    if ace_hand1 > 0:

        if new_hand1 > 21:

            while new_hand1 > 21:
                new_hand1 -= 10
                ace_hand1 -= 1

    new_deck1.remove(card_h)

    card_d = random.choice(new_deck1)

    if card_d[1] == 11:
        ace_dealer1 += 1

    new_dealer1 += card_d[1]

    if ace_dealer1 > 0:

        if new_dealer1 > 21:

            while new_dealer1 > 21:
                new_dealer1 -= 10
                ace_dealer1 -= 1

    new_deck1.remove(card_d)

    card_h = random.choice(new_deck1)

    if card_h[1] == 11:
        ace_hand1 += 1

    new_hand1 += card_h[1]

    if ace_hand1 > 0:

        if new_hand1 > 21:

            while new_hand1 > 21:
                new_hand1 -= 10
                ace_hand1 -= 1

    new_deck1.remove(card_h)

    return new_deck1, new_hand1, ace_hand1, new_dealer1, ace_dealer1


def bot_turn(new_deck1, new_hand1, ace_hand1, new_dealer1, ace_dealer1):

    new_deck2 = new_deck1
    new_hand2 = new_hand1
    ace_hand2 = ace_hand1
    new_dealer2 = new_dealer1
    ace_dealer2 = ace_dealer1

    while new_hand2 <= 17:

        card_h = random.choice(new_deck2)

        if card_h[1] == 11:
            ace_hand2 += 1

        new_hand2 += card_h[1]

        if ace_hand2 > 0:

            if new_hand2 > 21:

                while new_hand2 > 21:
                    new_hand2 -= 10
                    ace_hand2 -= 1

        new_deck2.remove(card_h)

    return new_deck2, new_hand2, ace_hand2, new_dealer2, ace_dealer2


def dealer_turn(new_deck2, new_hand2, ace_hand2, new_dealer2, ace_dealer2):

    new_deck3 = new_deck2
    new_hand3 = new_hand2
    ace_hand3 = ace_hand2
    new_dealer3 = new_dealer2
    ace_dealer3 = ace_dealer2

    while new_dealer3 <= 16:

        card_d = random.choice(new_deck3)

        if card_d[1] == 11:
            ace_dealer3 += 1

        new_dealer3 += card_d[1]

        if ace_dealer3 > 0:

            if new_dealer3 > 21:

                while new_dealer3 > 21:
                    new_dealer3 -= 10
                    ace_dealer3 -= 1

        new_deck3.remove(card_d)

    return new_deck3, new_hand3, ace_hand3, new_dealer3, ace_dealer3


def main():

    player_wins = 0
    dealer_wins = 0
    draws = 0
    plays = 0

    print()
    answer = int(input("How many times do you want to run the simulation? "))
    print()

    done = False

    while not done:

        if plays == answer-1:

            done = True

        new_deck1, new_hand1, ace_hand1, new_dealer1, ace_dealer1 = first_deal()

        new_deck2, new_hand2, ace_hand2, new_dealer2, ace_dealer2 = \
            bot_turn(new_deck1, new_hand1, ace_hand1, new_dealer1, ace_dealer1)

        if new_hand2 == 21:

            player_wins += 1
            plays += 1
            continue

        elif new_hand2 > 21:

            dealer_wins += 1
            plays += 1
            continue

        new_deck3, new_hand3, ace_hand3, new_dealer3, ace_dealer3 = \
            dealer_turn(new_deck2, new_hand2, ace_hand2, new_dealer2, ace_dealer2)

        if new_dealer3 == 21:

            dealer_wins += 1
            plays += 1
            continue

        elif new_dealer3 > 21:

            player_wins += 1
            plays += 1
            continue

        elif new_hand1 == new_dealer1:

            draws += 1
            plays += 1
            continue

        elif new_dealer3 > new_hand3:

            dealer_wins += 1
            plays += 1
            continue

        elif new_dealer3 < new_hand3:

            player_wins += 1
            plays += 1
            continue

    print()
    print("You ran the simulation", plays, "times")
    print()
    print("You won", player_wins, "times")
    print("The dealer won", dealer_wins, "times")
    print("There were", draws, "draws")
    print()
    print(player_wins + dealer_wins + draws)
    print()


if __name__ == "__main__":
    main()
