"""Longest Common Substring"""


def lcs(t1: str, t2: str):
    """Find same substring using dynamic programming"""
    cell = [[0] * len(t1) for _ in range(len(t1))]
    l, r = 0, 0

    for i in range(len(t1)):
        for j in range(len(t1)):
            if t1[i] == t2[j]:
                cell[i][j] = cell[i - 1][j - 1] + 1

            if cell[i][j] > l:
                l = cell[i][j]
                r = i

    if l > 0:
        print(f"{t1[r - l + 1 : r + 1]}\n{l}")
        return
    print("No common substring.")


def main():
    """Main function"""
    lcs(input(), input())


main()
