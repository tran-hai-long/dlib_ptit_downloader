# dlib-ptit-downloader

A simple script to download documents from PTIT online library (dlib.ptit.edu.vn).

> **Note**  
> This script will not download the PDF version of a document, but instead a collection of single-page images. For
> example, if the document is 90 pages long, it will download 90 images, each representing a page of the document.

## Usage

1. Install Python 3.10 or higher.
2. Download `script.py` and `requirements.txt`.
3. Open CMD/Terminal and run ```pip install -r requirements.txt``` to install necessary packages for the script.
4. On your web browser, log in to [PTIT online library](http://dlib.ptit.edu.vn) with your own account and open the document you want to
   download.
5. Run either ```python3 script.py``` or ```python script.py``` depending on your OS. The script will ask for the document URL.
6. Open your web browser, copy the document URL, paste it to the script, then type in the number of pages.
7. Sit back and relax while the script do its magic.

## Legal

This project does **NOT** attempt to violate Vietnam copyright law. If you have
a [PTIT online library](http://dlib.ptit.edu.vn) account, you can already access and download any document via the use of a web browser's developer tool. All this script does is automating the process to save time.

## License

[MIT](LICENSE)


