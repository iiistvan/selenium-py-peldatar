# trickyelements - find by id - button

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://localhost:9999/trickyelements.html")

# for item in ["element1", "element2", "element3", "element4", "element5"]:
#    i = (driver.find_element_by_id(item))
#    if driver.find_element_by_tag_name(i) == "button":
#        print("gomb")
#        i.click()
#    else:
#        print(i)
buttons = driver.find_elements_by_xpath('//button[@id]')
print(buttons)
print(type(buttons))

if len(buttons) == 0:
    print('nincs gomb')
else:
    for button in buttons:
        button.click()
        result = driver.find_element_by_xpath('//label[@id="result"]')
        print(result.text)
        assert (result.text == f"{button.text} was clicked")
        break

# driver.close()
