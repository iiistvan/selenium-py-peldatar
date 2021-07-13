# 026 Feladat: scroll to load more
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
import requests


def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


def image_data():
    for i in range(1, 21):
        element = driver.find_element_by_xpath(f"/html/body/div[1]/div[{i}][@class ='image']")
        data_row = {}
        data_row['sorszam'] = i
        catId = element.find_element_by_tag_name("p").text
        catId = catId.replace("Cat id: ", "")
        data_row['cat_id'] = catId
        catUrl = element.find_element_by_tag_name("img").get_attribute("src")
        catReq = requests.get(catUrl)
        if catReq.status_code == 200:
            with open(f"{catpath}\\{data_row['sorszam']}_{data_row['cat_id']}.jpg", "wb") as filecat:
                filecat.write(catReq.content)
        catlist.append(data_row)


# az oldal hívása, időzítés, lapozás, 20. elem
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://localhost:9999/scrolltoload.html")
time.sleep(10)
js = "window.scrollTo(0, 3000)";
driver.execute_script(js)
time.sleep(10)
element = driver.find_element_by_xpath("/html/body/div[1]/div[20][@class ='image']")
actions = ActionChains(driver)
actions.move_to_element(element).perform()

# képállományok helyének beállítása, létrehozása
catpath = 'c:\\cats'
mkdir_p(catpath)

# képlista definíció, listát létrehozó fv. meghívása
catlist = []
image_data()

driver.close()
