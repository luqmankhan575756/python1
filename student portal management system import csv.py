import csv
from datetime import datetime


FILENAME = "attendance.csv"

def add_attendance():
    name = input("Enter student name: ").strip()
    status = input("Enter status (Present/Absent): ").strip().capitalize()
    date = datetime.now().strftime("%Y-%m-%d")

    
    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, date, status])
    
    print(f"✅ Attendance marked for {name} on {date} as {status}")


def view_attendance():
    try:
        with open(FILENAME, "r") as file:
            reader = csv.reader(file)
            print("\n--- Attendance Record ---")
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("⚠️ No attendance record found yet!")


def search_attendance():
    name = input("Enter student name to search: ").strip()
    found = False
    try:
        with open(FILENAME, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row and row[0].lower() == name.lower():
                    print(row)
                    found = True
        if not found:
            print(f"❌ No record found for {name}")
    except FileNotFoundError:
        print("⚠️ No attendance file found!")


def main():
    while True:
        print("\n==== Attendance Management System ====")
        print("1. Add Attendance")
        print("2. View Attendance")
        print("3. Search Attendance by Name")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            add_attendance()
        elif choice == "2":
            view_attendance()
        elif choice == "3":
            search_attendance()
        elif choice == "4":
            print("👋 Exiting program... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    
    try:
        with open(FILENAME, "x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Date", "Status"])
    except FileExistsError:
        pass  

    main()

