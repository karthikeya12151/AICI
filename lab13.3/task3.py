class Student:
    """
    A class to represent a student with personal details and marks.
    """
    def __init__(self, name, age, marks):
        """
        Initialize a Student object.
        Parameters:
        name (str): Name of the student
        age (int): Age of the student
        marks (list): List of marks in subjects
        """
        self.name = name
        self.age = age
        self.marks = marks
    def details(self):
        """Prints student details in a readable format."""
        print(f"Name: {self.name}, Age: {self.age}")
    def total(self):
        """Returns the total marks of the student."""
        return sum(self.marks)
if __name__ == "__main__":
    # Dynamic input
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    marks = []
    for i in range(3):  # Can easily expand if more subjects
        mark = float(input(f"Enter mark {i+1}: "))
        marks.append(mark)
    student = Student(name, age, marks)
    print("\n--- Student Information ---")
    student.details()
    print(f"Total Marks: {student.total()}")
