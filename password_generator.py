"""
Password Generator
------------------
A simple command-line tool that generates strong, random passwords.
Author: Your Name
"""

import random
import string


# ── Character sets ──────────────────────────────────────────────
LOWERCASE = string.ascii_lowercase        # a-z
UPPERCASE = string.ascii_uppercase        # A-Z
DIGITS    = string.digits                 # 0-9
SYMBOLS   = "!@#$%^&*()-_=+[]{}|;:,.<>?" # special characters


def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True):
    """
    Generate a random password.

    Parameters:
        length      (int)  : how many characters long (default 12)
        use_upper   (bool) : include uppercase letters  (default True)
        use_digits  (bool) : include numbers            (default True)
        use_symbols (bool) : include special characters (default True)

    Returns:
        str : the generated password
    """

    # Always start with lowercase letters
    characters = LOWERCASE

    # Add more character types based on user choices
    if use_upper:
        characters += UPPERCASE
    if use_digits:
        characters += DIGITS
    if use_symbols:
        characters += SYMBOLS

    # Build the password — guarantee at least one of each chosen type
    password = []

    password.append(random.choice(LOWERCASE))
    if use_upper:
        password.append(random.choice(UPPERCASE))
    if use_digits:
        password.append(random.choice(DIGITS))
    if use_symbols:
        password.append(random.choice(SYMBOLS))

    # Fill the rest of the password with random characters
    remaining = length - len(password)
    for _ in range(remaining):
        password.append(random.choice(characters))

    # Shuffle so the guaranteed characters aren't always at the start
    random.shuffle(password)

    return "".join(password)


def check_strength(password):
    """
    Check how strong a password is.

    Returns:
        str : 'Weak', 'Medium', 'Strong', or 'Very Strong'
    """
    score = 0

    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if any(c in UPPERCASE for c in password):
        score += 1
    if any(c in DIGITS for c in password):
        score += 1
    if any(c in SYMBOLS for c in password):
        score += 1

    if score <= 1:
        return "Weak"
    elif score == 2:
        return "Medium"
    elif score == 3:
        return "Strong"
    else:
        return "Very Strong"


def get_yes_no(prompt):
    """Ask a yes/no question and return True for yes, False for no."""
    while True:
        answer = input(prompt + " (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        elif answer in ("n", "no"):
            return False
        else:
            print("  Please type y or n.")


def get_number(prompt, min_val, max_val):
    """Ask for a number between min_val and max_val."""
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"  Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("  That's not a valid number. Try again.")


def main():
    print("=" * 45)
    print("       PASSWORD GENERATOR")
    print("=" * 45)

    while True:
        print()

        # ── Ask the user what they want ──────────────────
        length      = get_number("Password length (8–64): ", 8, 64)
        use_upper   = get_yes_no("Include uppercase letters? (A-Z)")
        use_digits  = get_yes_no("Include numbers?          (0-9)")
        use_symbols = get_yes_no("Include special symbols?  (!@#...)")
        how_many    = get_number("How many passwords to generate? (1–10): ", 1, 10)

        print()
        print("-" * 45)
        print(f"  Generated {how_many} password(s):")
        print("-" * 45)

        # ── Generate and display passwords ───────────────
        for i in range(how_many):
            pwd      = generate_password(length, use_upper, use_digits, use_symbols)
            strength = check_strength(pwd)
            print(f"  {i+1}. {pwd}   [{strength}]")

        print("-" * 45)

        # ── Ask if they want to go again ─────────────────
        print()
        again = get_yes_no("Generate more passwords?")
        if not again:
            print()
            print("  Stay safe online!")
            print("=" * 45)
            break


if __name__ == "__main__":
    main()
