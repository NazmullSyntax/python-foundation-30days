# # # print("Loading", end="")
# # # print(".", end="")
# # # print(".", end="")
# # # # print(".")

# # a = 5
# # b = 3
# # print(f"{a} + {b} = {a + b}")   # 5 + 3 = 8
# # print(f"{a} * {b} = {a * b}")   # 5 * 3 = 15

# big = 1234567890
# print(f"{big:,}")    # 1,234,567,890

# name = input("What's your name? ")
# print(f"Hello, {name}! Welcome to Python.")

# What's your name? Alex
# Hello, Alex! Welcome to Python.

Example 2: Age calculator
name = input("Name: ")
birth_year = int(input("Birth year: "))
current_year = 2026
age = current_year - birth_year

print(f"\n{name}, you are {age} years old.")
print(f"Next year you'll turn {age + 1}.")