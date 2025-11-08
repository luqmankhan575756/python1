import csv
from datetime import datetime

# File name
FILENAME = "attendance.csv"

# ✅ Function to add attendance
def add_attendance():
    name = input("Enter student name: ").strip()
    status = input("Enter status (Present/Absent): ").strip().capitalize()
    date = datetime.now().strftime("%Y-%m-%d")

    # Open file in append mode
    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, date, status])
    
    print(f"✅ Attendance marked for {name} on {date} as {status}")

# ✅ Function to view all attendance
def view_attendance():
    try:
        with open(FILENAME, "r") as file:
            reader = csv.reader(file)
            print("\n--- Attendance Record ---")
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("⚠️ No attendance record found yet!")

# ✅ Function to search attendance by name
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

# ✅ Main menu
def main():
    while True:
        print("\n===== Attendance Management System =====")
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

# ✅ Run the program
if __name__ == "__main__":
    # Create file header if file doesn't exist
    try:
        with open(FILENAME, "x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Date", "Status"])
    except FileExistsError:
        pass  # File already exists

    main()
