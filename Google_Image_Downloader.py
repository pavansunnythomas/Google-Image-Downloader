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
browser.execute_script("document.body.style.zoom='150%'")

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

now = 0
counter =0
while(len(sub)< (limit*3)):
  browser.execute_script("scrollBy("+ str(value) +",+1000);")
  value += 1000
  time.sleep(0.1)
  print(f"about {len(sub)} images captured")
  if now == len(sub):
    counter+=1
  else:
    counter = 0
  if counter>20:
    print("available pictures to download :",len(sub))
    break
  now = len(sub)
  sub = elem1.find_elements_by_tag_name('img')

try:
  os.mkdir(queryForSearch)
except Exception as p:
  print(p,"\nOverwriting")

count = 0
for i in sub:
  src = i.get_attribute('src')
  count+=1
  if count>limit:
    break
  if src != None:
    src  = str(src)
    print("downloaded Image no : ",count)
    try:
      urllib.request.urlretrieve(src, os.path.join(f'{queryForSearch}','image'+str(count)+'.jpg'))
    except Exception:
      count-=1
      print(f'could not print Image {count}\n tring alternative pic ')
  else:
    count-=1
    print(f'could not print Image {count}\n tring alternative pic ')

print("Total pictures downloaded : ",(count-1))
browser.close()
