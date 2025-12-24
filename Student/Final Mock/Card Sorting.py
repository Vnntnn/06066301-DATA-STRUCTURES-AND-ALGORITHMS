import json

"""Card Sorting using bubble sort"""


def card_priority(card: str) -> tuple:
    """Card priority checking"""
    dork = ("S", "H", "D", "C")
    cards = ("K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2", "1", "A")

    if card[:-1] == "10":
        dork_card, cards_ = "10", card[-1]
    else:
        dork_card, cards_ = card[:-1], card[-1]

    return (dork.index(cards_), cards.index(dork_card))


def bubble_sort_card(cards: list) -> list:
    """Bubble sort for sorting cards based on priority"""
    n = len(cards)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if card_priority(cards[j]) > card_priority(cards[j + 1]):
                cards[j], cards[j + 1] = cards[j + 1], cards[j]
    return cards


def bubble_sort_point(lst: list) -> list:
    """Bubble sort for sorting total points from player"""
    n = len(lst)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lst[j][2] < lst[j + 1][2]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


def card_sorting(n: int, m: int):
    """Card sorting and counting points function"""
    lst = []

    # Input
    for _ in range(n):
        player = json.loads(input())
        lst.append([player[0], player[1], 0])

    # Card sorting
    for player in lst:
        player[1] = bubble_sort_card(player[1])

    # Points calc
    for player in lst:
        for card in player[1]:
            if card in ("2C", "QS"):
                player[2] += 50
            elif "A" in card:
                player[2] += 15
            elif card[:-1] in ("J", "K", "Q", "10"):
                player[2] += 10
            else:
                player[2] += 5

    # Sorting total point from player
    lst = bubble_sort_point(lst)

    for player in lst:
        print(player[0], "->", player[2], "->", player[1])


def main():
    """Main function"""
    card_sorting(int(input()), int(input()))


main()
