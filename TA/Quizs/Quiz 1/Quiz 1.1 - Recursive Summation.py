"""

Average solution this quiz time: 1 - 2 mins
Time: 14:40 - 14:42 (Bangkok timezone)

"""
def res(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return n + res(n - 2)

def main() -> None:
    print(res(int(input())))

if __name__ == "__main__":
    main()