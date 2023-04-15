import os
for folder, subfolder, filename in os.walk("/Users/sukumarsubudhi/Library/CloudStorage/GoogleDrive-suku.subudhi@gmail.com/My Drive"):
    print("Folder Name :", folder)
    print("Subfolder(s):", subfolder)
    print("File(s):", filename)
    
    
for folder, subfolder, filename in os.walk("/Users/sukumarsubudhi/Library/CloudStorage/GoogleDrive-suku.subudhi@gmail.com/My Drive"):
    for indv_file in filename:
        if "Sushree" in indv_file:
            print("Folder: ", folder)
            print("File: ", filename)
            print("Invidual File: ", indv_file)
            print("Complete Path: ", os.path.join(folder, indv_file))
            complete_path = os.path.join(folder, indv_file)

print(complete_path)


import platform, shlex, subprocess
if platform.system() == "Darwin":       # macOS
    os.system("open " + shlex.quote(complete_path))
    # subprocess.call(("open", shlex.quote(complete_path))) # This is not working, since this is taking reference path
    "open " + shlex.quote(complete_path)
elif platform.system() == 'Windows':    # Windows 
    os.startfile(complete_path)
else:                                   # linux variants
    subprocess.call(('xdg-open', complete_path))
