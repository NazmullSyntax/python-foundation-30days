# # # # # # print("Loading", end="")
# # # # # # print(".", end="")
# # # # # # print(".", end="")
# # # # # # # print(".")

# # # # # a = 5
# # # # # b = 3
# # # # # print(f"{a} + {b} = {a + b}")   # 5 + 3 = 8
# # # # # print(f"{a} * {b} = {a * b}")   # 5 * 3 = 15

# # # # big = 1234567890
# # # # print(f"{big:,}")    # 1,234,567,890

# # # # name = input("What's your name? ")
# # # # print(f"Hello, {name}! Welcome to Python.")

# # # # What's your name? Alex
# # # # Hello, Alex! Welcome to Python.

# # # Example 2: Age calculator
# # # name = input("Name: ")
# # # birth_year = int(input("Birth year: "))
# # # current_year = 2026
# # # age = current_year - birth_year

# # # print(f"\n{name}, you are {age} years old.")
# # # print(f"Next year you'll turn {age + 1}.")

# # # Example 3: Bill / invoice

# # item = input("Item name: ")
# # price = float(input("Price: "))
# # qty = int(input("Quantity: "))
# # tax_percent = 5

# # subtotal = price * qty
# # tax = subtotal * tax_percent / 100
# # total = subtotal + tax

# # print("\n" + "-" * 40)
# # print("            INVOICE")
# # print("-" * 40)
# # print(f"Item     : {item}")
# # print(f"Price    : ${price:.2f}")
# # print(f"Quantity : {qty}")
# # print(f"Subtotal : ${subtotal:.2f}")
# # print(f"Tax ({tax_percent}%) : ${tax:.2f}")
# # print("-" * 40)
# # print(f"TOTAL    : ${total:,.2f}")
# # print("-" * 40)

# Example 4: Profile card

name = input("Full name: ")
age = int(input("Age: "))
city = input("City: ")
gpa = float(input("GPA: "))

print("\n" + "=" * 40)
print("        STUDENT PROFILE")
print("=" * 40)
print(f"Name     : {name}")
print(f"Age      : {age}")
print(f"City     : {city}")
print(f"GPA      : {gpa:.2f}")
print("=" * 40)