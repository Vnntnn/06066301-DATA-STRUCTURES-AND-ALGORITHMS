"""Student class"""
class Student:
    def __init__(self, std_id: int, name: str, gpa: float):
        self.__std_id = std_id
        self.__name = name
        self.__gpa = gpa
    
    def getStd_id(self) -> int:
        return self.__std_id

    def getName(self) -> str:
        return self.__name

    def getGpa(self) -> float:
        return self.__gpa

    def print_details(self):
        print(f"ID: {self.getStd_id()}\nName: {self.getName()}\nGPA: {self.getGpa():.2f}")

def main(text_in):
    import json
    std_in = json.loads(text_in)
    std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
    std.print_details()

main(input())
