import random
import string
green_text = "\033[32m"
reset_color = "\033[0m"
yellow_text = "\033[33m"

# Function to generate a random password
def generate_password(length=10):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Function to generate a random email
def generate_email():
    domains = ["gmail.com", "yahoo.com", "outlook.com", "example.com", "testmail.com","hotmail.com"]
    username = ''.join(random.choice(string.ascii_lowercase) for i in range(8))
    domain = random.choice(domains)
    return f"{username}@{domain}"

# Get the number of email/password pairs to generate
n = int(input("Enter the number: "))

# Generate email and password pairs
for i in range(n):
    email = generate_email()
    password = generate_password()
    print(f"Email: {green_text}{email}{reset_color}")
    print(f"Password: {green_text}{password}{reset_color}")
    print()
print(f"{yellow_text}Email accounts :",n,f"{reset_color}")
