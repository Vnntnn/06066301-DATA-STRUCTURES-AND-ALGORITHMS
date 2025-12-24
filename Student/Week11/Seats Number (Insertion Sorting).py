"""Sorting seats number by using insertion sorting"""


def text_seperate(seat: str):
    """Seperate character and number from String"""
    text, number = "", ""
    for char in seat:
        if char.isalpha():
            text += char
        else:
            number += char
    return text, int(number)


def seatsInsertionSort(lst: list, last: int) -> int:
    """Insertion sorting algorithms function for seats number"""
    comparison = 0

    for current in range(1, last + 1):
        hold = lst[current]
        walker = current - 1

        hold_t, hold_n = text_seperate(hold)

        while walker >= 0:
            comp_t, comp_n = text_seperate(lst[walker])

            comparison += 1
            if hold_t < comp_t or (hold_t == comp_t and hold_n < comp_n):
                lst[walker + 1] = lst[walker]
                walker -= 1
            else:
                break

        lst[walker + 1] = hold
        print(lst)

    return comparison


def main():
    """main function"""
    from json import loads

    print(f"Comparison times: {seatsInsertionSort(loads(input()), int(input()))}")


main()
