# WebScraping-python Export to json,csv,xml

This runs on ubuntu platform
# Table of Contents
1. [Installation](#1)
2. [How to get xpath of a particular text block](#2)
3. [To Run](#3)
4. [Important How to not get banned](#4)

 <a name="1"></a>
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
<a name="2"></a>
## How to get xpath of a particular text block 
In **Chrome** or **FireFox**, right click on the text field on the website and click **Inspect** or **Inspect Elements** 

![image](https://github.com/gcgloven/WebScraping-python/blob/master/scrapy/quotes_spider/GetXpath.png)

<a name="3"></a>
## To Run 

1. Edit your .py file's **def parse(self, response):** method for the specific data you want to crawl 
   eg:
   
       data =response.xpath('//*[@class="yourclass"]').extract() 
       
       data =response.xpath('// [@id="sg"]/div[1]/div[3]/div/div/div[1]/div/div/div[1]/div/span/span/span[1]/span').extract() 
       
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
<a name="4"></a>
# Important How to not get banned 
When you are scraping a website's data, you are most likely to visit the domain too frequently and download data too rapidly. For some websites, you may get your ip banned due to the unsual traffic.

## Method 1: Add a delay 
In the folder, you will see settings.py, uncomment the ***DOWNLOAD_DELAY***  
Or you can manually add a sleep(3) to your scrapy code

## Method 2: Add USER_AGENT
By defining a user agent, you are tellig the browser that you are a human not a robot.
In the folder, you will see settings.py, uncomment  ***USER_AGENT*** You may define it based on the browser you are using.
Sample definition 
```python
USER_AGENT = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1" 
```

## Method 3: Use Proxy
Let's say you want to scrapy youtube comments for over 1000000 videos, you are using the same ip address and most likely you will be the legendary youtube user who visit 1000000 in a very short of times, you are suspicious.
You need to rotate you ip address frequently to prevent banning. For details of rotational ip address and proxy visit:  https://github.com/aivarsk/scrapy-proxies

## Method 4: Use paid servers to host your Scrapy file
For easy hosting of scheduled scraping, you may consider scrapyhub.com for they in-built IP rotation service and hosting.
