import tkinter as tk
from tkinter import messagebox

class Students:
    def __init__(self, name, math, science, english):
            self.name = name
            self.math = math
            self.science = science
            self.english = english

    def calculateGrades(self):
        try:
            math = int(self.math)
            english = int(self.english)
            science = int(self.science)
            return (math + english + science) / 3
        except ValueError:
                    return None
    
    def displayGrades(self, resultLabel):
        gpa = self.calculateGrades()
        if gpa is None:
            messagebox.showerror("Invalid Input", "Please enter a valid value")
            return
        status = "Passed" if gpa > 75 else "Failed"
        resultLabel.config(text=f"Average grade: {gpa:.2f}\n"
                   f"Status: {status}\n"
                   f"Name: {self.name}\n"
                   f"Science: {self.science}\n"
                   f"Math: {self.math}\n"
                   f"English: {self.english}")

root = tk.Tk()
title = root.title("GPA Calculator")

tk.Label(root, text="Calculate grades").grid(columnspan=4)
# tkinter doesnt support html syntax to use texts, use Label instead.
name = tk.Label(root, text="Your Name:", width=30).grid(row=1)
math = tk.Label(root, text="Math:", width=30).grid(row=2)
science = tk.Label(root, text="Science:", width=30).grid(row=3)
english = tk.Label(root, text="English:", width=30).grid(row=4)

# Declare
nameEntry = tk.Entry(root)
mathEntry = tk.Entry(root)
scienceEntry = tk.Entry(root)
englishEntry = tk.Entry(root)

# Assign
nameEntry.grid(row=1, column=2)
mathEntry.grid(row=2, column=2)
scienceEntry.grid(row=3, column=2)
englishEntry.grid(row=4, column=2)

# result label display
result = tk.Label(root, text="")
result.grid(row=6, columnspan=4)


def displayInLabel():
    initia = Students(nameEntry.get(), mathEntry.get(), scienceEntry.get(), englishEntry.get())
    initia.displayGrades(result)


# this is a button that will be used to calculate the grades
button = tk.Button(root, text="Calculate your grades", width=30, command=displayInLabel)
button.grid(row=5, columnspan=4)
root.mainloop()
