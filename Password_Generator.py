import string
import random

def generate_password(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters)for _ in range(length))
    return password

def generate_multiple_passwords(num_passwords,length):
    password = []
    for _ in range(num_passwords):
        password.append(generate_password(length))
    return password

def main():
    try:
        length = int(input("Enter the length of the password:"))
        if(length<8):
            print('Weak password!Please enter a strong number')
            return
        num_passwords = int(input("Enter how many passwords to be generated:"))
        
        password = generate_multiple_passwords(num_passwords,length)
        print("\n")
        
        print("Generated Passwords are :")
        for i, password in enumerate(password,1):
            print(f"Password {i}:{password}")
            
    except ValueError:
        print("Invalid input! Please enter a number.")
        
if __name__ == "__main__":
    main()