

from selenium import webdriver
import time
import os

option = webdriver.ChromeOptions().add_argument(' — incognito')
#option.add_argument(“ — incognito”)

page_URL = "https://www.parimatch.ge/"

chromedriver_path = os.path.normpath(os.path.dirname(os.path.realpath(__file__)) + '/venv/selenium/webdriver/chromedriver.exe')
print(chromedriver_path)


#driver = webdriver.Chrome("/home/unfor2/PycharmProjects/TestTot001/venv/selenium/webdriver/chromedriver", chrome_options=option)
driver = webdriver.Chrome(chromedriver_path, chrome_options=option)
driver.get(page_URL)
time.sleep(5)


#sportbox-head__title_link



#tab_title = driver.find_elements_by_class_name("tab__title").click()



#event_blocks = driver.find_elements_by_class_name("sportbox-head__title_link")

event_blocks = driver.find_elements_by_class_name("sportbox-head__add")

for l_bl in event_blocks:
    event_blocks = l_bl.find_elements_by_class_name("sportbox-head__title_link")
    for e_bl_l in event_blocks:
        print(e_bl_l.get_attribute("html"))
    event_chck = l_bl.find_elements_by_class_name("checkbox ")
    for l_bl_e in event_chck:
        try:
            l_bl_e.click()
            time.sleep(5)
            live_block_rows = driver.find_elements_by_class_name("live-block-row")
            for l_bl_r in live_block_rows:
                comps = l_bl_r.find_elements_by_class_name("competitor-name")
                for l_comps in comps:
                    print(l_comps.get_attribute("title"))
                tar = l_bl_r.find_element_by_class_name("live-block-time").text
                koefs = l_bl_r.find_elements_by_class_name("outcome__coeff")
                i = 0
                try:
                    for l_koef in koefs:
                        print("{} -- {}".format(i, l_koef.text))
                        i = i + 1
                except:
                    print("no koefs")
            l_bl_e.click()
        except:
            print("Except")


#print(driver.find_element_by_class_name("live-block-row").text)



driver.close()

"""from bs4 import BeautifulSoup as bs
import requests

page_URL = "https://www.parimatch.ge/prematch/all/1|F|F_INTERN|PT61:520352646"

page = requests.get(page_URL)

soup = bs(page.content, 'html.parser')

print(soup) """
