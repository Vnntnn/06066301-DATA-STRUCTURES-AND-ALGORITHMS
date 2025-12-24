"""Find city(ies) that covering all stations in all cities"""

import json


def insertionSort(lst: list, stations: set) -> list:
    """Insertion sorting function by sorted from max value first to min value"""
    for current in range(1, len(lst)):
        hold = lst[current]
        walker = current - 1

        while walker >= 0 and len(
            set(lst[walker]["Cities"]).intersection(stations)
        ) < len(set(hold["Cities"]).intersection(stations)):
            lst[walker + 1] = lst[walker]
            walker -= 1

        lst[walker + 1] = hold

    return lst


def findStations(stations: list) -> list:
    """Find intersec stations in city"""
    cities = [json.loads(input()) for _ in range(int(input()))]
    stations, ans = set(stations), []

    while stations:
        cities = insertionSort(cities, stations)
        current = cities.pop(0)
        covered = set(current["Cities"]).intersection(stations)

        if not covered:
            break

        ans.append(current["Name"])
        stations -= covered

    return sorted(ans)


def main():
    """main function"""
    print(findStations(json.loads(input())))


main()
