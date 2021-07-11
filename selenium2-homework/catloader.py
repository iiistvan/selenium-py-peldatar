# 023 Feladat: Load more feladatok
import csv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import difflib
import filecmp
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pprint
from pathlib import Path
import os
import errno

driver = webdriver.Chrome(ChromeDriverManager().install())

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise

def image_load(o):
    for i in range(int(o) - 1):
        load_more.click()
        time.sleep(4)


def image_data():
    images = driver.find_elements_by_xpath("//div[@class ='image']")
    time.sleep(5)
    i = 0

    for j in images:
        data_row = {}
        data_row['sorszam'] = i + 1
        catid = j.find_element_by_tag_name("p").text
        catid = catid.replace("Cat id: ", "")
        data_row['cat_id'] = catid
        with open(f"{catpath}\\{data_row['sorszam']}_{data_row['cat_id']}.jpg", "w") as filecat:
            filecat.write(j.find_element_by_tag_name("img").get_attribute("src"))
        catlist.append(data_row)
        i += 1
    # print(len(catlist))
    # pprint.pprint(catlist)
    # return catlist


try:
    driver.get("http://localhost:9999/loadmore.html")
    # gomb definició, betöltendő oldalszám beállítás
    load_more = driver.find_element_by_xpath("//div[@class='load-more-button']/button")
    time.sleep(4)
    oldal = 4

    # képállományok helyének beállítása, létrehozása
    catpath = 'c:\\cats'
    mkdir_p(catpath)

    # oldalak betöltése
    image_load(oldal)

    # képlista definíció, listát létrehozó fv. meghívása
    catlist = []
    image_data()


finally:
    driver.close()
