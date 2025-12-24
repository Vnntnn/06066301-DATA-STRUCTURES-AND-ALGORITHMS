"""Calculator"""
def calculator(num) -> int:
    """Calc input function"""
    if num == 1:
        return 1
    return num * 2 - 1

def main():
    """main function"""
    print(calculator(int(input())))

main()
