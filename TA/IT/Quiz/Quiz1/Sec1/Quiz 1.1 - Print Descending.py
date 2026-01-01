def print_desc(n: int, step: int) -> None:
    if n < 0 or step <= 0:
        return
    print(f"{n}, ", end="")
    next_n = n - step
    if next_n >= 0:
        print_desc(next_n, step)

def main():
    print_desc(int(input()), int(input()))

if __name__ == "__main__":
    main()