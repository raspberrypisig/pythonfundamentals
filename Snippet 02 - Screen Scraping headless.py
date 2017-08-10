#!/usr/bin/env python

# Do the following on the command line (uncomment)
# wget -c https://github.com/fg2it/phantomjs-on-raspberry/releases/download/v2.1.1-wheezy-jessie-armv6/phantomjs_2.1.1_armhf.deb
# sudo dpkg -i phantomjs_2.1.1_armhf.deb
# rm -f dpkg -i phantomjs_2.1.1_armhf.deb
# sudo pip install selenium

from selenium import webdriver
import json

driver = webdriver.PhantomJS()
driver.set_window_size(1124, 850)
driver.get('https://raw.githubusercontent.com/pklaus/python-spelling-alphabet/master/alphabets/NATO.json
')
print("----- START SOURCE---")
print(driver.page_source)
print("------END SOURCE----")
justjson = driver.find_element_by_tag_name('body').text
jsondata = json.loads(justjson)
print("\n\n--- NATO Phonetic for letter B----")
print(jsondata['letters']['B'])
driver.close()
