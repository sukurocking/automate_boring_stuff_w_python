import requests
# file_to_download = "https://filesamples.com/samples/document/txt/sample3.txt"
file_to_download = "https://automatetheboringstuff.com/files/rj.txt"
resp = requests.get(file_to_download)
resp.raise_for_status() #This does not print anything to the terminal, so we are good to proceed
resp.status_code == requests.codes.ok
print(resp.status_code) # This prints 200, which is the HTTP status code for 200
len(resp.text)

with open("RomeoJuliet2.txt", "wb") as file:
    for chunk in resp.iter_content(100000):
        file.write(chunk)
        
