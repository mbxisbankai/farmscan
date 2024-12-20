import os
import shutil
import hashlib
import time


def display_tips():
    tips = [
        "1. Always keep your software and antivirus up to date.",
        "2. Avoid clicking on unknown links or downloading files from untrusted sources.",
        "3. Regularly back up your important files to an external drive or cloud storage.",
        "4. Use strong passwords and enable two-factor authentication where possible.",
        "5. Disconnect from the internet immediately if you suspect a ransomware attack."
    ]
    print("\nCybersecurity Tips:")
    for tip in tips:
        print(tip)


def backup_files(source_folder, backup_folder):
    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)

    for filename in os.listdir(source_folder):
        source_file = os.path.join(source_folder, filename)
        backup_file = os.path.join(backup_folder, filename)

        if os.path.isfile(source_file):
            shutil.copy2(source_file, backup_file)
            print(f"Backed up: {filename}")


def hash_file(filepath):
    hasher = hashlib.sha256()
    try:
        with open(filepath, 'rb') as f:
            buf = f.read()
            hasher.update(buf)
        return hasher.hexdigest()
    except FileNotFoundError:
        return None


def scan_files(folder):
    print("\nScanning files for potential threats...")
    suspicious_files = []
    for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename)
        if os.path.isfile(filepath):
            file_hash = hash_file(filepath)
            if file_hash and file_hash.startswith("00000"):  # Example condition for suspicious files
                suspicious_files.append(filename)

    if suspicious_files:
        print("Suspicious files detected:")
        for file in suspicious_files:
            print(f"- {file}")
    else:
        print("No suspicious files found.")


def ransomware_response():
    print("\nRansomware Response Guide:")
    steps = [
        "1. Disconnect from the internet immediately to prevent further spread.",
        "2. Do not pay the ransom; there is no guarantee of file recovery.",
        "3. Restore files from your backups.",
        "4. Contact local cybersecurity experts or authorities for assistance.",
        "5. Report the incident to law enforcement."
    ]
    for step in steps:
        print(step)


def main():
    print("Welcome to the Farmer Cybersecurity Tool")
    while True:
        print("\nChoose an option:")
        print("1. Display cybersecurity tips")
        print("2. Back up important files")
        print("3. Scan files for ransomware")
        print("4. Ransomware response guide")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_tips()
        elif choice == "2":
            source = input("Enter the folder path to back up: ")
            backup = input("Enter the backup folder path: ")
            backup_files(source, backup)
        elif choice == "3":
            folder = input("Enter the folder path to scan: ")
            scan_files(folder)
        elif choice == "4":
            ransomware_response()
        elif choice == "5":
            print("Exiting. Stay safe!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
