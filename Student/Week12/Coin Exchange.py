"""Exchange coins using greedy and using less coins as impossible"""


def coinExchange(amount: int, coins: dict):
    """Funtion using greedy algorithms"""
    print("Amount:", amount)

    result = {}
    total_coins = 0

    for coin in coins.keys():
        coin_num = min(amount // coin, coins[coin])

        if amount >= 0:
            result[coin] = coin_num
            total_coins += coin_num
            amount -= coin * coin_num

    if amount > 0:
        print("Coins are not enough.")
        return

    print("Coin exchange result:")
    for coin in result.keys():
        print(f"  {coin} baht = {result[coin]} coins")
    print(f"Number of coins: {total_coins}")
    return


def convert_key(data):
    """Convert String key to integer"""
    return {int(k): v for k, v in data.items()}


def main():
    """Main function"""
    import json

    coinExchange(int(input()), convert_key(json.loads(input())))


main()
