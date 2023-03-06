from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import numpy as np
import time

browser = webdriver.Chrome()
# browser.implicitly_wait(10) # seconds
browser.get('http://cntd.cityghg.com/pages/database')
title_dic={"行业领域":0,"技术类型":1,"工艺环节":2,"技术名称":3,"技术说明":4}
allVal_dic={}
# activity = WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, "activity")))
nav=browser.find_element(By.CLASS_NAME, "sidebar-container")
nav_lis=nav.find_elements(By.CSS_SELECTOR, "li")
domain="default"
for ni in range(len(nav_lis)):
    if ni!=15:
        continue
    nav_li_btn=nav_lis[ni]
    domain=nav_li_btn.text
    print(domain)
    nav_li_btn.click()
    time.sleep(10)
    activity=browser.find_element(By.CLASS_NAME, "activity")
    act_divs=activity.find_elements(By.CSS_SELECTOR, "div")
#     itemDiv=activity.find_element(By.CLASS_NAME, "item-info")
    act_div_len=len(act_divs)
    time.sleep(10)
    print(act_div_len)
    for ai in range(int(act_div_len/3)):
        itemDiv=act_divs[ai*3+1]
        tech_type=itemDiv.text
        print(tech_type)
        li_btns=act_divs[ai*3+2].find_elements(By.CSS_SELECTOR, "li")
        for li_btn in li_btns:
            gongyi=li_btn.find_element(By.CLASS_NAME, "second-type-title").text
            print(domain+"->"+tech_type+"->"+gongyi)
            li_btn.click()
            time.sleep(5)
            table= li_btn.find_element(By.CSS_SELECTOR,"table")
            trs=table.find_elements(By.CSS_SELECTOR,'tr')
            trsLen=len(trs)
            print(trsLen)
            for tbi in range(int(trsLen/4)):
                tech_name=trs[tbi*4+0].text.replace(' ','-')
                tds_title=trs[tbi*4+1].find_elements(By.CSS_SELECTOR,'td')
                tds_val=trs[tbi*4+2].find_elements(By.CSS_SELECTOR,'td')
                remark=trs[tbi*4+3].text
                vList=[0]*200
                vList[0]=domain
                vList[1]=tech_type
                vList[2]=gongyi
                vList[3]=tech_name
                vList[4]=remark
                print(domain+"->"+tech_type+"->"+gongyi+"->"+tech_name+"->"+remark)
                for i in range(len(tds_title)):
                    title=tds_title[i].text.replace('\n','')
                    if title not in title_dic:
                        title_dic[title]=len(title_dic)
                    val=tds_val[i].find_element(By.CSS_SELECTOR,".prop-value").text
                    vList[title_dic[title]]=val
                    print(title+":"+val,end=",")
                print("\n")
                allVal_dic[domain+"->"+tech_type+"->"+gongyi+"->"+tech_name]=vList

f=open("cntd/"+domain+".csv",mode='a',encoding='utf-8')
for t in title_dic:
    print(t)
    f.write(t+",")
f.write('\n')
for key in allVal_dic:
    print(key)
    for t in title_dic:
        print(t+":"+str(allVal_dic[key][title_dic[t]]))
        f.write(str(allVal_dic[key][title_dic[t]])+",")
    f.write('\n')
f.close()
