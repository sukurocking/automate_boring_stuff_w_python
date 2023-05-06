#! python3
# searchpypi.py  - Opens several search results.

# This is what the program does:

# Gets search keywords from the command line arguments
# Retrieves the search results page
# Opens a browser tab for each result

"""
This means your code will need to do the following:

Read the command line arguments from sys.argv.
Fetch the search result page with the requests module.
Find the links to each search result.
Call the webbrowser.open() function to open the web browser.
"""


import sys, requests, bs4
import webbrowser

# 1:Read the command line arguments from sys.argv.
args_list = sys.argv[1:]


# 2:Fetch the search result page with the requests module.
google_search_url = "https://www.google.com/search?q="
pypi_search_url = "https://pypi.org/search/?q="


complete_pypi_search_url = pypi_search_url + " ".join(args_list)
# complete_pypi_search_url = pypi_search_url + "python"
# print(complete_pypi_search_url)
pypi_resp = requests.get(complete_pypi_search_url)
# print(type(pypi_resp))
# print(len(pypi_resp.text))
# print(pypi_resp.text[100:1000])


# 3:Find the links to each search result.
# Getting the CSS selector for each element
#content > div > div > div.left-layout__main > form > div:nth-child(3) > ul > li:nth-child(1) > a > h3
pypi_resp_soup = bs4.BeautifulSoup(pypi_resp.text, "html.parser")
# print(pypi_resp_soup)
pypi_resp_elements_list = pypi_resp_soup.select(".package-snippet")
# print(type(pypi_resp_elements_list))
print(pypi_resp_elements_list[1])
print(len(pypi_resp_elements_list))

# The link to the project(s) will be available in the href
print(pypi_resp_elements_list[0].get("href"))


# Call the webbrowser.open() function to open the web browser.
num_elements = min(5, len(pypi_resp_elements_list))
for i in range(num_elements):
    webbrowser.open("https://pypi.org" + str(pypi_resp_elements_list[i].get("href")))
