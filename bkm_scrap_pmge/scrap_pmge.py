from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import psycopg2
from datetime import date



def readParimatch () :
    tot_code = 'parimatch.ge'
    year_now = date.today()
    year_str = '{}'.format(year_now.year)

    conn_string = "host='localhost' dbname='tot_scrap_01' user='postgres' password='`12'"
    con = psycopg2.connect(conn_string)
    con.autocommit = True
    cur = con.cursor()
    cur.execute('delete from tbl_save_info_ver001 where "Bookmaker" = \'{}\' '.format(tot_code))
    #print('delete from tbl_save_info_ver001 where "Bookmaker" = ''{}'' '.format(tot_code))

    insert_statement = '''INSERT INTO tbl_save_info_ver001 ("Bookmaker", "SportName_original", "EventGroup_original", "EventTime", 
                                      "EventTimeStr", "EventCode", "Player_1_original", "Player_2_original", "Bet_Type_original",
                                      "Bet_koef") VALUES (%s, %s, %s, to_timestamp(%s, 'YYYY-MM-DD HH24:MI'), %s, %s, %s, %s, %s, %s)'''


    timeout = 5
    page_URL = "https://www.parimatch.ge/en/"
    option = webdriver.ChromeOptions().add_argument(' — incognito')
    chromedriverpath =  os.path.dirname(os.path.realpath(__file__))[0:-14] + '/venv/selenium/webdriver/chromedriver.exe'
    chromedriver_path = os.path.normpath(chromedriverpath)
    #print(chromedriver_path)


    #driver = webdriver.Chrome("/home/unfor2/PycharmProjects/TestTot001/venv/selenium/webdriver/chromedriver", chrome_options=option)
    driver = webdriver.Chrome(chromedriver_path, chrome_options=option)
    driver.get(page_URL)
    WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "//html//body//div[3]//route//center-block//main//aside[1]//sidemenu//sidemenu-block[3]//div//div[2]//div//sidemenu-prematch")))
    #time.sleep(5)
    #driver.find_elements_by_xpath('//*[@id="wrapper"]/route/center-block/site-header/header/div[1]/div/div[1]/div/settings-dropdown/dropdown')[0].click()
    #driver.find_elements_by_link_text('EN')[0].click()
    #time.sleep(timeout)
    event_blocks = driver.find_elements_by_class_name("sportbox-head__add") # Читаем все виды спорта
    for l_bl in event_blocks:
        # Для всех видов спорта
        event_blocks = l_bl.find_elements_by_class_name("sportbox-head__title_link") #находим его на название
        for e_bl_l in event_blocks:
            sport_name = e_bl_l.get_attribute("html")
            #print(sport_name)

        event_chck = l_bl.find_elements_by_class_name("checkbox ")
        for l_bl_e in event_chck:
            try:
                l_bl_e.click()
                WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH,
                                                                                       "//html//body//div[3]//route//center-block//main//section//route//prematch-overview//div//prematch-sports//prematch-sport")))

                time.sleep(5)
                championship_block = driver.find_elements_by_class_name("live-block-championship")
                for it_chmp_bl in championship_block:
                    championship_name = it_chmp_bl.find_element_by_class_name("championship-name-title__text").text
                    koefs_title_block = it_chmp_bl.find_elements_by_class_name("market-names-shortcut")
                    koef_titles = [cap.text.strip() for cap in koefs_title_block]
                    live_block_rows = it_chmp_bl.find_elements_by_class_name("live-block-row")
                    for l_bl_r in live_block_rows:
                        event_code = 'pmge.' + l_bl_r.find_element_by_class_name('live-block-event-number').text
                        comps = l_bl_r.find_elements_by_class_name("competitor-name")
                        Competitors_list = [c.get_attribute("title").strip() for c in comps]
                        Competitors_list.append("")
                        #print("-Comp: {} - {} ###  {}".format(Competitors_list[0], Competitors_list[1], championship_name, ))
                        tar = l_bl_r.find_element_by_class_name("live-block-time").text.strip()
                        tar_year = '{}-{}'.format(year_str, tar[3:5] + '-' + tar[0:2] + ' ' + tar[6:])
                        #print(tar, tar_year)
                        #tar_year = tar_year.replace('.', '-').replace('/', '-')
                        koefs = l_bl_r.find_elements_by_class_name("outcome__coeff")
                        i = 0
                        try:
                            for l_koef in koefs:
                                st_koef = l_koef.text.strip()
                                if st_koef != "" :
                                    #print(insert_statement %("parimatch.ge", sport_name, championship_name, tar_year, tar, event_code, Competitors_list[0], Competitors_list[1], koef_titles[i], st_koef))
                                    cur.execute(insert_statement, (tot_code, sport_name, championship_name, tar_year, tar, event_code, Competitors_list[0], Competitors_list[1], koef_titles[i], st_koef))
                                    print("  {}: {} -- {}".format(i, koef_titles[i], st_koef))
                                i = i + 1
                        except :
                            print("no koefs")
                l_bl_e.click()
            except :
                print("Except")
    driver.close()
    cur.close()
    con.close()