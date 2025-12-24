"""ProbHash Hashing"""
class Student:
    """Student class"""
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
        """Print student detail"""
        print(f"ID: {self.getStd_id()}\nName: {self.getName()}\nGPA: {self.getGpa():.2f}")

class ProbHash:
    """Hashing table"""
    def __init__(self, size: int):
        self.hash_table = [None] * size
        self.size = size

    def hash(self, key: int) -> int:
        return key % self.size

    def rehash(self, hkey: int) -> int:
        return (hkey + 1) % self.size

    def insert_data(self, student: Student):
        """insert data"""
        if None not in self.hash_table:
            print(f"The list is full. {student.getStd_id()} could not be inserted.")
            return
        index = self.hash(student.getStd_id())
        while self.hash_table[index] is not None:
            index = self.rehash(index)
        self.hash_table[index] = student
        print(f"Insert {student.getStd_id()} at index {index}")

    def search_data(self, std_id: int) -> Student:
        """Search for a student"""
        start_index = self.hash(std_id)
        for _ in range(self.size):
            item = self.hash_table[start_index]
            if item is None:
                break
            if item.getStd_id() == std_id:
                print(f"Found {std_id} at index {start_index}")
                return item
            start_index = self.rehash(start_index)
        print(f"{std_id} does not exist.")
        return None

def main():
    import json
    size = int(input())
    hashtable = ProbHash(size)
    while True:
        finish = input()
        if finish == "Done":
            break
        condition, data = finish.split(" = ")
        if condition == "I":
            std_in = json.loads(data)
            std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
            hashtable.insert_data(std)
        elif condition == "S":
            print("------")
            student = hashtable.search_data(int(data))
            if student is not None:
                student.print_details()
            print("------")
        else:
            print("Invalid Condition!")
main()
