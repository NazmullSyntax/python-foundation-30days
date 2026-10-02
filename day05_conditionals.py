"""
Day 5: Conditionals
Learn how to make programs decide.
"""

print("=" * 55)
print("PART 1: BASIC if STATEMENT")
print("=" * 55)

age = 20

if age >= 18:
    print("You are an adult.")
    print("You can vote.")

print("This line always runs.")


print("\n" + "=" * 55)
print("PART 2: if / else")
print("=" * 55)

temperature = 30

if temperature > 25:
    print("It's hot outside.")
else:
    print("It's cool outside.")


print("\n" + "=" * 55)
print("PART 3: if / elif / else")
print("=" * 55)

score = 78

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score} -> Grade: {grade}")


print("\n" + "=" * 55)
print("PART 4: NESTED if")
print("=" * 55)

has_ticket = True
age = 25

if has_ticket:
    print("Ticket found.")
    if age >= 18:
        print("You may enter.")
    else:
        print("Too young to enter alone.")
else:
    print("No ticket. Please buy one.")


print("\n" + "=" * 55)
print("PART 5: TERNARY (one-line if-else)")
print("=" * 55)

age = 16
status = "adult" if age >= 18 else "minor"
print(f"Age {age} -> {status}")

# Equivalent long form:
if age >= 18:
    status2 = "adult"
else:
    status2 = "minor"
print(f"Long form result: {status2}")


print("\n" + "=" * 55)
print("PART 6: LOGICAL OPERATORS WITH if")
print("=" * 55)

username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login successful.")
else:
    print("Login failed.")

day = "Saturday"
if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")
else:
    print("It's a workday.")


print("\n" + "=" * 55)
print("PART 7: MEMBERSHIP WITH if")
print("=" * 55)

fruits = ["apple", "banana", "cherry"]
fruit = "banana"

if fruit in fruits:
    print(f"{fruit} is available.")
else:
    print(f"{fruit} is not available.")


print("\n" + "=" * 55)
print("PART 8: TRUTHY / FALSY VALUES")
print("=" * 55)

# Falsy: 0, "", [], {}, None, False
# Everything else is Truthy

values = [0, 1, "", "hi", [], [1], None, "False"]
for v in values:
    if v:
        print(f"{repr(v):10} -> Truthy")
    else:
        print(f"{repr(v):10} -> Falsy")


print("\n" + "=" * 55)
print("PART 9: REAL-WORLD EXAMPLE — LOGIN SYSTEM")
print("=" * 55)

# Simulated input (uncomment to make interactive)
# username = input("Username: ")
# password = input("Password: ")

username = "admin"
password = "secret"

if not username:
    print("❌ Username cannot be empty.")
elif not password:
    print("❌ Password cannot be empty.")
elif username == "admin" and password == "secret":
    print(f"✅ Welcome back, {username}!")
elif username == "admin":
    print("❌ Wrong password.")
else:
    print("❌ Unknown user.")


print("\n" + "=" * 55)
print("PART 10: REAL-WORLD EXAMPLE — BMI CALCULATOR")
print("=" * 55)

weight = 70     # kg
height = 1.75   # meters

bmi = weight / (height ** 2)
print(f"BMI = {bmi:.2f}")

if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

print(f"Category: {category}")