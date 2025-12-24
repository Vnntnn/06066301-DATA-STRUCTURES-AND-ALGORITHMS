"""Choose items in a bag by using greedy by picking any items 
    to get the most total weight as impossible"""


class Item:
    def __init__(self, name: str, price: int, weight: float):
        self.__name = name
        self.__price = price
        self.__weight = weight

    def get_name(self) -> str:
        return self.__name

    def get_price(self) -> int:
        return self.__price

    def get_weight(self) -> float:
        return self.__weight

    def get_cost(self) -> float:
        return self.__price / self.__weight


def insertionSort(lst: list) -> list:
    """Insertion sorting function by sorted from max value first to min value"""
    for current in range(1, len(lst)):
        hold = lst[current]
        walker = current - 1

        while walker >= 0 and lst[walker].get_cost() < hold.get_cost():
            lst[walker + 1] = lst[walker]
            walker -= 1

        lst[walker + 1] = hold

    return lst


def knapsack(amount: int, itemList: list):
    """Picking items by using greedy algorithms"""
    sorted_item = insertionSort(itemList)
    index, total = 0, 0

    print(f"Knapsack Size: {amount} kg\n===============================")

    while amount > 0 and len(sorted_item) > index:
        if sorted_item[index].get_weight() <= amount:
            total += sorted_item[index].get_price()
            amount -= sorted_item[index].get_weight()
            print(
                f"{sorted_item[index].get_name()} -> {sorted_item[index].get_weight()} kg -> {sorted_item[index].get_price()} THB"
            )
        index += 1

    print(f"Total: {total} THB")


def main():
    import json

    items = []
    num_items = int(input())
    while num_items != 0:
        item_in = json.loads(input())
        items.append(Item(item_in["name"], item_in["price"], item_in["weight"]))
        num_items = num_items - 1
    knapsack_capacity = float(input())
    knapsack(knapsack_capacity, items)


main()
