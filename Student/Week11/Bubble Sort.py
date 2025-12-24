"""Bubble Sort"""


def bubbleSort(lst: list, last: int) -> int:
    """Bubble sort function"""
    current = 0
    sorte_d = False
    comparison = 0

    while current <= last and sorte_d != True:
        walker = last
        sorte_d = True

        while walker > current:
            if lst[walker] < lst[walker - 1]:
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

    print(f"Comparison times: {bubbleSort(loads(input()), int(input()))}")


main()
