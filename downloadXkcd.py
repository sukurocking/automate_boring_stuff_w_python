#! python3
# downloadXkcd.py - Downloads every single XKCD comic.


# Here’s what your program does:

#     Loads the XKCD home page
#     Saves the comic image on that page
#     Follows the Previous Comic link
#     Repeats until it reaches the first comic
    
# This means your code will need to do the following 
# 1. Download pages with the requests module
# 2. find the url of the comic image for a page using Beautiful Soup
# 3. Download and save the comit image to the hard drive with iter_content()
# 4. Find the URL of the previous comic link, and repeat

import requests, os, bs4
url = "https://xkcd.com"                # starting url
os.makedirs("xkcd", exist_ok = True)    # store comics in ./xkcd
while not url.endswith("#"):
    # Download the page
    print("Downloading page {}...".format(url))
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    
    # Find the URL of the comic page
    comicElem = soup.select("#comic img")
    if comicElem == []:
        print("Could not find comic image.")
    else:
        comicUrl = "https:" + str(comicElem[0].get("src"))
        # Download the image
        print("Downloading image {}...".format(comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()
    
    # Save the image to ./xkcd
        imageFile = open(os.path.join("xkcd", os.path.basename(comicUrl)), "wb")
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
    
    # Get the prev button's url
    prevLink = soup.select("a[rel='prev']")[0]
    url = "https://xkcd.com" + str(prevLink.get("href"))
    
print("Done.")