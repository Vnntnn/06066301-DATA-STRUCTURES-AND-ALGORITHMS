"""Runner"""


def runner(distance: int, player: int) -> int:
    """Find winner of all runners from speed and distances"""
    winner, min_time, max_speed = 0, float("inf"), 0

    for i in range(1, player + 1):
        speed, start = map(int, input().split())
        time = (distance - start) / speed

        if time < min_time or (time == min_time and speed > max_speed):
            min_time, max_speed, winner = time, speed, i

    return winner


def main(d: int, p: int):
    """main function"""
    print(runner(d, p))


main(int(input()), int(input()))
