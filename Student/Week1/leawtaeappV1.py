"""food application"""
class app:
    def __init__(self):
        self.food = ["Pizza", "Fried Chicken", "Hamburger", "Steak"]
        self.random = 0

    def random_foods(self):
        self.random += 1

    def list_foods(self):
        return sorted(self.food)

LST = app()
print(LST.list_foods())
