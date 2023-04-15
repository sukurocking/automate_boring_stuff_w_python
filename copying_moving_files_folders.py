with open("spam.txt", "w") as spam_file:
    spam_file.write("This is a spam file.\nThis does not contain any useful text")


import shutil, os
mypath = "/Users/sukumarsubudhi/Downloads/automate_boring_stuff_w_python"
src_path = os.path.join(mypath, "copying_moving_files_folders", "spam.txt")
dest_path = os.path.join(mypath, "reading_writing_files", "spam.txt")
print(src_path)
print(dest_path)
shutil.copy(src_path, dest_path)

# removing a file
os.unlink(src_path)

# Moving file from one folder to another 
shutil.move(src=dest_path, dst=os.path.join(mypath, "copying_moving_files_folders", "spamspamspam.txt"))
# Renaming file
shutil.move(src=os.path.join(mypath, "copying_moving_files_folders", "spamspamspam.txt"), dst=os.path.join(mypath, "copying_moving_files_folders", "spam.txt"))
os.getcwd()
os.chdir(os.path.join(mypath,"copying_moving_files_folders"))
os.getcwd()
os.listdir()

# copying entire folders - can be done using copytree
shutil.copytree(src= os.path.join(mypath, "copying_moving_files_folders"),dst=os.path.join(mypath, "copying_moving_files_folders_2"))
for list_item in os.listdir(mypath):
    print(list_item)
    
os.listdir(os.path.join(mypath, "copying_moving_files_folders_2"))


# removing entire folder
shutil.rmtree(os.path.join(mypath, "copying_moving_files_folders_2"))
os.getcwd()
os.listdir(mypath)

