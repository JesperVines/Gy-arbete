import random
import Start
import copy

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


def dealer_turn(new_deck2, new_hand2, ace_hand2, new_dealer2, ace_dealer2):

    new_deck3 = copy.deepcopy(new_deck2)
    new_hand3 = copy.deepcopy(new_hand2)
    ace_hand3 = copy.deepcopy(ace_hand2)
    new_dealer3 = copy.deepcopy(new_dealer2)
    ace_dealer3 = copy.deepcopy(ace_dealer2)

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

    new_deck1, new_dealer1, new_hand1, ace_dealer1, ace_hand1 = Start.start()

    answer = float(input("How many times do you want to run the simulation? "))
    print()

    done = False

    while not done:

        if plays == answer:

            break

        if new_hand1 == 21:

            player_wins += 1
            plays += 1
            continue

        new_deck2, new_hand2, ace_hand2, new_dealer2, ace_dealer2 = \
            Start.bot(new_deck1, new_hand1, ace_hand1, new_dealer1, ace_dealer1)

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
