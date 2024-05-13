from cryptography.fernet import Fernet
import sys
import os
import subprocess
import atexit

def cleanup():
    # Perform any cleanup operations here
    file_to_remove = "decrypted_file.txt"
    if os.path.exists(file_to_remove):
        os.remove(file_to_remove)

def open_file_in_gedit(file_path):
    subprocess.Popen(['gedit', file_path])
    subprocess.Popen.wait()

def decryption():
    file_path = sys.argv[1]
    with open(file_path, 'rb') as f:
        data = f.read()

    data_parts = data.split(b'\n')

    key = data_parts[1]
    encrypted_data = data_parts[0]

    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)
    
    with open("decrypted_file.txt", 'wb') as f:
        f.write(decrypted_data)
    open_file_in_gedit("decrypted_file.txt")
#    atexit.register(cleanup) 
        
def main():
    decryption()
    
    
if __name__=="__main__":
    main()
