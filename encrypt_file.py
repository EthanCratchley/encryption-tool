from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher_suite = Fernet(key)

with open("important.txt", "r") as file:
    data = file.read()
    data = data.encode('utf-8')
    encrypt_data = cipher_suite.encrypt(data)
    
print(data)
print(encrypt_data)
