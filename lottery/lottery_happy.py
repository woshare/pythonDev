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
allVal={}
f=open("lottery.csv",mode='a',encoding='utf-8')
f.write("期号,日期,前区1,前区2,前区3,前区4,前区5,后区1,后区2")
f.write("\n")
while True:
    time.sleep(3)
    bodyDatas=browser.find_element(By.ID, "historyData")
    trs=bodyDatas.find_elements(By.CSS_SELECTOR,"tr")
    trLen=len(trs)
    for tri in range(int(trLen)):
        tr=trs[tri]
        tds=tr.find_elements(By.CSS_SELECTOR,"td")
        tdLen=len(tds)
        vList=[0]*9
        firstContent=tds[0].text
        if firstContent=="派奖":
            continue
        if len(firstContent)<5:
            continue
        for i in range(min(9,tdLen)):
            vList[i]=tds[i].text
        #allVal[tds[0].text]=vList
        print(vList)
        for i in range(0,len(vList)):
            f.write(vList[i])
            if i<len(vList)-1:
                f.write(",")
        f.write("\n")
    btns=browser.find_elements(By.CSS_SELECTOR,".number.u-pad10")
    nextPageBtn=btns[2]
    nextPageBtn=btns[2].click()


# for key in allVal:
#     vs=allVal[key]
#     for i in range(0,len(vs)):
#          f.write(vs[i])
#          if i<len(vs)-1:
#             f.write(",")
f.close()
#act_divs=frame.find_elements(By.CSS_SELECTOR, "title").text

#print(browser.page_source)
