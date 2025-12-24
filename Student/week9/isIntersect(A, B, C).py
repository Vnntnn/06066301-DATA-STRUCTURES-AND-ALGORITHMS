"""isIntersect(A, B, C)"""
from json import loads

def intersec(a, b, c) -> bool:
    """intersec function"""
    for i in a:
        if i in b and i in c:
            return True
    return False

def main():
    """main function"""
    print(intersec(loads(input()), loads(input()), loads(input())))

main()
