import os
from datetime import datetime

current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
user_input = input("Search (s)/Write (w)/List (l): ")

if user_input == "s" or user_input == "S":
    search = True
elif user_input == "w" or user_input == "W":
    search = False
elif user_input == "l" or user_input == "L":
    search = None
else:
    print("Not valid input")

if search == False:
    input2 = input("Name of file: ")
    folder_path = r"C:\Users\23liot\Desktop\Note Saver\Notes"
    file_name = input2 + ".txt"
    file_path = os.path.join(folder_path, file_name)

    with open(file_path, "w") as file:
        print(f"File {file_name} created in {folder_path}")
        file.write(f"Created: {formatted_datetime}\n")

if search == True:
    input1 = input("Search for: ")
    folder_path = r"C:\Users\23liot\Desktop\Note Saver\Notes"
    
    files = os.listdir(folder_path)
    files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]
    matching_files = [f for f in files if input1.lower() in f.lower()]

    if matching_files:
        print("Matching files found in folder:")
        for file in matching_files:
            print(file)
    else:
        print("No files found matching your search.")

if search == None:
    print("Files: ")
    folder_path = r"C:\Users\23liot\Desktop\Note Saver\Notes"

    files = os.listdir(folder_path)
    files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]

    for file in files:
        print(file)

file_choice = input("Choose a file: ") 

folder_path = r"C:\Users\23liot\Desktop\Note Saver\Notes"
files = os.listdir(folder_path)
files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]

if file_choice in files:
    print(f"You selected: {file_choice}")

    file_path = os.path.join(folder_path, file_choice)

    print("\nChoose an option:")
    print("1. Delete")
    print("2. Open")
    print("3. Edit")

    option = input("Enter the number of the action: ")

    if option == "1":
        check = input("Are you sure? (y/n): ")
        if check == "y" or check == "Y":
            os.remove(file_path)
            print(f"File '{file_choice}' has been deleted.")
        elif check == "n" or check == "N":
            print("Deletion is cancelled")
            
    elif option == "2":
        with open(file_path, "r") as file:
            content = file.read()
            print(f"\nContent of {file_choice}:")
            print(content)

    elif option == "3":
        os.startfile(file_path)  # This opens the file in the default text editor
        print(f"Opened '{file_choice}' in your text editor. Make your edits and save.")

    else:
        print("Invalid option selected.")
else:
    print(f"File '{file_choice}' not found in the folder.")