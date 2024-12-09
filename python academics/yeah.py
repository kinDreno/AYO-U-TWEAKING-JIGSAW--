class Students:
    def __init__(self, name, math, science, english):
        self.name = name
        self.math = math
        self.science = science
        self.english = english
    
    def computeAverage(self):
        return (self.math + self.science + self.english) / 3

    def displayAverage(self):
        
        average = self.computeAverage()

        status = "Passed" if average >= 75 else "Failed"

        print(f"Name: {self.name}")
        print(f"Math grade: {self.math}")
        print(f"Science: {self.science}")
        print(f"English: {self.english}")
        print(f"GPA Calculated: {average}, {status}")

name = input("Input your name: ")
math = int(input("Your grade in math: "))
science = int(input("Your grade in science:  "))
english = int(input("Your grade in english: "))

students = Students(name, math, science, english)
students.displayAverage()
