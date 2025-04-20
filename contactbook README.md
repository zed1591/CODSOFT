# Contact Book Application in Python

This Python code implements a simple Contact Book application that allows users to store, view, search, update, and delete contact information. It utilizes basic Python data structures (dictionaries) and regular expressions for input validation.

## Code Description

The code consists of the following functions:

* **`add_contact(contacts, Name, Phone, Email, Address)`:**
    * Adds a new contact to the contact book.
    * Performs basic validation on the `Name` (must be a string and not a number), `Phone` (must contain only digits and an optional '+' sign), and `Email` (must contain '@').
    * Stores the contact details in the `contacts` dictionary.

* **`view_contacts(contacts)`:**
    * Displays all registered contacts, showing their name and phone number.
    * Handles the case where no contacts are registered.

* **`search_contact(contacts, search_term)`:**
    * Searches for contacts by name or phone number (case-insensitive).
    * Displays the full details (Name, Phone, Email, Address) of any matching contacts.
    * Indicates if no contact is found.

* **`update_contact(contacts, Name, phone=None, email=None, Address=None)`:**
    * Updates the phone number, email, or address of an existing contact.
    * Performs basic validation on the new phone and email if provided.
    * Handles the case where the contact to update is not found.

* **`delete_contact(contacts, Name)`:**
    * Deletes a contact from the contact book based on their name.
    * Handles the case where the contact to delete is not found.

* **`main()`:**
    * The main function that runs the Contact Book application.
    * Provides a menu-driven command-line interface.
    * Allows users to choose from adding, viewing, searching, updating, deleting contacts, or exiting the application.
    * Takes user input and calls the appropriate functions.
    * Includes basic input validation loops for adding contacts.

## How to Run the Code

1.  Save the code as a Python file (e.g., `contact_book.py`).
2.  Open a terminal or command prompt.
3.  Navigate to the directory where you saved the file.
4.  Run the script using the command: `python contact_book.py`
5.  Follow the on-screen menu to interact with the Contact Book application.

## Features

* **Add Contacts:** Easily add new contacts with name, phone, email, and address.
* **View Contacts:** See a list of all saved contacts with their names and phone numbers.
* **Search Contacts:** Find contacts by name or phone number.
* **Update Contacts:** Modify the details of existing contacts.
* **Delete Contacts:** Remove contacts from the book.
* **Input Validation:** Basic validation for name, phone number, and email format during contact addition and update.
* **Simple Command-Line Interface:** User-friendly menu for interacting with the application.
