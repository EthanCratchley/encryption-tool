from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher_suite = Fernet(key)

with open("important.txt") as file:
    for line in file:
        data = line.encode('utf-8')
        encrypted_data = cipher_suite.encrypt(data)
        print(data)
        print("-----")
        print(encrypted_data)





