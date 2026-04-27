import os
import shutil

source_folder = "your_folder_path_here"

files = os.listdir(source_folder)

for file in files:
    if file.endswith(".jpg") or file.endswith(".png"):
        shutil.move(file, source_folder + "/Images/" + file)
    elif file.endswith(".pdf") or file.endswith(".docx"):
        shutil.move(file, source_folder + "/Documents/" + file)