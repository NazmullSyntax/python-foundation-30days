"""
Day 4: Input & Output
Learn how to take input from the user and format output beautifully.
"""

print("=" * 55)
print("PART 1: BASIC OUTPUT WITH print()")
print("=" * 55)

# 1. Simple print
print("Hello!")

# 2. Multiple values (Python adds spaces between them)
print("Name:", "Alex", "Age:", 25)

# 3. Custom separator
print("apple", "banana", "cherry", sep=", ")
print("2026", "10", "02", sep="-")

# 4. Custom end character
print("Loading", end="")
print(".", end="")
print(".", end="")
print(".")
# Output: Loading...

# 5. Escape characters
print("Line1\nLine2")            # \n = new line
print("Name:\tAlex")             # \t = tab
print("She said \"hi\"")          # \" = quote inside string
print("Path: C:\\Users\\Alex")    # \\ = single backslash


print("\n" + "=" * 55)
print("PART 2: TAKING INPUT WITH input()")
print("=" * 55)

# input() ALWAYS returns a string
name = input("Enter your name: ")
print(f"Hello, {name}!")

# If you need a number, convert it
age_str = input("Enter your age: ")
age = int(age_str)               # convert string → int
print(f"Next year you'll be {age + 1}.")

# Shorter (one line)
age2 = int(input("Enter your age again: "))
print(f"Double your age = {age2 * 2}")

# Float input
height = float(input("Enter your height in meters: "))
print(f"Your height is {height} m")

# Note: Once you call input(), the program WAITS until the user types something
# and presses Enter.


print("\n" + "=" * 55)
print("PART 3: THREE WAYS TO FORMAT STRINGS")
print("=" * 55)

name = "Alex"
age = 25
height = 1.75

# Method 1: Old style (%, like C)
print("Method 1 (%%): %s is %d years old." % (name, age))

# Method 2: str.format()
print("Method 2 (format): {} is {} years old.".format(name, age))

# Method 3: f-strings (BEST — Python 3.6+)
print(f"Method 3 (f-string): {name} is {age} years old.")


print("\n" + "=" * 55)
print("PART 4: F-STRING POWER FEATURES")
print("=" * 55)

# 1. Expressions inside {}
a = 5
b = 3
print(f"{a} + {b} = {a + b}")
print(f"{a} × {b} = {a * b}")

# 2. Function calls inside {}
print(f"Uppercase name: {name.upper()}")
print(f"Name length: {len(name)}")

# 3. Decimal places
pi = 3.14159265
print(f"Pi (2 decimals): {pi:.2f}")
print(f"Pi (4 decimals): {pi:.4f}")

# 4. Padding and alignment
print(f"|{name:<10}|")   # left-align, width 10
print(f"|{name:>10}|")   # right-align
print(f"|{name:^10}|")   # center

# 5. Numbers with commas
big = 1234567890
print(f"With commas: {big:,}")

# 6. Percentages
score = 0.856
print(f"Score: {score:.1%}")   # 85.6%

# 7. Mixed
price = 1299.5
print(f"Price: ${price:,.2f}")


print("\n" + "=" * 55)
print("PART 5: A SMALL PROFILE BUILDER")
print("=" * 55)

# Simulated user data
user_name = "Rahim"
user_age = 22
user_city = "Dhaka"
user_gpa = 3.75

print("=" * 40)
print("        STUDENT PROFILE")
print("=" * 40)
print(f"Name     : {user_name}")
print(f"Age      : {user_age}")
print(f"City     : {user_city}")
print(f"GPA      : {user_gpa:.2f}")
print("=" * 40)


print("\n" + "=" * 55)
print("PART 6: INTERACTIVE BILL CALCULATOR")
print("=" * 55)

# Comment out to skip interactive input during testing
print("(Pretend input: item=Pen, price=25.50, qty=4, tax=5)")

item = "Pen"
price = 25.50
quantity = 4
tax_percent = 5

subtotal = price * quantity
tax = subtotal * tax_percent / 100
total = subtotal + tax

print("\n" + "-" * 40)
print("            INVOICE")
print("-" * 40)
print(f"Item     : {item}")
print(f"Price    : ${price:.2f}")
print(f"Quantity : {quantity}")
print(f"Subtotal : ${subtotal:.2f}")
print(f"Tax ({tax_percent}%) : ${tax:.2f}")
print("-" * 40)
print(f"TOTAL    : ${total:.2f}")
print("-" * 40)