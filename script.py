import re

import requests

# ask user to input url and number of pages
url = input("Please input the document URL: ")
# extract document ID and subfolder ID from pasted url
subID = re.search(r"subfolder=(.+)&doc=", url).group(1)
docID = re.search(r"doc=(.+)&bitsid=", url).group(1)
# loop to download the entire document
count = 1
while True:
    newUrl = f"http://dlib.ptit.edu.vn/flowpaper/services/view.php?doc={docID}&format=jpg&page={count}&subfolder={subID}"
    request = requests.get(newUrl, stream=True)
    if request.headers["Content-Type"] == "image/png":
        print(f"Downloading page {count}...")
        image = f"{count}.png"
        downloaded_file = open(image, "wb")
        for chunk in request.iter_content(chunk_size=256):
            if chunk:
                downloaded_file.write(chunk)
    else:
        break
    count += 1
print("Download complete, enjoy.")
