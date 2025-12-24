"""Sorting seats number by using bubble sorting"""


def text_seperate(seat: str):
    """Seperate character and number from string"""
    text, number = "", ""
    for char in seat:
        if char.isalpha():
            text += char
        else:
            number += char
    return text, int(number)


def seatsBubbleSort(lst: list, last: int) -> int:
    """Bubble sorting algorithms function for seats number"""
    current = 0
    sorte_d = False
    comparison = 0

    while current <= last and sorte_d != True:
        walker = last
        sorte_d = True

        while walker > current:
            walker_t, walker_n = text_seperate(lst[walker])
            pwalker_t, pwalker_n = text_seperate(lst[walker - 1])

            if walker_t < pwalker_t or (walker_t == pwalker_t and walker_n < pwalker_n):
                sorte_d = False
                lst[walker - 1], lst[walker] = lst[walker], lst[walker - 1]

            comparison += 1
            walker -= 1

        print(lst)
        current += 1

    return comparison


def main():
    """main function"""
    from json import loads

    print(f"Comparison times: {seatsBubbleSort(loads(input()), int(input()))}")


main()
