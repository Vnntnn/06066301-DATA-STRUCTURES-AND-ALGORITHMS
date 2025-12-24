"""Selection Sort"""


def selectionSort(lst: list, last: int) -> int:
    """Selection sort function"""
    comparison = 0

    for current in range(last):
        smallest = current
        walker = current + 1

        while walker <= last:

            if lst[walker] < lst[smallest]:
                smallest = walker

            walker += 1
            comparison += 1

        lst[current], lst[smallest] = lst[smallest], lst[current]
        print(lst)

    return comparison


def main():
    """main function"""
    from json import loads

    print(f"Comparison times: {selectionSort(loads(input()), int(input()))}")


main()
