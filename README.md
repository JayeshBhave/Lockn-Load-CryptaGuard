# Lockn’Load CryptaGuard – Secure File Encryption and Decryption

This repository contains a set of scripts for file encryption and decryption.

## Scripts Overview

1. **check.sh**: This script checks if the user executing it is the owner of the file it's operating on.
2. **decrypt.sh**: Accepts a file as an argument and passes it to `decrypt.py` for decryption.
3. **decrypt.py**: Decrypts the file it receives as an argument from the `decrypt.sh` script.
4. **encrypt.sh**: Accepts a file as an argument and passes it to `encrypt.py` for encryption.
5. **encrypt.py**: Encrypts the file it receives as an argument from the `encrypt.sh` script.
6. **monitor.sh**: Monitors a specified folder for new file creations. When a new file is detected, it automatically runs `encrypt.sh` on that file and assigns ownership to the user who created the file.

## Usage

1. **File Encryption**:
   - To encrypt a file, run `encrypt.sh` with the file path as an argument: `./encrypt.sh <file_path>`
   
2. **File Decryption**:
   - To decrypt a file, run `decrypt.sh` with the file path as an argument: `./decrypt.sh <file_path>`

3. **Monitoring Folder**:
   - To monitor a folder for new file creations, run `monitor.sh` in the background: `./monitor.sh &`

## Requirements

- Python 3.x
- Bash shell

## Note

- Ensure that the necessary permissions are set for executing the scripts.

## Contributors

- [Jayesh Bhave](https://github.com/JayeshBhave)

Feel free to contribute by forking the repository and sending pull requests.

