from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher_suite = Fernet(key)

data = b"Test, Hello MARS!"

encrypted_data = cipher_suite.encrypt(data)

print(data)
print(f"Encrypted: ", encrypted_data)

decrypted_data = cipher_suite.decrypt(encrypted_data)
print(f"Decrypted: ", decrypted_data)