#######################################  
#  
# Project Name - GANaCH
# File Author(s): Cliff Landis <jlandis@auctr.edu>  
# License: GPLv3
# Description / Purpose: Scrape GHRAC database entries and write them to a text file, seperated by a pipe, for processing in Excel into a CSV
# Dependencies / Libraries / Modules: urllib, BeautifulSoup
#  
#######################################  

# import libraries
import urllib.request as urllib
from bs4 import BeautifulSoup

#create/open text file to write results to
f = open("ghrac_data.txt","w+")

#loop over each page in the range specified
for i in range(0, 1000): 
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
        f.write("RECORD NUMBER|"+ num + "|")  #write page number as "record number"
        f.write("ORGANIZATION|" + name + "|")  #write h2 tag contents as "organization"
    else:
        continue  # if the record is empty, just continue on to table contents

# grab the table
    table_data = soup.find('table')
    results = table_data.get_text("|", strip=True) + "\n" # grab each cell seperated with a pipe
    f.write(results) # write the results to the file
    print(name_box.text) # print the organization name to the console to watch the script process through

print("GHRAB Scrape Complete!")
f.close()
