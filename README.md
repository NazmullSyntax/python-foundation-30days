# Python Foundation 30 Days

This repository contains beginner-friendly Python learning exercises and practice scripts for a 30-day foundation journey.

## Contents

- `day_one.py` - basic Python examples and print statements
- `day-four.py` - additional Python practice file
- `five.py` - simple Python beginner examples
- `day01_hello_world.ipynb` - notebook version of a Hello World exercise

## How to run

Use Python 3 to run any script:

```bash
python day_one.py
```

Or run a notebook in Jupyter Notebook or VS Code.

## Goal

Learn core Python concepts such as variables, data types, input/output, arithmetic, and beginner problem solving through daily practice.
# Chained comparison
if 18 <= age <= 65: ...

# match/case
match command:
    case "start": ...
    case _: ...

# Guard clause
if not item: return "No item"

# Comprehension filter
evens = [n for n in nums if n % 2 == 0]

# all / any
all(s >= 60 for s in scores)
any(s == 100 for s in scores)

# Walrus
if (n := len(data)) > 5: ...

# OR shortcut
if role in ("admin", "editor", "moderator"): ...