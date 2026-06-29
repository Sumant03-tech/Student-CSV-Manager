import pandas as pd
names = []
ages = []
marks = []

for i in range(5):
    name = input("Enter Name:")
    age = int(input("Enter Age:"))
    mark = float(input("Enter Mark:"))
    
    names.append(name)
    ages.append(age)
    marks.append(mark)

students = {
    "Name" : names,
    "Age" : ages,
    "Mark" : marks
    }
df = pd.DataFrame(students)
df.to_csv("students_1.csv",index = False)
df = pd.read_csv("students_1.csv")
print(df)
print(df[df["Mark"] == df["Mark"].max()])
print(df[df["Mark"] == df["Mark"].min()])
print(df["Mark"].mean())
print(df[df["Mark"]>80])
print(df[df["Age"]>20])
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())