# WebScraping-python

This runs on ubuntu platform

## Installation
Install Scrapy 
sudo pip install scrapy 
Install 
python-dev, zlib1g-dev, libxml2-dev and libxslt1-dev are required for lxml
libssl-dev and libffi-dev are required for cryptography

sudo apt-get install python-dev python-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev
## Scrapy Shell
```python
$ Scraphy shell

$ fetch("your url")

$ resonse # check the HTTP status 
```

Go to your desired url and click "inspection" on the particular text block
```python
$ response.xpath('//*[@class="yourclass"]')
$ response.xpath('//*[@class="yourclass"]').extract() // contain all the data under class=="yourclass"
```

To specific the data within the markdown tree:
```python
$ response.xpath('//*[@class="accordion-title"]/h2').extract()
```
