# -*- coding: utf-8 -*-

import scraperwiki
import urllib2
import urllib
import urlparse
from datetime import datetime
from bs4 import BeautifulSoup

# Set up variables
entity_id = "E2221_KCC_gov"
url = "http://www.kent.gov.uk/about-the-council/finance-and-budget/spending/invoices-over-250"

# Set up functions
def convert_mth_strings ( mth_string ):
	month_numbers = {'JAN': '01', 'FEB': '02', 'MAR':'03', 'APR':'04', 'MAY':'05', 'JUN':'06', 'JUL':'07', 'AUG':'08', 'SEP':'09','OCT':'10','NOV':'11','DEC':'12' }
	#loop through the months in our dictionary
	for k, v in month_numbers.items():
		#then replace the word with the number
		mth_string = mth_string.replace(k, v)
	return mth_string

# pull down the content from the webpage
html = urllib2.urlopen(url)
soup = BeautifulSoup(html)

# find all entries with the required class
block = soup.find('div',{'class':'large-12 column content-text'})
headers = block.findAll('h3')

for header in headers:
	title = header.text
	ns = find_next_sibling('p')
	print ns
	'''
	url = block.header.next_element.next_element.get("href")
	print title
	print url
	
	url = link['href']
	if '.csv' in url:
		print url
		#parsed_link = urlparse.urlsplit(url.encode('utf8'))
		parsed_link = parsed_link._replace(path=urllib.quote(parsed_link.path))
		encoded_link = parsed_link.geturl()
		title = encoded_link.split('/')[-1].replace('.csv','')
		# create the right strings for the new filename
		csvYr = title.split('-')[2]
		csvMth = title.split('-')[1][:3]
		csvMth = csvMth.upper()
		csvMth = convert_mth_strings(csvMth);
		filename = entity_id + "_" + csvYr + "_" + csvMth + ".csv"
		todays_date = str(datetime.now())
		scraperwiki.sqlite.save(unique_keys=['l'], data={"l": url, "f": filename, "d": todays_date })
		print filename
	'''
