# 019 Feladat: videó lejátszás kihívások
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

driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    driver.get("http://localhost:9999/videos.html")
    # HTML5 video built in controls tesztje
    video1 = driver.find_element_by_id("html5video")
    video1.send_keys(Keys.SPACE)
    time.sleep(5)
    video1.send_keys(Keys.SPACE)

    # HTML5 video with custom controls tesztje
    video2 = driver.find_element_by_xpath('//button[contains(text(), "Play/Pause")]')
    video2.click()
    time.sleep(5)
    video2.click()

    # Embedded youtube video in iframe tesztje
    video3 = driver.find_element_by_id('youtubeframe')
    video3.click()
    time.sleep(5)
    video3.click()


finally:
    driver.close()
