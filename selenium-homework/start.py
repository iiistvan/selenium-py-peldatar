# egy tetszetős, jól használható weboldal megnyitása selenium-al Chrome-ban

from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.eredmenyek.com/foci/europa/euro/")


# driver.close()