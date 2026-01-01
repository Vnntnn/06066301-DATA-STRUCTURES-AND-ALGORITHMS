def res(n: int, max: int) -> int:
    if n + 3 > max:
        return n
    return n + res(n + 3, max)

def main():
    print(res(int(input()), int(input())))

if __name__ == "__main__":
    main()
