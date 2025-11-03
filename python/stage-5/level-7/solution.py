contacts = []

def add_contact(name, phone, email):
    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }
    contacts.append(contact)

def find_contact(name):
    for c in contacts:
        if c["name"].lower() == name.lower():
            return c
    return None

def display_contact(contact):
    print("Name: " + contact["name"])
    print("Phone: " + contact["phone"])
    print("Email: " + contact["email"])

while True:
    print("\nContact Book")
    print("1. Add contact")
    print("2. Search")
    print("3. View all")
    print("4. Delete")
    print("5. Quit")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        add_contact(name, phone, email)
        print("Added!")

    elif choice == "2":
        name = input("Search for: ")
        c = find_contact(name)
        if c:
            display_contact(c)
        else:
            print("Not found")

    elif choice == "3":
        for c in contacts:
            display_contact(c)
            print()

    elif choice == "4":
        name = input("Delete who: ")
        c = find_contact(name)
        if c:
            contacts.remove(c)
            print("Deleted!")
        else:
            print("Not found")

    elif choice == "5":
        break

print("Goodbye!")
