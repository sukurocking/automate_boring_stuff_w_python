# Opening a webpage in browser
import webbrowser

from bs4 import ResultSet, Tag

webbrowser.open("https://inventwithpython.com")


# Downloading a webpage with requests.get() function
import requests
res = requests.get("https://automatetheboringstuff.com/files/rj.txt")
type(res)
res.status_code == requests.codes.ok
# requests.codes
print(requests.codes.ok)

len(res.text)
print(res.text[:250])

# The below will raise an exception if there was an error downloading the file and will do nothing if the download succeeded
res = requests.get("https://automatetheboringstuff.com/files/random_page_that_might_not_exist")
res.raise_for_status()


# In case we want to ensure that our program does not crash, we can use try/except block
res = requests.get("https://automatetheboringstuff.com/files/random_page_that_might_not_exist")
try:
    res.raise_for_status()
except Exception as exc:
    print("There was a problem: {}".format(exc))
    
    
########## Saving Donwloaded files to the hard drive ##########
res = requests.get("https://automatetheboringstuff.com/files/rj.txt")
with open("RomeoandJuliet.txt", "wb") as file:
    for chunk in res.iter_content(100000):
        file.write(chunk)


########## Parsing HTML with the BS4 module ##########




import requests, bs4
res = requests.get("https://nostarch.com")
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text, "html.parser")
type(noStarchSoup)



exampleFile = open("example.html")
exampleSoup = bs4.BeautifulSoup(exampleFile, "html.parser")
type(exampleSoup)
exampleFile.close()

# Output a list of *paragraghs*
exampleSoup.select('p')

# Outputs a list of span
exampleSoup.select("span")

# Outputs a list of elements with id as author
print(exampleSoup.select("#author")[0])
type(exampleSoup.select("#author")[0])
elem = exampleSoup.select("#author")
elem[0].getText()
elem[0].attrs



# Using another example
# The below is the string we copied when we clicked on https://weather.gov >> forecast >> inspect element >> copy >> selector (CSS selector)
#detailed-forecast-body > div:nth-child(1) > div.col-sm-10.forecast-text
# This can be used by bs4's select() or Selenium's find_element_by_css_selector() methods
import requests, bs4
weather_sample_resp = requests.get("https://forecast.weather.gov/MapClick.php?lat=37.78873500000003&lon=-122.3945")
type(weather_sample_resp)

len(weather_sample_resp.text)

# Saving the weather.gov response file into hard drive
with open("weather_sample_response_file.html", "wb") as html_file:
    for chunk in weather_sample_resp.iter_content(10000):
        html_file.write(chunk)


# Now we will parse the html file using beautiful soup
with open("weather_sample_response_file.html", "r") as weather_sample_html_file:
    weather_soup = bs4.BeautifulSoup(weather_sample_html_file.read(), "html.parser")

elems = weather_soup.select("#detailed-forecast-body > div:nth-child(1) > div.col-sm-10.forecast-text")
print(elems[0].attrs)
elems[0].getText()
type(elems[0].getText())
print(elems[0].getText() == elems[0].text)

