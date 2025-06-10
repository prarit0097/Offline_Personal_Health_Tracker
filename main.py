from tracker import add_new_entry, view_all_entries,search_by_date,search_and_update
from file_handler import initialize_file

# First file initialize (header check & create)
initialize_file()

def show_menu():
    while True:
        print("\n📊 Personal Health Tracker")
        print("1. ➕ Add New Entry")
        print("2. 👀 View All Entries")
        print("3. 🔍 Search Entry by Date")
        # print("4. ✏️ Update Entry by Date + Name")
        print("0. ❌ Exit")

        choice = input("👉 Enter your choice: ")

        if choice == '1':
            add_new_entry()
        elif choice == '2':
            view_all_entries()
        elif choice == '3':
            search_by_date()
        # elif choice == '4':
        #     search_and_update()
        elif choice == '0':
            print("👋 Exiting the app. Stay Healthy!")
            break

        else:
            print("⚠️ Invalid choice! Try again.")


# Start the menu
show_menu()

