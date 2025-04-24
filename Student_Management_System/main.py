from database import create_connection, add_student, view_students

def main():
    conn = create_connection()
    while True:
        print("\n1. Add Student\n2. View Students\n3. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            roll = input("Enter roll number: ")
            add_student(conn, name, age, roll)
        elif choice == '2':
            view_students(conn)
        elif choice == '3':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
