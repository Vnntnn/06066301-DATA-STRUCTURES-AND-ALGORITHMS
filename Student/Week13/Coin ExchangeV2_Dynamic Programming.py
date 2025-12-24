import json

def convert_key(data):
    return {int(k): v for k, v in data.items()}

def coin_exchange(amount, coins):
    coin_types = sorted(coins.keys(), reverse=True)
    dp = {0: {c: 0 for c in coin_types}}

    for value in range(1, amount + 1):
        dp[value] = None
        for coin in coin_types:
            if value >= coin and dp[value - coin] is not None and dp[value - coin][coin] < coins[coin]:
                new_combination = dp[value - coin].copy()
                new_combination[coin] += 1

                if dp[value] is None or sum(new_combination.values()) < sum(dp[value].values()):
                    dp[value] = new_combination

    print(f"Amount: {amount}")
    if dp[amount] is None:
        print("Can not exchange.")
    else:
        print("Coin exchange result:")
        total_used = 0
        for coin in coin_types:
            count = dp[amount][coin]
            print(f"  {coin} baht = {count} coins")
            total_used += count
        print(f"Number of coins: {total_used}")

def main():
    amount = int(input())
    coins = convert_key(json.loads(input()))
    coin_exchange(amount, coins)

main()

