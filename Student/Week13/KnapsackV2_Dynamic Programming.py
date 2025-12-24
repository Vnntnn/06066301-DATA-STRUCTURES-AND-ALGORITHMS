"""Knapsack using dynamic programming"""

import json


def knapsack(capacity: int, items: list):
    """Picking up item using Dynamic Programming"""
    names, values, weights = zip(*items)
    n, dp = len(weights), [[0] * (capacity + 1) for _ in range(len(weights) + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            dp[i][w] = (
                dp[i - 1][w]
                if weights[i - 1] > w
                else max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            )

    selected, w = [], capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append((names[i - 1], weights[i - 1], values[i - 1]))
            w -= weights[i - 1]

    print(f"Total: {dp[n][capacity]}")
    for name, weight, value in sorted(selected):
        print(f"{name} -> {weight} kg -> {value} THB")


def main():
    items = json.loads(input())
    cap = int(input())
    knapsack(cap, items)


main()
