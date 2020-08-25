from selenium import webdriver
import time
import urllib.request
import os
from selenium.webdriver.common.keys import Keys

queryForSearch = input("search query : ")
limit = int(input("Enter the required no of pics : "))

browser = webdriver.Firefox() 

# It opens the URL in the browser.
browser.get('https://www.google.com/')

#to get into the images page to download images and
#get_attribute fetches the URL of the Images and
#then clicks on the URL
elem = browser.find_element_by_link_text('Images')
elem.get_attribute('href')
elem.click()

# To get the search bar field from the Google home page.
search = browser.find_element_by_name('q')

# sending query and enter
search.send_keys(queryForSearch,Keys.ENTER)

value = 0
for i in range(10):
  browser.execute_script("scrollBy("+ str(value) +",+1000);")
  value += 1000
  time.sleep(0.1)

elem1 = browser.find_element_by_id("islmp")
sub = elem1.find_elements_by_tag_name('img')


while(len(sub)< limit):
  browser.execute_script("scrollBy("+ str(value) +",+1000);")
  value += 1000
  time.sleep(0.1)
  sub = elem1.find_elements_by_tag_name('img')

try:
  os.mkdir(queryForSearch)
except Exception as p:
  print(p)
count = 0
while(count<=limit):
  src = i.get_attribute('src')
  if src != None:
    src  = str(src)
    count+=1
    print("Image Source : ",src)
    print("Image no : ",count)
    try:
      urllib.request.urlretrieve(src, os.path.join(f'{queryForSearch}','image'+str(count)+'.jpg'))
    except Exception:
      print(f'could not print Image {count}\n tring alternative pic ')
      count-=1

browser.close()
