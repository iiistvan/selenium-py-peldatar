# 011 Feladat: selenium táblázatok gyakorlása
import csv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import difflib
import filecmp
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://localhost:9999/editable-table.html")

# tesztadatok
tesztadat1 = ['bicycle', '299.99', '2', 'Sporting Goods']
tesztadat2 = ['tennis racket', '69.99', '10', 'Sporting Goods']
tesztadat3 = ['football', 'iPod Touch', 'iPhone 5']
tesztadat4 = ['12', '25.99', 'Asus Nexus 7']
tesztadat5 = [['baseball', 2, '12'], ['basketball', 1, '25.99'], ['nexus 7', 0, 'ASUS Nexus 7']]

add = driver.find_element_by_class_name("btn-success")
actions = ActionChains(driver)


def felvitel(tesztadat):
    add.click()
    time.sleep(2)
    sorok = driver.find_elements_by_class_name('eachRow')
    for sor in sorok[-1:]:
        oszlopok = sor.find_elements_by_xpath('./td/input')
        for i in range(4):
            oszlopok[i].clear()
            oszlopok[i].send_keys(tesztadat[i])
            actions.send_keys(Keys.TAB)
            actions.perform()
    driver.find_element_by_xpath('//input[@placeholder="Search..."]').click()


def ellenorzes(tc, tesztadat):
    sorok = driver.find_elements_by_class_name('eachRow')
    for sor in sorok[-1:]:
        oszlopok = sor.find_elements_by_xpath('./td/input')
        for i in range(4):
            # print(oszlopok[i])
            try:
                assert oszlopok[i].get_attribute('value') == tesztadat[i]
                print(f"{tc} Felvitel ellenőrzés eredménye: {i}.oszlop => OK")
            except:
                print(f"{tc} Felvitel ellenőrzés eredménye: {i}.oszlop => Gebasz!")
    driver.find_element_by_xpath('//input[@placeholder="Search..."]').click()


def kereses(str, tesztadat):
    driver.find_element_by_xpath('//input[@placeholder="Search..."]').send_keys(str)
    time.sleep(2)
    elso_oszlopok = []
    sorok = driver.find_elements_by_class_name('eachRow')
    for sor in sorok:
        elso_oszlop = sor.find_element_by_xpath('./td[1]/input').get_attribute('value')
        elso_oszlopok.append(elso_oszlop)
    print(f"Keresés eredménye: {elso_oszlopok}", end=' => ')
    try:
        assert elso_oszlopok == tesztadat
        print('OK')
    except:
        print('Gebasz!')


def modosit(tesztadat):
    driver.find_element_by_xpath('//input[@placeholder="Search..."]').click()
    actions.send_keys(Keys.DELETE)
    actions.perform()
    time.sleep(2)
    sorok = driver.find_elements_by_class_name('eachRow')
    for sor in sorok:
        time.sleep(1)
        oszlopok = sor.find_elements_by_xpath('./td/input')
        for i in range(len(tesztadat5)):
            if oszlopok[0].get_attribute('value') == tesztadat[i][0]:
                oszlopok[tesztadat[i][1]].clear()
                oszlopok[tesztadat[i][1]].send_keys(tesztadat[i][2])

    driver.find_element_by_xpath('//input[@placeholder="Search..."]').click()


def modositas_ellenorzes(tesztadat):
    sorok = driver.find_elements_by_class_name('eachRow')
    for sor in sorok:
        oszlopok = sor.find_elements_by_xpath('./td/input')
        for i in range(len(tesztadat5)):
            if oszlopok[0].get_attribute('value') == tesztadat[i][0] or oszlopok[0].get_attribute('value') == \
                    tesztadat[i][2]:
                try:
                    assert oszlopok[tesztadat[i][1]].get_attribute('value') == tesztadat[i][2]
                    print(f"{i + 1}. módosítás ellenőrzésének eredménye: {i}.oszlop => OK")
                except:
                    print(f"{i + 1}. módosítás ellenőrzésének eredménye: {i}.oszlop => Gebasz!")
    driver.find_element_by_xpath('//input[@placeholder="Search..."]').click()


# a) 2 sor hozzáadása és ellenőrzése
felvitel(tesztadat1)
ellenorzes('TC1', tesztadat1)
felvitel(tesztadat2)
ellenorzes('TC2', tesztadat2)
time.sleep(2)

# b) keresés funkció
kereses('o', tesztadat3)
kereses('o', ['football'])
time.sleep(2)

# c) módosítás és ellenőrzése funkció
modosit(tesztadat5)
time.sleep(2)
modositas_ellenorzes(tesztadat5)
time.sleep(2)

driver.close()
