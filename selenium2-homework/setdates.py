# 009 Feladat: selenium dátum mezők gyakorlása
import csv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime, timezone, time, date
import time
from selenium.webdriver.common.keys import Keys

# 1. verzió - Chrome options argument
options = webdriver.ChromeOptions()
options.add_argument('--lang=en')

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get("http://localhost:9999/forms.html")
time.sleep(2)

datedata = datetime(2021, 6, 5)
driver.find_element_by_id('example-input-date').send_keys(datedata.strftime('%m%d%Y'))
time.sleep(2)

datedata = datetime(2012, 5, 5, 5, 5, 5, 555000)
driver.find_element_by_id('example-input-date-time').send_keys(datedata.strftime('%Y.%m.%d %H:%M:%S:%f')[:-3])
time.sleep(2)

datedata = datetime(2000, 5, 12, 12, 1)
driver.find_element_by_id('example-input-date-time-local').send_keys(datedata.strftime('%mt%dt%Y\t%H%M%p'))
time.sleep(2)

datedata = datetime(1995, 12, 1)
driver.find_element_by_id('example-input-month').send_keys(datedata.strftime('%B\t%Y'))
time.sleep(2)

datedata = datetime(2015, 12, 31)
driver.find_element_by_id('example-input-week').send_keys(datedata.strftime('%W%Y'))
time.sleep(2)

datedata = datetime(2021, 7, 16, 0, 25)
driver.find_element_by_id('example-input-time').send_keys(datedata.strftime('%H%M%p'))

time.sleep(3)

driver.close()


# 2. verzió
# data_list = [[2021, 6, 5], [2012, 5, 5, 5, 5, 5, 555000], [2000, 5, 12, 12, 1], [1995, 12, 1], [2015, 12, 31], [2021, 1, 1, 0, 25]]
# data_form = [['%m%d%Y'], ['%Y.%m.%d %H:%M:%S:%f')[:-3]'],]
# field_list = ['example-input-date', 'example-input-date-time', 'example-input-date-time-local', 'example-input-month', 'example-input-week', 'example-input-time']
#
# def setdates(field_l, data_l):
#     for _ in range(len(field_l)):
#         datedata = data_l[_]
        driver.find_element_by_id(field_l[_]).send_keys(datedata.strftime())
