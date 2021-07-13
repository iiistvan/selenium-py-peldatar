# 030 Feladat: játék az ablakokkal
import csv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import difflib
import filecmp
import time
import random
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
driver.get("http://localhost:9999/windowgame.html")

main_window = driver.window_handles[0]
colorQuiz = driver.find_element_by_id("target_color").text
my_list = list(range(1, 101))
random.shuffle(my_list)

for number in my_list:
    driver.find_element_by_id(number).click()
    time.sleep(0.5)
    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)
    colorText = driver.find_element_by_tag_name("h1").text
    print(f"Keresett szín: {colorQuiz}\nTippelt szám szine: {colorText}")
    if colorText == colorQuiz:
        print('Eltaláltam!')
        time.sleep(1)
        driver.close()
        break
    else:
        driver.close()
        driver.switch_to.window(main_window)

driver.switch_to.window(main_window)
time.sleep(3)
driver.close()
