donors = []


def add_donor():
    name = input("Enter name: ")
    blood = input("Enter blood group: ")
    place = input("Enter location: ")
    phone = input("Enter contact number: ")

    donors.append({
        "name": name,
        "blood": blood,
        "place": place,
        "phone": phone
    })
    print("Donor added successfully!\n")


def search_donor():
    bg = input("Enter blood group to search: ")
    found = False

    for d in donors:
        if d["blood"].lower() == bg.lower():
            print("\nName:", d["name"])
            print("Location:", d["place"])
            print("Contact:", d["phone"])
            print("-" * 20)
            found = True

    if not found:
        print("No donor found for this blood group.\n")


while True:
    print("\n--- Blood Donor Finder System ---")
    print("1. Add Donor")
    print("2. Search Donor")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_donor()
    elif choice == "2":
        search_donor()
    elif choice == "3":
        print("Thank you!")
        break
    else:
        print("Invalid choice, try again.")
