"""FibonacciRecursionV1"""
def fibo(n: int):
    if n == 1:
        return 1
    if not n:
        return 0
    return fibo(n - 1) + fibo(n -2)

print(fibo(int(input())))
