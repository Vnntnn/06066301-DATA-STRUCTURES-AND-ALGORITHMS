"""Super food application"""
class app:
    def __init__(self, food = ["Pizza", "Fried Chicken", "Hamburger", "Steak"]):
        self.food = food
        self.random = 0

    def random_foods(self):
        self.random += 1

    def list_foods(self):
        return sorted(self.food)
    
    def add_food_item(self, name):
        self.food.append(name)

FOOD_NUMBER = int(input())
FOOD_NAME = [input() for _ in range(FOOD_NUMBER)]
FOOD_LST = app()

for food in FOOD_NAME:
    FOOD_LST.add_food_item(food)

print(FOOD_LST.list_foods())
