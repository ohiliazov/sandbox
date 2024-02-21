numbers = set()
while True:
    input_data = input("Enter numbers (or leave empty to proceed): ").strip()

    new_numbers = input_data.strip().split()

    if not new_numbers:
        break

    numbers |= {n for n in map(int, new_numbers) if n % 5 != 0}

print(sorted(numbers))
