#######################################  
#  
# Project Name - GANaCH
# File Author(s): Cliff Landis <jlandis@auctr.edu>  
# License: GPLv3
# Description / Purpose: Scrape GHRAC database entries and write them to a text file
# Dependencies / Libraries / Modules: urllib, BeautifulSoup, csv, datetime
#  
#######################################  

# import libraries
import urllib.request as urllib
from bs4 import BeautifulSoup
import csv
from datetime import datetime

#create/open text file to write results to
f = open("ghrac_data.txt","w+")
#loop over each page in the range specified
for i in range(100, 102): 
    quote_page = 'https://www.georgiaarchives.org/ghrac/print_view/?rec={}'.format(i)

# query page and return html to variable 'page'
    page = urllib.urlopen(quote_page)

# parse page's html w/ BeautifulSoup and store in 'soup'
    soup = BeautifulSoup(page, 'html.parser')

#find the instance of the h2 styled this way (organization name), which has the content inside 
    name_box = soup.find('h2', attrs={'style': 'margin-bottom: 0em;'})
    num = str(i)
    if name_box != None:  #test if there is an organization title on the page, if not, skip to else
        name = name_box.text.strip()  # strip out the starting and trailing tags
        f.write("{'RECORD NUMBER': '" + num + "', ")  #write page number as "record number"
        f.write("'ORGANIZATION': '" + name + "', ")  #write h2 tag contents as "organization"
    else:
        # f.write("{'RECORD NUMBER': '" + num + "', ") # write page number as "record number"
        # f.write(str(i) + " is an Empty Record" + "\n") # record is empty, record as such
        continue  # if the record is empty, just continue on to table contents

# grab the table
    table_data = soup.find('table')
#for table_strip in table_data.children:
    #find = soup.find_all("strong", string=['CATEGORY', 'COUNTY', 'MAILING ADDRESS'])
    print(table_data.strong.stripped_strings)
    results = table_data.get_text(",", strip=True) + "}\n"
    f.write(results)
#    table_strip = table_data.text.strip()
#print(table_strip)
print("GHRAB Scrape Complete!")
f.close()
#open a csv file with append, so old data won't be erased
#with open('ghrab.csv', 'a') as csv_file:
#    writer = csv.writer(csv_file)
#    writer.writerow(name, table_data, datetime.now())