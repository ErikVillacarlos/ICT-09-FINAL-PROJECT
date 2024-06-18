import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_generator():
    while True:
        try:
            length = int(input("Enter the length of the password: "))
            if length <= 0:
                print("Password length must be positive. Try again.")
                continue
            print("Generated Password:", generate_password(length))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue
 
        
        continue_generating = input("Do you want to generate another password? (yes/no): ").strip().lower()
        if continue_generating != "yes":
            break

password_generator()