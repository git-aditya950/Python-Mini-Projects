import random
import string

def generate_password(length=12, use_digits=True, use_special=True):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    if length < 4:
        return "❌ Password too short!"
    return ''.join(random.sample(characters, length))

def main():
    print("🔐 Aditya's Password Generator (Refactored)")
    try:
        length = int(input("Enter password length: "))
        use_digits = input("Include numbers? (y/n): ").lower() == 'y'
        use_special = input("Include special characters? (y/n): ").lower() == 'y'
        password = generate_password(length, use_digits, use_special)
        print(f"✅ Your Password: {password}")
    except ValueError:
        print("❌ Please enter a valid number.")

if __name__ == "__main__":
    main()
