# 015 Feladat: felugró ablakok és tabok kezelése
import csv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import difflib
import filecmp
import time
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://localhost:9999/alert_playground.html")

# gombok kikeresése
alertBtn = driver.find_element_by_name('alert')
confirmationBtn = driver.find_element_by_name('confirmation')
promptBtn = driver.find_element_by_name('prompt')
doubleClickBtn = driver.find_element_by_id('double-click')

# referencia üzenetek definiálása
ref_text_alert = "I am alert"
ref_text_confirm = "I am confirm"
ref_text_prompt = "I am prompt"
ref_text_prompt_send = "I am Steve Miller"
ref_text_prompt_get = "You entered: I am Steve Miller"
ref_text_double = "You double clicked me!!!, You got to be kidding me"

# alert gomb működésének vizsgálata
alertBtn.click()
alert = driver.switch_to.alert
assert (alert.text == ref_text_alert)
print(alert.text)
time.sleep(1)
alert.accept()
time.sleep(1)

# confirmation box gomb működésének vizsgálata
# ciklus az OK és a Mégse gombra
for i in range(2):
    confirmationBtn.click()
    alert = driver.switch_to.alert
    assert (alert.text == ref_text_confirm)
    print(alert.text)
    time.sleep(1)
    if i == 0:
        alert.accept()
    else:
        alert.dismiss()
    time.sleep(1)

# prompt gomb működésének vizsgálata
promptBtn.click()
alert = driver.switch_to.alert
assert (alert.text == ref_text_prompt)
print(alert.text)
alert.send_keys(ref_text_prompt_send)
time.sleep(1)
alert.accept()
time.sleep(1)
# assert driver.find_element_by_id('demo').text == f"(You entered: {ref_text_prompt_send}"
assert driver.find_element_by_id('demo').text == ref_text_prompt_get
print(driver.find_element_by_id('demo').text)

# double click me gomb működésének vizsgálata
action = ActionChains(driver)
action.double_click(doubleClickBtn).perform()
alert = driver.switch_to.alert
assert (alert.text == ref_text_double)
print(alert.text)
time.sleep(1)
alert.accept()
time.sleep(1)

# driver.close()
