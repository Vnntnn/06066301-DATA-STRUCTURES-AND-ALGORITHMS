"""Summation using formula to calc"""
def formSum(num) -> int:
    """Using formula function to calc each number"""
    return (num * (num + 1)) / 2

def main():
    """main function"""
    print(formSum(int(input())))

main()
