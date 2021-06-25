# Kitchensink - find by id, name, xpath - attributes and text


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://localhost:9999/kitchensink.html")


def query_by_id(ids):
    for q in ids:
        try:
            q_name = driver.find_element_by_id(q).get_attribute("name")
            q_value = driver.find_element_by_id(q).get_attribute("value")
            q_type = driver.find_element_by_id(q).get_attribute("type")

            print("element id -", q)
            print("name:", q_name)
            print("value:", q_value)
            print("type:", q_type, "\n")

        except:
            print("valami nem stimmel")


def query_by_name(names):
    for q in names:
        try:
            q_text = driver.find_element_by_name(q).get_attribute("text")
            q_id = driver.find_element_by_name(q).get_attribute("name")
            q_value = driver.find_element_by_name(q).get_attribute("value")
            q_type = driver.find_element_by_name(q).get_attribute("type")

            print("element name -", q)
            print("text: ", q_text)
            print("id:", q_id)
            print("value:", q_value)
            print("type:", q_type, "\n")

        except:
            print("valami nem stimmel")


def query_by_xpath(path):
    for q in path:
        try:
            q_text = driver.find_element_by_xpath(q).text
            q_name = driver.find_element_by_xpath(q)
            # q_value = driver.find_element_by_xpath(q).value
            # q_type = driver.find_element_by_xpath(q).type

            print("element name:", q)
            print("text: ", q_text)
            print("name:", q_name.get_attribute('name'))

        except:
            print("valami nem stimmel")


qlist_id = ["bmwradio", "bmwcheck", "carselect"]
qlist_name = ["multiple-select-example", "courses"]
# kis, -nagybetű számít!
qlist_path = ["//*[@id='radio-btn-example']/fieldset/label[@for='bmw']/input", "//*[@id='carselect']/option[@value='bmw']",
              "//*[@id='checkbox-example']/fieldset/label[@for='bmw']"]

query_by_id(qlist_id)
query_by_name(qlist_name)
query_by_xpath(qlist_path)

driver.close()
