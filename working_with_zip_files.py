import zipfile, os
from pathlib import Path
p = Path.home()
p1 = p / "Downloads/automate_boring_stuff_w_python/zip_files"
# print(p1)

# Reading a zip file and reading its contents
exampleZip = zipfile.ZipFile(p1 / "Automate_the_Boring_Stuff_2e_onlinematerials.zip")
exampleZip.namelist()

req_file_info = exampleZip.getinfo("automate_online-materials/automate-win-requirements.txt")
req_file_info.file_size
req_file_info.compress_size

f"Compressed file is {round(req_file_info.file_size / req_file_info.compress_size, 2)}x smaller"
exampleZip.close()

exampleZip2 = zipfile.ZipFile(p1 / "iTerm2-3_4_19.zip")
exampleZip2.namelist()
exampleZip2.close()


exampleZip3 = zipfile.ZipFile(p1 / "cab_expenses.zip")
exampleZip3.namelist()
pdf_file_info = exampleZip3.getinfo("cab_expenses/airport_to_hotel_02Apr23_ola.pdf")
pdf_file_info.file_size
pdf_file_info.compress_size
f"Compressed file is {round(pdf_file_info.file_size / pdf_file_info.compress_size,2)}x smaller"
exampleZip3.close()

# Extracting all files of a zip file
exampleZip = zipfile.ZipFile(p1 / "cab_expenses.zip")
exampleZip.extractall()
exampleZip.close()

# Extracting a single file of a zip file
os.chdir(p1)
exampleZip = zipfile.ZipFile(p1 / "cab_expenses.zip")
exampleZip.extract("cab_expenses/airport_to_hotel_02Apr23_ola.pdf")
exampleZip.close()
