import os

def find_txt_files(folder_path):
    # folder ke andar ke sab items (files + folders) lo
    for item in os.listdir(folder_path):
        
        # item ka full path banao
        full_path = os.path.join(folder_path, item)

        # agar item file hai
        if os.path.isfile(full_path):
            # aur agar .txt file hai
            if item.endswith(".txt"):
                print(full_path)

        # agar item folder (directory) hai
        elif os.path.isdir(full_path):
            # recursion: us folder ke andar bhi check karo
            find_txt_files(full_path)


# --------- PROGRAM STARTS HERE ---------

# Main folder ka path
main_folder_path = "/Users/padhai/Wipro Training/day6/Project/MainFolder"

# function call
find_txt_files(main_folder_path)
