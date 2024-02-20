student_marks={
        "Renju":95,
        "Edwynn":67,
        "Bosco":100,
        "Don":60,
        "Wamboi":75
        }
sorted_marks =sorted(student_marks.items(),key =lambda x:x[1])
print("Student marks in ascending order:")
for name,marks in sorted_marks:
    print(f"{name}:{marks}")
