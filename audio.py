import requests
import zipfile
import io

class audio:
    """
    Class for downloading audio files/data.
    """

    def __init__(self):
        pass

    def downloadData(self):
        url = "https://github.com/karoldvl/ESC-50/archive/master.zip"
        response = requests.get(url)
        z = zipfile.ZipFile(io.BytesIO(response.content))
        z.extractall("ESC-50-data")
