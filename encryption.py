import os
import sys
import pwd
from cryptography.fernet import Fernet

def encrypt_file():
    file_path = sys.argv[1]
    current_user = pwd.getpwuid(os.getuid()).pw_uid
    current_group = pwd.getpwuid(os.getuid()).pw_gid

    key = Fernet.generate_key()

    with open(file_path, 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)

    os.remove(file_path)

    with open(file_path, 'wb') as f:
        f.write(encrypted_data)
        f.write(b'\n')
        f.write(key)
            
    os.chown(file_path, current_user, current_group)
    
def main():
    encrypt_file()
    
if __name__=="__main__":
    main()
