def print_asc(n, max):
    if n > 0 and max >= n:
        print(f"{n}, ", end="")
        print_asc(n + 2, max)
    return

def main():
    print_asc(int(input()), int(input()))

if __name__ == "__main__":
    main()
