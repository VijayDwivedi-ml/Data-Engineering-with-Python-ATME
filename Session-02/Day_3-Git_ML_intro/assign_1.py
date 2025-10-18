import json
import os

FILE_NAME = "students.json"

# ----------- Utility Functions -----------

def load_data():
    """Load student records from a JSON file."""
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    return {}

def save_data(students):
    """Save student records to a JSON file."""
    with open(FILE_NAME, "w") as f:
        json.dump(students, f, indent=4)

# ----------- CRUD Functions -----------

def display_menu():
    print("\n--- Student Record Management System ---")
    print("1. Add Student Record")
    print("2. View All Students")
    print("3. Search Student by ID")
    print("4. Update Student Record")
    print("5. Delete Student Record")
    print("6. Exit")

def add_student(students):
    sid = input("Enter Student ID: ").strip()
    if sid in students:
        print("❌ Student ID already exists!")
        return
    name = input("Enter Student Name: ")
    age = input("Enter Age: ")
    grade = input("Enter Grade: ")
    students[sid] = {"name": name, "age": int(age), "grade": grade}
    save_data(students)
    print(f"✅ Record added for {name} (ID: {sid})")

def view_students(students):
    if not students:
        print("📭 No records found.")
        return
    print("\n📋 Student Records:")
    for sid, info in students.items():
        print(f"ID: {sid} | Name: {info['name']} | Age: {info['age']} | Grade: {info['grade']}")

def search_student(students):
    sid = input("Enter Student ID to search: ").strip()
    if sid in students:
        info = students[sid]
        print(f"🔍 Found: {info['name']} (Age: {info['age']}, Grade: {info['grade']})")
    else:
        print("❌ Student not found.")

def update_student(students):
    sid = input("Enter Student ID to update: ").strip()
    if sid in students:
        print("Enter new details (leave blank to keep current value):")
        name = input(f"New Name [{students[sid]['name']}]: ") or students[sid]['name']
        age_input = input(f"New Age [{students[sid]['age']}]: ")
        grade = input(f"New Grade [{students[sid]['grade']}]: ") or students[sid]['grade']
        age = int(age_input) if age_input else students[sid]['age']
        students[sid] = {"name": name, "age": age, "grade": grade}
        save_data(students)
        print("✅ Record updated successfully.")
    else:
        print("❌ Student not found.")

def delete_student(students):
    sid = input("Enter Student ID to delete: ").strip()
    if sid in students:
        confirm = input(f"Are you sure you want to delete record for {students[sid]['name']}? (y/n): ").lower()
        if confirm == 'y':
            del students[sid]
            save_data(students)
            print("🗑️ Record deleted successfully.")
    else:
        print("❌ Student not found.")

# ----------- Main Program -----------

def main():
    students = load_data()
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            print("👋 Exiting program. Records saved.")
            break
        else:
            print("⚠️ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
