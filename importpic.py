#how to import pic from the web into tree  
import os
os.mkdir('C:/vova')
from importlib.resources import path
import urllib.request

URL = 'https://img.haarets.co.il/img/1.4062586/1504506551.jpg'
FILENAME = r'c:\vova\image1.jpg'
with urllib.request.urlopen(URL) as response:
    image = response.read()
    with open(FILENAME, 'wb') as output_file:
        output_file.write(image)