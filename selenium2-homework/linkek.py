# localhost:9999 oldal linkjeinek kigyűjtése és fájlba írása

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://localhost:9999")


# a linkek listába gyűjtése
def ahref_list():
    a_list = driver.find_elements_by_xpath('//a[@href]')
    l_list = []
    for elem in a_list:
        l_list.append(elem.get_attribute("href"))
    print(len(l_list), "db linket találtam.")
    driver.close()
    return l_list


# lista kiiratása fájlba
def file_write(l_list):
    with open("linkek.txt", "a") as file1:
        file1.write("\n".join(l_list))


link_list = ahref_list()
file_write(link_list)
