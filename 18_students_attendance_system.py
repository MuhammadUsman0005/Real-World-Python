students = {}

print("------- ATTENDANCE SYSTEM -------")
print("1. Add student")
print("2. Mark attendance")
print("3. Show student Attendence")
print("4. Class stats")
print("5. Top 3 students")
print("6. Exit Attendance System")

while True:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter student name: ").strip()
        if name == "":
            print("Invalid name!")
            continue
        if name not in students:
            students[name] = []
            print("Student added!")
        else:
            print("Already exists!")
    elif choice == 2:
        if len(students) == 0:
            print("No students to mark.")
            continue
        print("\nMark Attendance (P/A):")
        for name in students:
            status = input(f"{name}: ").strip().upper()
            if status not in ["P", "A"]:
                print("Invalid input! Marked as A.")
                status = "A"
            students[name].append(status)
        print("Attendance marked!")
    elif choice == 3:
        name = input("Enter student name: ").strip()
        if name not in students:
            print("Student not found!")
        else:
            total = len(students[name])
            present = students[name].count("P")
            percent = (present/total * 100) if total > 0 else 0
            print(f"\n{name}'s Attendance:")
            print("Record: ",students[name])
            print("Present: ",present)
            print("Attendance %:", round(percent, 2))
    elif choice == 4:
        if len(students) == 0:
            print("No data!")
            continue

        print("\nClass Stats:")
        for name, record in students.items():
            total = len(record)
            present = record.count("P")
            percent = (present / total * 100) if total > 0 else 0
            print(f"{name}: {round(percent,2)}%")

    # 5. Top 3 students
    elif choice == 5:
        if len(students) == 0:
            print("No data!")
            continue

        stats = []
        for name, record in students.items():
            total = len(record)
            present = record.count("P")
            percent = (present / total * 100) if total > 0 else 0
            stats.append((name, percent))

        top3 = sorted(stats, key=lambda x: x[1], reverse=True)[:3]

        print("\nTop 3 Students:")
        for name, percent in top3:
            print(f"{name}: {round(percent,2)}%")

    elif choice == 6:
        exit()
    else:
        print("Invalid choice!")