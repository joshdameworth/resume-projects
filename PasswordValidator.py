# Dictionary of special characters that are not allowed
special_chars = {
    "!" : 1,
    "@" : 2,
    "#" : 3,
    "$" : 4,
    "%" : 5,
    "^" : 6
}
# Functions that check all conditions (has a capital, lowercase, digit, no special characters, no repeating characters, no initials)
def has_upper(password):
    return any(c.isupper() for c in password)
def has_lower(password):
    return any(c.islower() for c in password)
def has_digit(password):
    return any(c.isdigit() for c in password)
def has_special(password):
    return any(c in special_chars for c in password)
def avoids_initials(password, initials):
    return all(c.upper() not in initials.upper() for c in password)
def no_repeating_chars(password):
    for i in range(1, len(password)):
        if password[i] == password[i - 1]:
            return False
    return True
def main():
    # Input the user's full name
    name = input("Input your first and last name: ").strip()
    name_parts = name.split()
    if len(name_parts) < 2:
        print("Please enter both first and last name.")
        return
    initials = name_parts[0][0] + name_parts[1][0]
    # Password input loop with validation checks
    while True:
        password = input("Input your password: ").strip()
        # Check password length
        if not (8 <= len(password) <= 12):
            print("Password must be between 8 and 12 characters.")
            continue
        # Check if password starts with "pass" or "Pass"
        if password.lower().startswith("pass"):
            print("Password must not begin with 'pass'.")
            continue
        # Check for uppercase letter
        if not has_upper(password):
            print("Password must contain at least one uppercase letter.")
            continue
        # Check for lowercase letter
        if not has_lower(password):
            print("Password must contain at least one lowercase letter.")
            continue
        # Check for digit
        if not has_digit(password):
            print("Password must contain at least one digit.")
            continue
        # Check for special characters
        if has_special(password):
            print("Password must NOT contain special characters.")
            continue
        # Check for initials
        if not avoids_initials(password, initials):
            print("Password must not contain your initials.")
            continue
        # Check for repeating characters
        if not no_repeating_chars(password):
            print("Password must not contain repeating characters.")
            continue

        print("Password is valid and OK to use.")
        break
if __name__ == "__main__":
    main()