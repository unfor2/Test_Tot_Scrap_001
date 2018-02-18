from selenium import webdriver
import time
import os

option = webdriver.ChromeOptions().add_argument(' — incognito')

page_URL = "https://www.parimatch.ge/"

chromedriver_path = os.path.normpath(os.path.dirname(os.path.realpath(__file__)) + '/venv/selenium/webdriver/chromedriver.exe')
print(chromedriver_path)


#driver = webdriver.Chrome("/home/unfor2/PycharmProjects/TestTot001/venv/selenium/webdriver/chromedriver", chrome_options=option)
driver = webdriver.Chrome(chromedriver_path, chrome_options=option)
driver.get(page_URL)
time.sleep(5)

event_blocks = driver.find_elements_by_class_name("sportbox-head__add") # Читаем все виды спорта

for l_bl in event_blocks:
    # Для всех видов спорта
    event_blocks = l_bl.find_elements_by_class_name("sportbox-head__title_link") #находим его на название
    for e_bl_l in event_blocks:
        print(e_bl_l.get_attribute("html"))
    event_chck = l_bl.find_elements_by_class_name("checkbox ")
    for l_bl_e in event_chck:
        try:
            l_bl_e.click()
            time.sleep(5)
            championship_block = driver.find_elements_by_class_name("live-block-championship")
            for it_chmp_bl in championship_block:
                championship_name = it_chmp_bl.find_element_by_class_name("championship-name-title__text").text
                koefs_title_block = it_chmp_bl.find_elements_by_class_name("market-names-shortcut")
                koef_titles = [cap.text.strip() for cap in koefs_title_block]
                live_block_rows = it_chmp_bl.find_elements_by_class_name("live-block-row")
                for l_bl_r in live_block_rows:
                    comps = l_bl_r.find_elements_by_class_name("competitor-name")
                    Competitors_list = [c.get_attribute("title").strip() for c in comps]
                    Competitors_list.append("")
                    print("-Comp: {} - {} ###  {}".format(Competitors_list[0], Competitors_list[1], championship_name))
                    tar = l_bl_r.find_element_by_class_name("live-block-time").text
                    koefs = l_bl_r.find_elements_by_class_name("outcome__coeff")
                    i = 0
                    try:
                        for l_koef in koefs:
                            st_koef = l_koef.text.strip()
                            if st_koef != "" :
                                print("  {}: {} -- {}".format(i, koef_titles[i], st_koef))
                            i = i + 1
                    except:
                        print("no koefs")
            l_bl_e.click()
        except:
            print("Except")


driver.close()
