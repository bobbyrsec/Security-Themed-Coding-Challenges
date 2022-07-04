'''
Web scrapers

Write a script to scrape information from a website.

'''

#Recursively look for hrefs and get product descriptions:  <p class="description">Acer Aspire ES1-572 Black, 15.6" HD, Core i3-6006U, 4GB, 500GB, Windows 10 Home</p>

#Test website https://webscraper.io/test-sites/e-commerce/

import requests
import re

visited = set()
product_descriptions = set()
def spider(url):
   site = str(requests.get(url,verify=False).text)
   get_description(site)
   #print (url, "URL")
   #print (site)
   links = re.findall(r'(?:href=\")(\/.*)(?:\" class?)(?:.*)',site)
   for link in links:
   	   link =  "https://webscraper.io" + link
   	   if link not in visited:
   	   	  visited.add(link)
   	   	  spider(link)


def get_description(text):
	descriptions = re.findall(r'(?:<p class="description">)(.*)(?:</p>)', text)
	#print (descriptions)
	for description in descriptions:
		product_descriptions.add(description)



spider("https://webscraper.io/test-sites/e-commerce/allinone")
print (visited, "visited sites")
print (product_descriptions, "product descriptions")
