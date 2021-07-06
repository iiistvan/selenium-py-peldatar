# 009 Feladat: selenium dátum mezők gyakorlása
import csv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime, timezone, time, date
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://localhost:9999/forms.html")

datedata = datetime(2021, 6, 5)
driver.find_element_by_id('example-input-date').send_keys(datedata.strftime('%Y\t%m%d'))

datedata = datetime(2012, 6, 5, 5, 5, 5, 555)
driver.find_element_by_id('example-input-date-time').send_keys(datedata.strftime('%Y.%m.%d %H:%M:%S:%f'))

datedata = datetime(2000, 5, 12, 12, 1)
driver.find_element_by_id('example-input-date-time-local').send_keys(datedata.strftime('%Y\t%mt%dt%H%M'))

datedata = datetime(1995, 12, 1)
driver.find_element_by_id('example-input-month').send_keys(datedata.strftime('%Y\t%B'))

datedata = datetime(2015, 12, 31)
driver.find_element_by_id('example-input-week').send_keys(datedata.strftime('%W%Y'))

driver.find_element_by_id('example-input-time').send_keys(12, 25)

time.sleep(10)

driver.close()
