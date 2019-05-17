# WebScraping-python Export to json,csv,xml

This runs on ubuntu platform

## Installation
Install Scrapy 
sudo pip install scrapy 
Install 
python-dev, zlib1g-dev, libxml2-dev and libxslt1-dev are required for lxml
libssl-dev and libffi-dev are required for cryptography
```console
$ sudo apt-get install python-dev python-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev
$ sudo pip3 install bs4 // BeautifulSoup
$ sudo pip3 install scrapy // Scrapy
```
## Scrapy Shell
```console
$ Scraphy shell

$ fetch("your url")

$ resonse # check the HTTP status 
```

Go to your desired url and click "inspection" on the particular text block
```console
$ response.xpath('//*[@class="yourclass"]')
$ response.xpath('//*[@class="yourclass"]').extract() // contain all the data under class=="yourclass"
```

To specific the data within the markdown tree:
```console
$ response.xpath('//*[@class="accordion-title"]/h2').extract()
```


How to create a scrapy directory 

```console
$ cd /Destination 
$ scrapy makeproject 
$ scrapy genspider filename url //without http
```
## To Run 

1. Edit your .py file's "def parse(self, response):" method for the specific data you want to crawl 
   eg. data =esponse.xpath('//*[@class="yourclass"]').extract() 
       this contains all the data you have.
       
2. Remove html markdown by using BeautifulSoup. 
Example: 
```python
import scrapy
import openpyxl
from bs4 import BeautifulSoup
from openpyxl import Workbook

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['www.sutd.edu.sg/Admissions/Undergraduate/FAQs']
    start_urls = ['http://www.sutd.edu.sg/Admissions/Undergraduate/FAQs/']

    def parse(self, response):
        wb = Workbook() #output excel file for retrieved data 
        ws = wb.active   
        #Get list data of extracted info
        qn = response.xpath('//*[@class="accordion-title"]/h2').extract()
        ans = response.xpath('//*[@class="accordion-content"]').extract()
        
        count = 1 
        for i in qn:
            print("Did quesiton run?")
            ws["A"+str(count)] = BeautifulSoup(i, "lxml").text #remove html markdown syntax
            count+=1
        count = 1
        for j in ans:
            ws["B"+str(count)] = BeautifulSoup(j, "lxml").text
            count+=1
        wb.save("trial3.xlsx")
```


3. Go Terminal, go to your scrapy config files's folder. 

```console
$ scrapy list // shows all the scrapy files in this project file 
$ scrapy crawl filename // runs the scrapying 
```

3 B. Use scrapy to Export json,csv,xml

Example: 
```python
import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['www.sutd.edu.sg/Admissions/Undergraduate/FAQs']
    start_urls = ['http://www.sutd.edu.sg/Admissions/Undergraduate/FAQs/']

    def parse(self, response):
        wb = Workbook() #output excel file for retrieved data 
        ws = wb.active   
        #Get list data of extracted info
        qn = response.xpath('//*[@class="accordion-title"]/h2/text()').extract() // instead of using bs4 text() works fine as well
        ans = response.xpath('//*[@class="accordion-content"]/text()').extract()
        yield {'Question':qn,'Answer': ans}

```
Then go to Terminal's scrapy project folder
```console 
$ scrapy crawl filename -o filename.csv // output csv file 
$ scrapy crawl filename -o filename.json // output json file 
$ scrapy crawl filename -o filename.xml // output xml file 
```
