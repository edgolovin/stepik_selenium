import time
from selenium import webdriver

dr = webdriver.Chrome()
time.sleep(5)

dr.get("https://ya.ru")
time.sleep(5)

text_area = dr.find_element_by_id('text')

text_area.send_keys("duckduckgo")

find_btn = dr.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/form/div[2]/button')
find_btn.click()

time.sleep(5)

dr.quit()
