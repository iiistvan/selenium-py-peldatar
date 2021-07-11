# 021 Feladat: Lapozó kontrol feladatok
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

driver = webdriver.Chrome(ChromeDriverManager().install())
# a szűrt lista
filter_a = []

try:
    driver.get("http://localhost:9999/pagination.html")
    while True:
        # Tábla és sorok azonosítása
        table = driver.find_element_by_xpath('//table[@id="contacts-table"]/tbody')
        rows = table.find_elements_by_tag_name("tr")
        time.sleep(2)
        # az adott oldal sorainak beolvasása
        for row in rows:
            data_row = {}
            cells = row.find_elements_by_tag_name("td")
            data_row["id"] = cells[0].text
            data_row["First name"] = cells[1].text
            data_row["Second name"] = cells[2].text
            data_row["Surname"] = cells[3].text
            data_row["Second Surname"] = cells[4].text
            data_row["Birth date"] = cells[5].text
            # az 'A'-val kezdődő keresztnevek szűrése és hozzáfűzése a listához
            if str.startswith(data_row["First name"], 'A'):
                filter_a.append(data_row)
        # a következő oldalakra kattintás, amíg van
        next_button = driver.find_element_by_id("next")
        if not next_button.is_enabled():
            break
        else:
            next_button.click()

finally:
    keys = filter_a[0].keys()
    with open('pagination.csv', 'a', newline='', encoding='utf-8') as fileA:
        writer = csv.DictWriter(fileA, keys)
        # Ha a fejléc is kell
        # writer.writeheader()
        writer.writerows(filter_a)
    driver.close()
