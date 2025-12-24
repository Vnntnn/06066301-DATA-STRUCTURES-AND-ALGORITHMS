"""Binary search"""
from json import loads

class Student:
    """Student Class"""
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
        """print student detail"""
        print(f"ID: {self.getStd_id()}\nName: {self.getName()}\nGPA: {self.getGpa():.2f}")

def binary_search(data: list[Student], name: str):
    """Binary search from arr"""
    start, stop, cnt = 0, len(data) - 1, 0
    while start <= stop:
        cnt += 1
        mid = (start + stop) // 2
        if name > data[mid].getName():
            start = mid + 1
        elif name < data[mid].getName():
            stop = mid - 1
        else:
            print(f"Found {data[mid].getName()} at index {mid}")
            data[mid].print_details()
            print(f"Comparisons times: {cnt}")
            return
    print(f"{name} does not exist.\nComparisons times: {cnt}")
    return

def main(text_in: list[dict], search: str):
    """main function"""
    std_inn = loads(text_in)
    students = [Student(std_in["id"], std_in["name"], std_in["gpa"]) for std_in in std_inn]
    binary_search(students, search)

main(input(), input())
