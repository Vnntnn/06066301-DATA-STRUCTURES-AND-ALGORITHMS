"""Find minimum maximum and average from list"""
from json import loads
def main():
    """main function"""

    lst = loads(input())
    mnn, mxx, avg = round(float(lst[0]), 2), round(float(lst[0]), 2), 0

    for i in lst:
        i = round(i, 2)
        if i < mnn:
            mnn = i
        elif i > mxx:
            mxx = i

    avg = sum(lst) / len(lst)

    print(f"({mxx:.2f}, {mnn:.2f}, {avg:.2f})")

main()
