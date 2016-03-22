import Deck
import random
import copy


def start():

    new_deck1 = copy.deepcopy(Deck.deck())

    new_dealer1 = 0
    new_hand1 = 0
    ace_dealer1 = 0
    ace_hand1 = 0

    print()
    card_d = int(input("What card should the dealer start with? "))
    print()

    card_d = new_deck1[card_d-1]
    print(card_d[0])

    new_dealer1 += card_d[1]

    if card_d[1] == 11:
        ace_dealer1 += 1

    print()
    cards_h = input("What cards should the player start with? ").split(" ")
    card_h = []
    for card in cards_h:
        card_h.append(int(card))
    print()

    card_h0 = new_deck1[card_h[0]-1]
    card_h1 = new_deck1[card_h[1]-1]

    new_deck1.remove(card_d)
    new_deck1.remove(card_h0)
    new_deck1.remove(card_h1)

    new_hand1 += card_h0[1]
    new_hand1 += card_h1[1]

    if card_h0[1] == 11:
        ace_hand1 += 1

    if card_h1[1] == 11:
        ace_hand1 += 1

    print(card_h0[0])
    print(card_h1[0])
    print()
    print("The dealer has", new_dealer1)
    print("You have", new_hand1)
    print()

    return new_deck1, new_dealer1, new_hand1, ace_dealer1, ace_hand1


def bot(new_deck1, new_dealer1, new_hand1, ace_dealer1, ace_hand1):

    new_deck2 = copy.deepcopy(new_deck1)
    new_hand2 = copy.deepcopy(new_hand1)
    ace_hand2 = copy.deepcopy(ace_hand1)
    new_dealer2 = copy.deepcopy(new_dealer1)
    ace_dealer2 = copy.deepcopy(ace_dealer1)

    done = False

    while not done:

        if new_hand2 > 16:

            done = True

        elif 12 < new_hand2 < 17:

            if new_dealer2 > 6:

                done = True

            else:

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

        elif new_hand2 == 12:

            if 3 < new_dealer2 < 7:

                done = True

            else:
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

        else:

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
