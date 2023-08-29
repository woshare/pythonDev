from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import numpy as np
import time

browser = webdriver.Chrome()
# browser.implicitly_wait(10) # seconds
browser.get('https://www.lottery.gov.cn/kj/kjlb.html?dlt')
time.sleep(6)
iframes=browser.find_elements(By.CSS_SELECTOR,"iframe")
browser.switch_to.frame("iFrame1")

bodyDatas=browser.find_element(By.ID, "historyData")
trs=bodyDatas.find_elements(By.CSS_SELECTOR,"tr")
trLen=len(trs)
allVal={}
for tri in range(int(trLen)):
    tr=trs[tri]
    tds=tr.find_elements(By.CSS_SELECTOR,"td")
    tdLen=len(tds)
    vList=[0]*9
    for i in range(9):
        vList[i]=tds[i].text
    allVal[tds[0].text]=vList
    print(vList)
#act_divs=frame.find_elements(By.CSS_SELECTOR, "title").text

#print(browser.page_source)
