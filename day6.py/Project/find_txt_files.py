import os

def find_txt_files(folder_path):
    # If the folder does not exist, show an error message
    if not os.path.exists(folder_path):
        print("Folder does not exist:", folder_path)
        return

    # Get all items (files + folders) inside the folder
    for item in os.listdir(folder_path):

        # Create the full path of the item
        full_path = os.path.join(folder_path, item)

        # If it is a file and ends with .txt
        if os.path.isfile(full_path) and item.endswith(".txt"):
            print(full_path)

        # If it is a directory, call the function recursively
        elif os.path.isdir(full_path):
            find_txt_files(full_path)


# -------- PROGRAM START --------

# Path of the main folder to scan
main_folder_path = "day6.py"

# Call the function
find_txt_files(main_folder_path)
