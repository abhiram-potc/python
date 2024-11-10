n = int(input("Enter the no. of students: "))
print("\n")
student={}
ls=[]
for i in range(0,n):
    name = input("Student name: ")
    age = input("Student age: ")
    grade = input("Student grade: ")
    print("\n")
    student[name]=[age,grade]
    ls.append((name, [age,grade]))

for name, info in ls:
    print(f"Name: {name}, Age: {info[0]}, Grade: {info[1]}")