# -*- coding:utf-8 -*-
import time
from selenium import webdriver
from bs4 import BeautifulSoup

tag = input('search tag : ')
url = 'https://www.instagram.com/explore/tags/' + tag

driver = webdriver.Chrome('/Users/parkgw/driver/chromedriver')

driver.implicitly_wait(3)
driver.get(url)
time.sleep(20)

soup = BeautifulSoup(driver.page_source, 'html.parser')
img_list = soup.find_all('div', class_='EZdmt')
print(img_list)

driver.close()
driver.quit()
