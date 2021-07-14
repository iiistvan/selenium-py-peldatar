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
from os import getcwd
import errno
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("http://localhost:9999/dragndrop2.html")

time.sleep(2)

cwd = getcwd()
dnd = open(cwd + '\\dnd.js', 'r').read()

todo = driver.find_element_by_id("Todo")
# teendő elemek kigyűjtése
todo_li = todo.find_elements_by_xpath('li')
todo_list = []
for tdl in todo_li:
    todo_list.append(tdl.get_attribute("id"))
# teendők áthelyezése, js futtatás
for todo_item in todo_list:
    source = driver.find_element_by_id(todo_item)
    target = driver.find_element_by_id('Doing')
    driver.execute_script(dnd, source, target)
    time.sleep(1)


driver.implicitly_wait(5)