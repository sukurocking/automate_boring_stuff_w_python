# This method works on all operating systems
from pathlib import Path
Path("spam", "bacon", "eggs") 
type(Path("spam", "bacon", "eggs") )
str(Path("spam", "bacon", "eggs"))


# Following code joins names from a list of filenames 
# to the end of a folder’s name
my_files = ["accounts.txt", "details.csv", "invite.docx"]
for filename in my_files:
    print(Path(r"/Users/sukumarsubudhi",filename))
    
# / operator that we normally use for division can also combine Path objects 
# and strings. This is helpful 
# for modifying a Path object after 
# they have been created using Path() function

Path("spam") / "bacon" / "eggs"
Path("spam") / Path("bacon/eggs")

Path("spam") / Path("bacon", "eggs")


home_folder = Path("/Users/sukumarsubudhi")
sub_folder = Path("spam")
home_folder / sub_folder
str(home_folder / sub_folder)

"spam" / Path("bacon") / "eggs"
# / operator replaces os.path.join() function

import os
Path.cwd()
os.chdir("/Users/sukumarsubudhi/Downloads/automate_boring_stuff_w_python/reading_writing_files")
os.getcwd()

Path.home()