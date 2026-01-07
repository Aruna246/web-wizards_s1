n = int(input("Enter number of students: "))
students = []
for i in range(n):
    name = input("Enter student name: ")
    dept = input("Enter department: ")
    students.append([name, dept])
    seating = []
while students:
    for student in students:
        if not seating:
            seating.append(student)
            students.remove(student)
            break
        elif seating[-1][1] != student[1]:
            seating.append(student)
            students.remove(student)
            break
print("Exam Hall Seating Arrangement:\n")
seat_no = 1
for s in seating:
    print(f"Seat {seat_no} - {s[0]} ({s[1]})")
    seat_no += 1
