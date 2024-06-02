import random
import string

def generate_password(length):
    if length < 12:
        raise ValueError("Password length should be at least 12 characters.")
    
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation
        
    all_characters = lower + upper + digits + special
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special),
    ]
        
    password += random.choices(all_characters, k=length-4)
        
    random.shuffle(password)
        
    return ''.join(password)

def get_valid_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def main():
    print("Welcome to the Password Generator!")
        
    length = get_valid_integer("Enter the password length (minimum 12 characters): ")
    while length < 12:
        print("Password length should be at least 12 characters.")
        length = get_valid_integer("Enter the password length (minimum 12 characters): ")
    
    count = get_valid_integer("Enter the number of passwords to generate: ")
        
    print("\nGenerated Passwords:")
    for _ in range(count):
        print(generate_password(length))

if __name__ == "__main__":
    main()
