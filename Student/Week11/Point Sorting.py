"""Point Sorting"""


def insertionSort(lst, last):
    """Insertion sorting function"""
    for current in range(1, last):
        hold = lst[current]
        walker = current - 1

        while walker >= 0 and (
            lst[walker][0] > hold[0]
            or (lst[walker][0] == hold[0] and lst[walker][1] < hold[1])
        ):
            lst[walker + 1] = lst[walker]
            walker -= 1

        lst[walker + 1] = hold


def pointSorting(pack):
    """Point sorting by using insertion sorting"""
    for _ in range(pack):
        point_pack = int(input())
        points = []

        for _ in range(point_pack):
            x, y = input().split()
            x, y = int(x), int(y)
            points.append((x + y, y, x))

        insertionSort(points, point_pack)

        for p in points:
            print(p[2], p[1], end="\n")


def main(n):
    """main function"""
    pointSorting(n)


main(int(input()))
