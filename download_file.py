# Note that pip is required to install the requests library 
import requests


def download(url):
    get_response = requests.get(url)  # Sending a get request for the specified url which returns a response
    file_name = url.split("/")[-1]  # Splitting our URL by / and accessing the last element
    # Opening up a file to save our download to as a binary file ("wb")
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)


# Note that the download url must contain a file type extension to properly download
download("https://cdn.bringatrailer.com/wp-content/uploads/2017/08/DSC_0246-1280x851-940x625.jpg")
