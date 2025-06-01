import random
import string

def generate_password(length=12):
    if length < 4:
        return "Password must be at least 4 characters long."

    # Character sets
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation

    # Ensure at least one of each
    all_chars = upper + lower + digits + symbols
    password = [
        random.choice(upper),
        random.choice(lower),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest of the password length
    password += random.choices(all_chars, k=length - 4)
    random.shuffle(password)
    
    return ''.join(password)

def main():
    try:
        length = int(input("Enter password length: "))
        pwd = generate_password(length)
        print(f"Generated Password: {pwd}")
    except ValueError:
        print("❌ Please enter a valid number.")

if __name__ == "__main__":
    main()
