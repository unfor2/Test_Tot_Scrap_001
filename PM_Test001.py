

from selenium import webdriver
import time

option = webdriver.ChromeOptions().add_argument(' — incognito')
#option.add_argument(“ — incognito”)

page_URL = "https://www.parimatch.ge/"


driver = webdriver.Chrome("/home/unfor2/PycharmProjects/TestTot001/venv/selenium/webdriver/chromedriver", chrome_options=option)
driver.get(page_URL)
time.sleep(10)

tab_title = driver.find_elements_by_class_name("tab__title").click()



live_blocks = driver.find_element_by_class_name("live-block-row")

live_blocks

print(driver.find_element_by_class_name("live-block-row").text)



driver.close()

"""from bs4 import BeautifulSoup as bs
import requests

page_URL = "https://www.parimatch.ge/prematch/all/1|F|F_INTERN|PT61:520352646"

page = requests.get(page_URL)

soup = bs(page.content, 'html.parser')

print(soup) """
