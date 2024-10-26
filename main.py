class Party:
    def __init__(self, name, date, budget):
        self.name = name
        self.date = date
        self.budget = budget
        self.guests = []
        self.todo_list = []
        self.expenses = 0

    def add_guest(self, name):
        self.guests.append({'name': name, 'RSVP': False})
        print(f"Added guest: {name}")

    def set_rsvp(self, name, response):
        for guest in self.guests:
            if guest['name'] == name:
                guest['RSVP'] = response
                status = "attending" if response else "not attending"
                print(f"{name} is now marked as {status}.")
                return
        print(f"Guest {name} not found.")

    def add_todo_item(self, item):
        self.todo_list.append({'item': item, 'done': False})
        print(f"Added to-do item: {item}")

    def mark_todo_done(self, item):
        for todo in self.todo_list:
            if todo['item'] == item:
                todo['done'] = True
                print(f"Marked '{item}' as done.")
                return
        print(f"To-do item '{item}' not found.")

    def add_expense(self, amount):
        self.expenses += amount
        print(f"Added expense of ${amount:.2f}. Total expenses now: ${self.expenses:.2f}")

    def get_summary(self):
        print("\n--- Party Summary ---")
        print(f"Party Name: {self.name}")
        print(f"Date: {self.date}")
        print(f"Budget: ${self.budget:.2f}")
        print(f"Total Expenses: ${self.expenses:.2f}")
        print("\nGuests:")
        for guest in self.guests:
            status = "RSVP: Yes" if guest['RSVP'] else "RSVP: No"
            print(f" - {guest['name']} ({status})")
        print("\nTo-Do List:")
        for todo in self.todo_list:
            status = "Done" if todo['done'] else "Not Done"
            print(f" - {todo['item']} ({status})")
        print("\n---------------------")

# CLI functions for interacting with the app

def main():
    print("Welcome to the Party Planner!")
    name = input("Enter the party name: ")
    date = input("Enter the party date (e.g., 2023-12-31): ")
    budget = float(input("Enter your budget: $"))

    party = Party(name, date, budget)

    while True:
        print("\n--- Party Planner Menu ---")
        print("1. Add Guest")
        print("2. Set RSVP")
        print("3. Add To-Do Item")
        print("4. Mark To-Do Item as Done")
        print("5. Add Expense")
        print("6. View Summary")
        print("7. Quit")

        choice = input("Choose an option: ")

        if choice == '1':
            guest_name = input("Enter guest name: ")
            party.add_guest(guest_name)
        elif choice == '2':
            guest_name = input("Enter guest name for RSVP: ")
            rsvp = input("Is the guest attending? (yes/no): ").lower() == 'yes'
            party.set_rsvp(guest_name, rsvp)
        elif choice == '3':
            todo_item = input("Enter a to-do item: ")
            party.add_todo_item(todo_item)
        elif choice == '4':
            todo_item = input("Enter the to-do item to mark as done: ")
            party.mark_todo_done(todo_item)
        elif choice == '5':
            amount = float(input("Enter expense amount: $"))
            party.add_expense(amount)
        elif choice == '6':
            party.get_summary()
        elif choice == '7':
            print("Exiting Party Planner. Have a great party!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
