# Hibakezelés nem létező elemnél

from selenium import webdriver
import selenium.common.exceptions

driver = webdriver.Chrome()

driver.get("https://python.org")

try:
    elem = driver.find_element_by_id("nemletezik")  # if selenium.common.exceptions.NoSuchElementException:
    print("Létezik")
except selenium.common.exceptions.NoSuchElementException:
    print("Nem létezik")
    pass

driver.close()
