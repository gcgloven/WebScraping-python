# WebScraping-python

## This repo consists of a scrapy project which you can use to retrive specific data based on **xpath** of the html architecture.

For the basic scrapying method:
[WebScraping-python Export to excel,json,csv,xml](https://github.com/gcgloven/WebScraping-python/blob/master/WebScraping-python%20Export%20to%20json%2Ccsv%2Cxml.md)

 
# Helpful Data Cleaning methods 
```python 
del ls[0] #remove list item with index[0]
string.strip() # remove the leading and trailing spaces
string.lower() # convert all char to lower case 
string.upper() # convert all char to upper case
string.replace("\r\n\t\t\t"," ") #replace specific string \r\n\t\t\t to " "
string[2:] #start string at index 2
string[:-1] #read everything before last chara
```

# Convert HTML to plain txt with no tags

``` python 
from bs4 import BeautifulSoup as Soup
import re, nltk
from urllib.request import urlopen
 
url = 'http://pm1sf.com/faq'
html = urlopen(url).read() #make the request to the url
soup = Soup(html) #using Soup on the responde read
for script in soup(["script", "style"]): #You need to extract this <script> and <style> tags
    script.extract() #strip them off
text = soup.getText() 
text = text.encode('utf-8') #make sure to encode your text to be compatible
#raw = nltk.clean_html(document)
print(text)

```
