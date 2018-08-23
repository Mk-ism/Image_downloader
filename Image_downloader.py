#!/usr/bin/env python

from bs4 import BeautifulSoup as soup
import requests
from urllib.parse import urljoin
from urllib.request import urlopen as uRqst

web_url = input("Enter url: ")



def make_soup(web_url):

	http_client_HTTPResponse = uRqst(web_url)
	web_html = http_client_HTTPResponse.read()
	http_client_HTTPResponse.close()
	beautiful_soup = soup(web_html, "html.parser")
	return beautiful_soup



def image_download():
	beautiful_soup = make_soup(web_url)
	image_tags = beautiful_soup.findAll("img")
	print(str(len(image_tags))+" images downloading \nPlease Wait..." )
	image_src = [each.get('src') for each in image_tags]

	for each in image_src:
		image_links = urljoin(web_url,each)
		filename = image_links.split('/')[-1]
		req = requests.get(image_links, allow_redirects=True)
		open(filename, 'wb').write(req.content)
	return None


if __name__ == '__main__':
	image_download()
	print("Download Completed.")

