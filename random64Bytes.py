import secrets
import string

bytes = [8, 32, 64, 128, 256]

for byte in bytes:
    # Convert the length to the number of hexadecimal characters
    hex_length = byte * 2
    
    # Generate random data
    random_data = secrets.token_hex(hex_length // 2)
    
    print(f"{byte} bytes: {random_data}")

# Define the characters to use in the password
characters = string.ascii_letters + string.digits + string.punctuation

# Set the desired length of the password
password_length = 16  # You can adjust this to your desired length

# Generate the random password
random_password = ''.join(secrets.choice(characters) for _ in range(password_length))

print("Random Password:", random_password)
