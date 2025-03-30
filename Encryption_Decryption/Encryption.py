# import required module
from cryptography.fernet import Fernet

key = Fernet.generate_key()
with open('filekey.key', 'wb') as filekey:
   filekey.write(key)

print("Key Generated Successfully. Key is saved in filekey.key")
print("Key is:", key)

# opening the key
with open('filekey.key', 'rb') as filekey:
    key = filekey.read()
fernet = Fernet(key)

# opening the original file to encrypt
with open("DataWellLog.txt", "rb") as file:
    original = file.read()

encrypted = fernet.encrypt(original)
with open("DataWellLog_encrypted.txt", "wb") as file:
    file.write(encrypted)
    print("File Encrypted Successfully")