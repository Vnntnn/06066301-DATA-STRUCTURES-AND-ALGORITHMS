"""Dispenser"""

def dispenser_drop_number(n, m):
    """Dispensor droping by find max from every dispenser first"""
    dispensers = [input().split() for _ in range(n)]
    dispensers = [[dispensers[i][j] for i in range(n)] for j in range(m)]

    result = ""
    full, max_n = 0, 0
    index = []

    for i in range(m):
        for j in range(n):
            

def main():
    """main function"""
    print(dispenser_drop_number(int(input()), int(input())))


main()
