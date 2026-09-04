# task5_contact_book.py
contacts = {}

def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    address = input("Address: ")
    contacts[name] = {"phone": phone, "email": email, "address": address}
    print("Contact added!")

def view_contacts():
    for name, info in contacts.items():
        print(f"{name} - {info['phone']}")

def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        print("Details:", contacts[name])
    else:
        print("Not found!")

def update_contact():
    name = input("Enter name to update: ")
    if name in contacts:
        phone = input("New phone: ")
        email = input("New email: ")
        address = input("New address: ")
        contacts[name] = {"phone": phone, "email": email, "address": address}
        print("Updated!")
    else:
        print("Not found!")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Deleted!")
    else:
        print("Not found!")

while True:
    print("\n--- CONTACT BOOK ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter choice: ")
    if choice == "1": add_contact()
    elif choice == "2": view_contacts()
    elif choice == "3": search_contact()
    elif choice == "4": update_contact()
    elif choice == "5": delete_contact()
    elif choice == "6": break
    else: print("Invalid choice!")
