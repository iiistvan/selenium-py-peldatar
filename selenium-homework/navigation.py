# navigáció az oldalon található linkekre, href és megnyitott url vizsgálata
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://localhost:9999/general.html")


def ahref_list():  # a linkek listába gyűjtése
    an_list = blank_list = []
    blank_list = driver.find_elements_by_xpath('//a[@href][@target="_blank"]')
    a_list = driver.find_elements_by_xpath('//a[@href]')

    print("A kigyűjtött", len(a_list)-len(blank_list), "db link: ")
    for elem in a_list:
        if elem in blank_list:
            continue
        an_list.append(elem)
        print(elem.get_attribute("href"))
    a_list = an_list
    return a_list


def link_parse(a_list):  # a linkek vizsgálata
    for elem in a_list:
        try:
            elem.click()
            # time.sleep(1.0)
            if (elem.get_attribute("href") == driver.current_url):
                print(elem.text, elem.get_attribute("href"), "OK")
            else:
                print(elem.text, elem.get_attribute("href"), "Eltérés")
                # driver.switch_to.alert.dismiss()
                time.sleep(1.0)
                driver.close(driver.current_url)
            time.sleep(1.0)
            driver.back
            # time.sleep(1.0)
        except:
            # driver.switch_to.alert.dismiss()
            pass

link_element_list = ahref_list()
print("*" * 100)
link_parse(link_element_list)

driver.close()
