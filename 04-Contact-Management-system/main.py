
# Contact Management System
# A simple command-line application for managing contacts.

# Store contacts as key-value pairs:
# The contact name is the key and the phone number is the value.
contacts = {}


# Add a new contact to the dictionary.
def add_contact(name, number):
    if not name or not number:
        print("Name and phone number cannot be empty.")
        return

    if name in contacts:
        print("This contact already exists.")
        return

    contacts[name] = number
    print(f"Contact '{name}' added successfully.")


# Edit an existing contact.
def edit_contact():
    if not contacts:
        print("There are no contacts to edit.")
        return

    old_name = input("Enter the contact name: ")

    if old_name not in contacts:
        print("Contact not found.")
        return

    new_name = input("Enter the new name: ")
    new_number = input("Enter the new phone number: ")

    if not new_name or not new_number:
        print("Name and phone number cannot be empty.")
        return

    if new_name != old_name and new_name in contacts:
        print("A contact with this name already exists.")
        return

    # Remove the old entry and save the updated contact.
    del contacts[old_name]
    contacts[new_name] = new_number

    print(f"Contact '{new_name}' updated successfully.")


# Delete an existing contact.
def delete_contact():
    if not contacts:
        print("There are no contacts to delete.")
        return

    name = input("Enter the contact name to delete: ")

    if name not in contacts:
        print("Contact not found.")
        return

    del contacts[name]
    print(f"Contact '{name}' deleted successfully.")


# Main program loop.
# Keep displaying the menu until the user chooses to exit.
while True:

    print("\nChoose an operation:")
    print("1. Add a contact")
    print("2. Delete a contact")
    print("3. Edit a contact")
    print("4. Exit")
    print("-----------------------------")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Contact name: ")
        phone = input("Phone number: ")
        add_contact(name, phone)

    elif choice == "2":
        delete_contact()

    elif choice == "3":
        print(contacts)
        edit_contact()

    elif choice == "4":
        print("Exiting the contact management system.")
        break

    else:
        print("Invalid option. Please try again.")

#thankyou for practicing with my github repository!