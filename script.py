import re

import requests

# ask user to input url and number of pages
url = input("Please input the document URL: ")
numPages = int(input("Please input the number of pages: "))
# extract document ID and subfolder ID from pasted url
subID = re.search(r"subfolder=(.+)&doc=", url).group(1)
docID = re.search(r"doc=(.+)&bitsid=", url).group(1)
# loop to download the entire document
for x in range(numPages):
    newUrl = f"http://dlib.ptit.edu.vn/flowpaper/services/view.php?doc={docID}&format=jpg&page={x + 1}&subfolder={subID}"
    print("Downloading page %d..." % (x + 1))
    r = requests.get(newUrl, stream=True)
    image = f"{x + 1}.jpg"
    downloaded_file = open(image, "wb")
    for chunk in r.iter_content(chunk_size=256):
        if chunk:
            downloaded_file.write(chunk)
print("Download complete, enjoy.")
