# 017 Feladat: komplett űrlap tesztelés
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import sys

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://localhost:9999/simplevalidation.html")

action = ActionChains(driver)
action = action.send_keys(Keys.TAB)
action.perform()
time.sleep(1)

# mező hibaüzenetek, hozzá tesztadatok

# # # textarea mezők //div[@class="form-group"]/div/textarea
# # text_err = ["This field can't be empty"]
# test-random-textarea
#
# # # select mezők //div[@class="form-group"]/div/select
# # cardtype_err = ['Please select a card type'] # sel,card type választás után a VISA választásánál hibát dob
# test-card-type
# # expMonth_err = ['Select a month']
# test-card-month
# # expYear_err = ['Select a year', 'Appears to be expired - please check date'] # év, hónap együtt vizsgálva 2021/06
# test-card-year

# # singlecheckvalidate /id
# checkbox_err = ["This field can't be empty"]

# # radiovalidate /id
# recEmail_err = []

# # checkboxvalidate /id
# agreeServ_err = ['Please agree to both to continue']
# agreeStuff_err = ['Please agree to both to continue'] # mindkettőt jelölni kell!!!
#
# # gomb elérése
# button = driver.find_element_by_id('test-button')

# input label for mezők
input_for_list = ['test-email',
                  'test-password',
                  'test-confirm-password',
                  'test-customer-number',
                  'test-dealer-number',
                  'test-random-field',
                  'test-date-field',
                  'test-url-field',
                  'test-card-number',
                  'test-card-cvv']

# input hibaüzenet mezők
input_err_list = [["Please enter an e-mail", "Login does not exist", "Please check your E-Mail format"],
                  ["Should be between 6 and 20 characters", "This field can't be empty"],
                  ["Does not match Desired Password", "This field can't be empty"],
                  ["This field can't be empty"],
                  ["This field can't be empty", 'Should be a 4 character number'],
                  [],  # 'Should contain \\"twelve\\"' MEGOLDÁSRA VÁR: idézőjel probléma!
                  ["This field can't be empty", 'Must match pattern YYYY-MM-DD'],
                  [],
                  # 'Please enter a valid URL (starts with \\"http\\" or \\"https\\")'], MEGOLDÁSRA VÁR: idézőjel probléma!
                  ["Please enter a credit card number (no spaces)", "Please check your credit card nubmer"],
                  ["Should be a number between 3 and 4 characters", "This field can't be empty"]]

# input adatmezők
input_data_list = [[' ', 'x@x.hu', 'x@x', 'yardy@yarr.com'],
                   ['123', '', '123456'],
                   ['123', '', '123456'],
                   [' ', '1'],
                   [' ', '1', '12345', '1234'],
                   ['', 'twelve'],
                   [' ', '2021/01/01', '0000-00-00'],
                   ['http://hu.hu'],
                   [' ', '111111', '4111111111111111'],
                   ['1', ' ', '1234', 'abc']]

# késleltetés
ts = 2


def input_validator(input_elements):
    # input_elements = driver.find_elements_by_xpath('//div[@class="form-group"]/div/input')
    for e, i in enumerate(input_elements):
        for n in range(len(input_err_list[e])):
            i.clear()
            time.sleep(ts)
            i.send_keys(input_data_list[e][n])
            time.sleep(ts)
            text = input_err_list[e][n]
            assert (i.find_element_by_xpath('../../div[2][contains(text(), "' + text + '")]')).is_displayed()
            time.sleep(ts)
        i.clear()
        time.sleep(ts)
        i.send_keys(input_data_list[e][-1])
        time.sleep(ts)
        assert driver.find_element_by_xpath('//label[@for= "' + input_for_list[e] + '"]').is_enabled()
        # assert driver.find_element_by_xpath('//label[@for= "' + input_for_list[e] + '"]/../div[contains(@class, "form-field-valid")]').is_enabled()
        time.sleep(ts)

# input text mezők kigyűjtése
x = driver.find_elements_by_xpath('//div[contains(@class, "form-group")]/div/input')
print(len(x))
input_validator(x)
