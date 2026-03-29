FILE = "students.txt"
while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        roll = input("Enter roll no: ")

        f = open(FILE, "a")
        f.write(roll + " " + name + "\n")
        f.close()

        print("Student added\n")

    elif choice == "2":
        try:
            f = open(FILE, "r")
            print("\nStudent List:")
            print(f.read())
            f.close()
        except:
            print("No data found\n")

    elif choice == "3":
        print("Thank you")
        break

    else:
        print("Invalid choice\n")
