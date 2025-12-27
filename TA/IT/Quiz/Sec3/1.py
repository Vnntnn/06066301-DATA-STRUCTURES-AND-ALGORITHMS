def res(n: int, m: int) -> int:
    if n > 0 and n <= m:
        return n + res(n + 3, m)
    return n

def main():
    print(res(int(input()), int(input())))

if __name__ == "__main__":
    main()