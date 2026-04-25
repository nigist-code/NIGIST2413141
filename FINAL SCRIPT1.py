equipment_list = []
bookings = {}

# ---------------- ADD EQUIPMENT ----------------
def add_equipment():
    name = input("Enter equipment name: ").strip()

    if name == "":
        print("Equipment name cannot be empty.\n")
        return

    if name in equipment_list:
        print("Equipment already exists.\n")
    else:
        equipment_list.append(name)
        bookings[name] = []
        print(f"{name} added successfully.\n")


# ---------------- RECORD BOOKING ----------------
def record_booking():
    equipment_name = input("Enter equipment name: ").strip()

    if equipment_name not in equipment_list:
        print("Equipment not found.\n")
        return

    student_name = input("Enter student name: ").strip()
    date = input("Enter booking date (YYYY-MM-DD): ").strip()

    if student_name == "" or date == "":
        print("Invalid input. Fields cannot be empty.\n")
        return

    # Prevent duplicate booking (same student, same date)
    for booking in bookings[equipment_name]:
        if booking["student"] == student_name and booking["date"] == date:
            print("This student already booked this equipment on this date.\n")
            return

    bookings[equipment_name].append({
        "student": student_name,
        "date": date
    })

    print("Booking recorded successfully.\n")


# ---------------- VIEW BOOKINGS ----------------
def view_bookings():
    print("\n===== ALL BOOKING RECORDS =====\n")

    if not equipment_list:
        print("No equipment available.\n")
        return

    for item in equipment_list:
        print(f"Equipment: {item}")

        booking_list = bookings.get(item, [])

        if len(booking_list) == 0:
            print("  No bookings found.")
        else:
            for b in booking_list:
                print(f"  Student: {b['student']} | Date: {b['date']}")

        print("-" * 30)


# ---------------- SEARCH BOOKINGS ----------------
def search_bookings():
    search_term = input("Enter student or equipment name: ").strip().lower()

    found = False

    for item in equipment_list:

        # Search by equipment
        if search_term in item.lower():
            print(f"\nEquipment: {item}")

            for b in bookings.get(item, []):
                print(f"  Student: {b['student']} | Date: {b['date']}")

            found = True

        # Search by student
        for b in bookings.get(item, []):
            if search_term in b["student"].lower():
                print(f"\nEquipment: {item}")
                print(f"  Student: {b['student']} | Date: {b['date']}")
                found = True

    if not found:
        print("No matching records found.\n")


# ---------------- MENU ----------------
def menu():
    while True:
        print("\n=== Equipment Booking System ===")
        print("1. Add Equipment")
        print("2. Record Booking")
        print("3. View Bookings")
        print("4. Search Bookings")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_equipment()
        elif choice == "2":
            record_booking()
        elif choice == "3":
            view_bookings()
        elif choice == "4":
            search_bookings()
        elif choice == "5":
            print("Exiting system...")
            break
        else:
            print("Invalid choice. Please try again.\n")


# ---------------- START PROGRAM ----------------
menu()