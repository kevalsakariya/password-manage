import random
import os

def password_generate(n):
    ans = ""
    other = ['!', '@', '#', '$', '%', '&']
    for i in range(n):
        count = random.randint(1, 4)
        if count == 1:
            ans += chr(random.randint(65, 90))  # Uppercase
        elif count == 2:
            ans += chr(random.randint(97, 122))  # Lowercase
        elif count == 3:
            ans += random.choice(other)  # Special characters
        else:
            ans += str(random.randint(0, 9))  # Numbers
    return ans

if __name__ == "__main__":
    n = int(input("Enter the length of the password: "))
    user = input("Enter your name: ")
    purpose = input("Enter the purpose for password generation: ")

    password = password_generate(n)
    file_name = "save.txt"
    
    file_exists = os.path.exists(file_name)

    with open(file_name, 'a' if file_exists else 'w') as file:
        file.write(f"User: {user}, Purpose: {purpose}, Password: {password}\n")

    print("Password saved successfully in save.txt")
