"""
Day 6: Advanced Conditionals
Level up your if/else skills.
"""

print("=" * 60)
print("PART 1: CHAINED COMPARISONS")
print("=" * 60)

age = 25

# ❌ Verbose way
if age >= 18 and age <= 65:
    print("Working age (verbose)")

# ✅ Chained comparison (Python-only superpower)
if 18 <= age <= 65:
    print("Working age (chained)")

# More examples
x = 5
print(f"0 < {x} < 10 -> {0 < x < 10}")     # True
print(f"10 < {x} < 20 -> {10 < x < 20}")   # False

# With floats
temp = 98.6
print(f"97 <= {temp} <= 99 -> {97 <= temp <= 99}")


print("\n" + "=" * 60)
print("PART 2: match / case (Python 3.10+)")
print("=" * 60)

command = "start"

match command:
    case "start":
        print("Starting the engine...")
    case "stop":
        print("Stopping the engine...")
    case "pause":
        print("Pausing...")
    case _:
        print("Unknown command.")

# Multiple values in one case
day = "Saturday"

match day:
    case "Saturday" | "Sunday":
        print("It's the weekend!")
    case "Monday":
        print("Back to work...")
    case _:
        print("Regular weekday.")

# With conditions (guard clause inside case)
num = 15

match num:
    case n if n < 0:
        print(f"{n} is negative")
    case 0:
        print("Zero")
    case n if n % 2 == 0:
        print(f"{n} is even")
    case _:
        print(f"{n} is odd")


print("\n" + "=" * 60)
print("PART 3: GUARD CLAUSES (Early Return)")
print("=" * 60)

def process_order(item, quantity, price):
    # Guard clauses — check bad cases FIRST, then proceed
    if not item:
        return "Error: No item provided."
    if quantity <= 0:
        return "Error: Invalid quantity."
    if price <= 0:
        return "Error: Invalid price."

    # Happy path (only reached if all guards passed)
    total = quantity * price
    return f"Order OK. Total = ${total:.2f}"

print(process_order("Pen", 5, 1.5))
print(process_order("", 5, 1.5))
print(process_order("Pen", -2, 1.5))
print(process_order("Pen", 5, 0))


print("\n" + "=" * 60)
print("PART 4: CONDITIONAL EXPRESSIONS IN COLLECTIONS")
print("=" * 60)

# List comprehension with condition
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = [n for n in numbers if n % 2 == 0]
print(f"Evens: {evens}")

odds = [n for n in numbers if n % 2 != 0]
print(f"Odds: {odds}")

# With if/else inside
labels = ["even" if n % 2 == 0 else "odd" for n in numbers]
print(f"Labels: {labels}")

# On strings
words = ["apple", "hi", "banana", "ok", "cherry"]
long_words = [w for w in words if len(w) > 3]
print(f"Long words: {long_words}")


print("\n" + "=" * 60)
print("PART 5: all() AND any()")
print("=" * 60)

scores = [85, 90, 78, 92, 88]

# all() — True if EVERY item is True
all_pass = all(s >= 60 for s in scores)
print(f"All passed (>=60): {all_pass}")

# any() — True if AT LEAST ONE item is True
any_perfect = any(s == 100 for s in scores)
print(f"Any perfect score: {any_perfect}")

any_below_50 = any(s < 50 for s in scores)
print(f"Any below 50: {any_below_50}")

# Practical: check if all required fields are filled
form = {"name": "Alex", "email": "", "age": 25}
all_filled = all(form.values())
print(f"Form fully filled: {all_filled}")

# Practical: check if user has any admin role
roles = ["user", "editor"]
has_admin = any(r in ("admin", "superadmin") for r in roles)
print(f"Has admin role: {has_admin}")


print("\n" + "=" * 60)
print("PART 6: WALRUS OPERATOR := (Python 3.8+)")
print("=" * 60)

# Without walrus: compute twice
value = input("Enter text (or press Enter): ")
# (In real code, you might not want to call input() twice)
# if len(input("Enter text: ")) > 5:
#     print("Long input")

# With walrus: compute once, use in condition
data = "hello world"
if (n := len(data)) > 5:
    print(f"'{data}' has {n} characters (long)")

# In while loops
# count = 0
# while (line := input("> ")) != "quit":
#     print(f"You typed: {line}")

# In comprehensions
values = [10, 20, 30, 40, 50]
filtered = [y for x in values if (y := x * 2) > 50]
print(f"Doubled values > 50: {filtered}")


print("\n" + "=" * 60)
print("PART 7: COMMON PATTERNS")
print("=" * 60)

# Pattern 1: Value between range
def is_teenager(age):
    return 13 <= age <= 19

print(f"is_teenager(15): {is_teenager(15)}")
print(f"is_teenager(25): {is_teenager(25)}")

# Pattern 2: Multiple OR conditions using 'in'
role = "editor"
if role in ("admin", "editor", "moderator"):
    print(f"{role} has write access.")

# Instead of:
# if role == "admin" or role == "editor" or role == "moderator":

# Pattern 3: Default values with 'or'
name = ""
display_name = name or "Guest"
print(f"Display name: {display_name}")

# Pattern 4: Safe navigation
user = {"name": "Alex", "age": None}
age = user.get("age") or "unknown"
print(f"Age: {age}")


print("\n" + "=" * 60)
print("PART 8: REFACTORING EXAMPLE")
print("=" * 60)

# ❌ Before: messy, deep nesting
def classify_bmi_bad(bmi):
    if bmi is not None:
        if bmi > 0:
            if bmi < 18.5:
                return "Underweight"
            else:
                if bmi < 25:
                    return "Normal"
                else:
                    if bmi < 30:
                        return "Overweight"
                    else:
                        return "Obese"
        else:
            return "Invalid"
    else:
        return "Missing"

# ✅ After: guard clauses + flat structure
def classify_bmi_good(bmi):
    if bmi is None:
        return "Missing"
    if bmi <= 0:
        return "Invalid"
    if bmi < 18.5:
        return "Underweight"
    if bmi < 25:
        return "Normal"
    if bmi < 30:
        return "Overweight"
    return "Obese"

for b in [None, -5, 17, 22, 27, 35]:
    print(f"BMI {b}: {classify_bmi_good(b)}")


print("\n" + "=" * 60)
print("PART 9: MENU-DRIVEN PROGRAM")
print("=" * 60)

def calculator(a, op, b):
    match op:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            if b == 0:
                return "Error: Division by zero"
            return a / b
        case _:
            return f"Unknown operator: {op}"

print(calculator(10, "+", 5))     # 15
print(calculator(10, "-", 5))     # 5
print(calculator(10, "*", 5))     # 50
print(calculator(10, "/", 5))     # 2.0
print(calculator(10, "/", 0))     # Error
print(calculator(10, "%", 5))     # Unknown