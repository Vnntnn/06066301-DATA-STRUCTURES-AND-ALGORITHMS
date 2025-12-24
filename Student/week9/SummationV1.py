"""Summation using loop"""
def loopSum(num) -> int:
    """Plus num using loop"""
    su_m = 0
    for i in range(1, num+1):
        su_m += i

    return su_m

def main():
    """main function"""
    print(loopSum(int(input())))

main()
