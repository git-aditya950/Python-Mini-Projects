import random
import string

print("🔐 Welcome to Aditya's Random Password Generator")

def generate_password(length=12, use_digits=True, use_special=True):
  
    characters = string.ascii_letters  

    if use_digits:
        characters += string.digits 
    if use_special:
        characters += string.punctuation  

    if length < 4:
        return "❌ Password length too short!"

    password = ''.join(random.sample(characters, length))
    return password

try:
    length = int(input("Enter password length (e.g., 8, 12, 16): "))
    digits = input("Include numbers? (y/n): ").lower() == 'y'
    special = input("Include special characters? (y/n): ").lower() == 'y'

    password = generate_password(length, digits, special)
    print(f"\n✅ Generated Password: {password}")

except ValueError:
    print(" Please enter a valid number for length.")
