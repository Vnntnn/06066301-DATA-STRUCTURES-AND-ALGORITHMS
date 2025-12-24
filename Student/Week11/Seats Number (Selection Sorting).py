"""Sorting seats number by using selection sorting"""


def text_seperate(seat: str):
    """Seperate character and number from string"""
    text, number = "", ""
    for char in seat:
        if char.isalpha():
            text += char
        else:
            number += char
    return text, int(number)


def seatsSelectionSort(lst: list, last: int) -> int:
    """Selection sorting algorithms function for seats number"""
    comparison = 0

    for current in range(last):
        smallest = current
        small_t, small_n = text_seperate(lst[smallest])

        for walker in range(current + 1, last + 1):
            walker_t, walker_n = text_seperate(lst[walker])

            if walker_t < small_t or (walker_t == small_t and walker_n < small_n):
                smallest = walker
                small_t, small_n = walker_t, walker_n

            comparison += 1

        lst[current], lst[smallest] = lst[smallest], lst[current]
        print(lst)

    return comparison


def main():
    """main function"""
    from json import loads

    print(f"Comparison times: {seatsSelectionSort(loads(input()), int(input()))}")


main()
