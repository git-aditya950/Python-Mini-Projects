# 📞 Phonebook App - by Aditya

phonebook = {}

def add_contact():
    name = input("Enter contact name: ").strip().capitalize()
    number = input("Enter phone number: ").strip()
    
    if name in phonebook:
        print("⚠️ Contact already exists!")
    else:
        phonebook[name] = number
        print(f"✅ {name} added to phonebook.")

def view_contacts():
    if not phonebook:
        print("📭 Phonebook is empty.")
    else:
        print("\n📖 Your Contacts:")
        for name, number in phonebook.items():
            print(f"📇 {name}: {number}")

def search_contact():
    name = input("Enter name to search: ").strip().capitalize()
    if name in phonebook:
        print(f"🔍 Found: {name} → {phonebook[name]}")
    else:
        print("❌ Contact not found.")

def delete_contact():
    name = input("Enter name to delete: ").strip().capitalize()
    if name in phonebook:
        del phonebook[name]
        print(f"🗑️ {name} deleted from phonebook.")
    else:
        print("❌ Contact not found.")

def show_menu():
    print("\n📱 Phonebook Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

def main():
    print("📞 Welcome to Aditya's Phonebook App")

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
