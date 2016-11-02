#### READ HTML 1.0

html = urllib2.urlopen(url)
soup = BeautifulSoup(html, 'lxml')


#### SCRAPE DATA

import urllib
import urlparse
block = soup.find('div',{'class':'large-12 column content-text'})
fileLinks = block.findAll('a', href=True)
for fileLink in fileLinks:
    url = fileLink['href']
    t = fileLink.text
    if '.csv' in url and 'nvoice' in t:
        parsed_link = urlparse.urlsplit(url.encode('utf8'))
        parsed_link = parsed_link._replace(path=urllib.quote(parsed_link.path))
        encoded_link = parsed_link.geturl()
        csvYr = url.replace('.-FINAL', '').split('.csv')[0][-4:]
        if '-16' in csvYr:
            csvYr = '2016'
        if '-250' in csvYr:
            csvYr = '2015'
        csvMth = t.split(' in ')[-1][:3]
        csvMth = convert_mth_strings(csvMth.upper())
        data.append([csvYr, csvMth, url])


#### STORE DATA 1.0

for row in data:
    csvYr, csvMth, url = row
    filename = entity_id + "_" + csvYr + "_" + csvMth
    todays_date = str(datetime.now())
    file_url = url.strip()

    valid = validate(filename, file_url)

    if valid == True:
        scraperwiki.sqlite.save(unique_keys=['l'], data={"l": file_url, "f": filename, "d": todays_date })
        print filename
    else:
        errors += 1

if errors > 0:
    raise Exception("%d errors occurred during scrape." % errors)


#### EOF
