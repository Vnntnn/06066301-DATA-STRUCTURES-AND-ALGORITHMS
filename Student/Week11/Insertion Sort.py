"""Insertion sort"""


def insertionSort(lst: list, last: int) -> int:
    """Insertion sorting function"""
    comparison = 0
    for current in range(1, last + 1):
        hold = lst[current]
        walker = current - 1

        while walker >= 0 and lst[walker] > hold:
            lst[walker + 1] = lst[walker]
            walker -= 1
            comparison += 1

        lst[walker + 1] = hold
        print(lst)

        if walker >= 0:
            comparison += 1

    return comparison


def main():
    """main function"""
    from json import loads

    print(f"Comparison times: {insertionSort(loads(input()), int(input()))}")


main()
