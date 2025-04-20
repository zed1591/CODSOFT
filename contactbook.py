import re

def add_contact(contacts, Name, Phone, Email, Address):
    if not isinstance(Name, str) or Name.isdigit():
        print("Invalid name. Name must be a string and cannot be a number.")
        return contacts

    if not re.match(r'^\+?\d+$', Phone):
        print("Invalid phone number. Phone number must contain only digits and an optional '+' sign.")
        return contacts
    if '@' not in Email:
        print("Invalid email. Email must contain '@'.")
        return contacts
    
    contacts[Name] = {'Phone': Phone, 'Email': Email, 'Address': Address}
    print("contact added succesfully!")
    return contacts

def view_contacts(contacts):
    if not contacts:
        print(" sorry! No contacts registered.")
    else:
        for Name, details in contacts.items():
            print(f"Name: {Name}, Phone: {details['Phone']}")

def search_contact(contacts, search_term):
    found = False
    search_term_lower=search_term.lower()
    for Name, details in contacts.items():
        if search_term in Name.lower() or search_term_lower in details['Phone'].lower():
            print(f"Name: {Name}, Phone: {details['Phone']}, Email: {details['Email']}, Address: {details['Address']}")
            found = True
    if not found:
        print("No contact found with that name or phone number.")

def update_contact(contacts, Name,Phone=None, Email=None, Address=None):
    if Name in contacts:
        if Phone and not re.match(r'^\+?\d+$', Phone):
            print("Invalid phone number. Phone number must contain only digits and an optional '+' sign.")
            return contacts
        if Email and '@' not in Email:
            print("Invalid email. Email must contain '@'.")
            return contacts
        
        if Phone:
            contacts[Name]['phone'] = Phone
        if Email:
            contacts[Name]['email'] = Email
        if Address:
            contacts[Name]['address'] = Address
            print("contact update successfully!")
    else:
        print("No contact found with that name.")
    return contacts
    
def delete_contact(contacts, Name):
    if Name in contacts:
        confirmation = input(f"Are you sure you want to delete the contact '{Name}'? (yes/no): ")
        if confirmation.lower() == 'yes':
            del contacts[Name]
            print("Contact deleted successfully! ")
        else:
            print("Deletion cancelled.")
    else:
        print("No contact found with that name.")
    return contacts


def main():
    contacts = {}
    while True:
        print("\n=======Contact Book==========")
        print("\n1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("\nEnter your choice: ")
        
        if choice == '1':
            while True:
                Name = input("\nEnter name: ")
                if isinstance(Name, str) and not Name.isdigit():
                    break
                else:
                    print("Invalid name. Name must be a string and cannot be a number.")
            while True:
                Phone = input("Enter phone: ")
                if re.match(r'^\+?\d+$', Phone):
                    break
                else:
                    print("Invalid phone number. Phone number must contain only digits and an optional '+' sign.")
            while True:
                Email = input("Enter email: ")
                if '@' in Email:
                    break
                else:
                    print("Invalid email. Email must contain '@'.")
            Address = input("Enter address: ")
            contacts = add_contact(contacts, Name, Phone, Email, Address)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_term = input("\nEnter name or phone number to search: ")
            search_contact(contacts, search_term)
        elif choice == '4':
            name = input("\nEnter name of the contact to update: ")
            if name in contacts:

                Phone = input("Enter new phone (leave blank to keep current): ")
                Email = input("Enter new email (leave blank to keep current): ")
                Address = input("Enter new address (leave blank to keep current): ")
                contacts = update_contact(contacts, name, Phone, Email, Address)
            else:
                print("No contact found with that name.")
        elif choice == '5':
            name = input("\nEnter name of the contact to delete: ")
            contacts = delete_contact(contacts, name)

        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
