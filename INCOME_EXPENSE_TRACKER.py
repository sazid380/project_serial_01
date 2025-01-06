class ExpenseTracker:
    def __init__(self):
        self.income = 0
        self.expenses = {category: 0 for category in ["RENT","MEAL", "TRANSPORT CONVEYANCE", "GROCERY","MEDICAL", "EXTRA"]}

    def add_income(self, amount):
        self.income += amount
        print(" ")

        print(f"Income of {amount} taka added successfully!")

    def add_expense(self, category, amount):
        if category in self.expenses:
            self.expenses[category] += amount
            print(" ")
            print(f"Expense of {amount} taka added to category '{category}' successfully!")
        else:
            print(f"Invalid category '{category}'!!! Please use a predefined category.")

    def calculate_savings(self):
        total_expenses = sum(self.expenses.values())
        return self.income - total_expenses

    def display_summary(self):
        print("\nExpense Summary:")
        print(" ")
        for category, amount in self.expenses.items():
            print(f"{category}: {amount}","Taka")
        print("\nTotal Income:  ", self.income, "Taka")
        print("Total Expenses:", sum(self.expenses.values()),"Taka")
        print("Total Savings: ", self.calculate_savings(), "Taka")

    def show_categories(self):
        print("\nAvailable Expense Categories:")
        for category in self.expenses.keys():
            print("-", category)

# Main Program
if __name__ == "__main__":
    tracker = ExpenseTracker()

    while True:
        print("\nINCOME-EXPENSE TRACKER CALCULATOR")
        print("\nWelcome to MENU")
        print("")
        print("Choice 1: Add Income")
        print("Choice 2: Add Expense")
        print("Choice 3: Display Summary")
        print("Choice 4: Exit")
      
        print("")
        choice = input("Enter your choice: ")
        print("")

        if choice == '1':
            amount = float(input("Enter income amount in BDT: "))
            tracker.add_income(amount)
        elif choice == '2':
            tracker.show_categories()
            category = input("Enter expense category: ").upper()
            amount = float(input("Enter expense amount in BDT: "))
            tracker.add_expense(category, amount)
        elif choice == '3':
            tracker.display_summary()
       
        elif choice == '4':
            print("Exiting Tracker!")
            break
        else:
            print("Wrong Credentials! Please try again...")
