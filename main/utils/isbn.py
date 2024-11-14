import random


def generate_isbn():
    # Generate the first 12 digits of ISBN-13
    isbn_base = [str(random.randint(0, 9)) for _ in range(12)]

    # Calculated control discharge
    total = sum(
        int(num) * (1 if idx % 2 == 0 else 3) for idx, num in enumerate(isbn_base)
    )
    check_digit = (10 - (total % 10)) % 10

    isbn_base.append(str(check_digit))

    return "".join(isbn_base)