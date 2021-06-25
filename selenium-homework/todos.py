# Kitchensink - find by id, name, xpath - attributes and text

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://localhost:9999/todo.html")


def todo_list():  # a teendők listázása
    td_list = driver.find_elements_by_xpath("//*[@class='done-false']")
    print("A teendők:")
    for td in td_list:
        print(" - ", td.text)
    print()


def done_list():  # az elvégzett feladatok beállítása
    dn_list = driver.find_elements_by_xpath("//*[@type='checkbox']")
    dn_list[0].click()
    dn_list[3].click()


# a teljes lista
todo_list()

# teszt az elvégzett feladatok jelölésével
done_list()
todo_list()

driver.close()
