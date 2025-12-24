"""Where the floor you at?"""
class Elevator:
    def __init__(self, max_floor):
        self.current_floor = 1
        self.max_floor = max_floor

    def go_to_floor(self, floor):
        self.current_floor = floor

    def report_current_floor(self):
        print(self.current_floor)

MAX = int(input())
ELEVATORR = Elevator(MAX)

while (z:= input()) != "Done":
    if int(z) > ELEVATORR.max_floor:
        print("Invalid Floor!")
    else:
        ELEVATORR.go_to_floor(z)

ELEVATORR.report_current_floor()
