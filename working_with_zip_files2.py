import os, shutil, zipfile
os.getcwd()
os.chdir("./zip_files")
os.listdir()
shutil.rmtree("cab_expenses")
os.unlink("spam.txt")

# os.unlink("spam_zip_file.zip")

# Creating a file and writing contents into it
with open("spam2.txt", "w") as spam_file:
    spam_file.write("This is another spam file.\nThere is no useful info in here.")


# Creating a zip file and "writing" or adding files into the zip
spam_zip_file = zipfile.ZipFile("spam_zip_file.zip", "w")
spam_zip_file.write("./spam.txt", compress_type=zipfile.ZIP_DEFLATED)
spam_zip_file.write("./spam2.txt", compress_type=zipfile.ZIP_DEFLATED)
spam_zip_file.close()

# Reading zip file and its contents
my_spam_zip_file =  zipfile.ZipFile("spam_zip_file.zip", "r")
my_spam_zip_file.namelist()
my_spam_file = my_spam_zip_file.getinfo("spam2.txt")
my_spam_file.file_size
my_spam_file.compress_size

print("The zip file is compressed {}x".format(round(my_spam_file.file_size / my_spam_file.compress_size, 2)))

my_spam_zip_file.close()