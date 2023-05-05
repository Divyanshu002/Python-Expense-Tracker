import openpyxl

# Define the initial balance in INR
balance = 0

# Create a function to record an expense
def record_expense(amount, description, wb):
    global balance
    balance -= amount
    print(f"Expense recorded: ₹{amount} - {description}")
    print(f"Current balance: ₹{balance}")
    sheet = wb.active
    sheet.append(["Expense", amount, description, balance])
    wb.save("Data.xlsx")

# Create a function to record an income
def record_income(amount, description, wb):
    global balance
    balance += amount
    print(f"Income recorded: ₹{amount} - {description}")
    print(f"Current balance: ₹{balance}")
    sheet = wb.active
    sheet.append(["Income", amount, description, balance])
    wb.save("Data.xlsx")

# Create a function to display the current balance
def display_balance():
    global balance
    print(f"Current balance: ₹{balance}")

# Main program loop
wb = openpyxl.Workbook()
sheet = wb.active
sheet.append(["Type", "Amount", "Description", "Balance"])

while True:
    print("Enter 'e' to record an expense, 'i' to record an income, 'b' to display the current balance, or 'q' to quit.")
    choice = input("> ")
    
    if choice == "e":
        amount = float(input("Enter the expense amount in INR: "))
        description = input("Enter a description of the expense: ")
        record_expense(amount, description, wb)
    elif choice == "i":
        amount = float(input("Enter the income amount in INR: "))
        description = input("Enter a description of the income: ")
        record_income(amount, description, wb)
    elif choice == "b":
        display_balance()
    elif choice == "q":
        break
    else:
        print("Invalid choice. Please try again.")

wb.close()
