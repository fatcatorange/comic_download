from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import wget
import os
import urllib.request
import ssl

def wait(classname):
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, classname))
    )

#不用ssl驗證
ssl._create_default_https_context = ssl._create_unverified_context

download_comic=input("想下載的漫畫:")
download_vol=input("想下載的集數:")

PATH="C:/Users/jason/Desktop/chromedriver_win32/chromedriver"
driver=webdriver.Chrome(PATH)
driver.get("https://comicbus.com/")

wait("search-box-main")

search=driver.find_element_by_id("key")
search.send_keys(download_comic)
search.send_keys(Keys.RETURN)

wait("col-2")

#點入第一個
comic=driver.find_element_by_class_name("col-2")
comic.click()

wait("Vol")

#集數
download_vol="c"+download_vol
vol=driver.find_element_by_id(download_vol)
vol.click()

#切分頁
driver.switch_to.window(driver.window_handles[1])



path=os.path.join("漫畫")
try:
    os.mkdir(path)
except:
    ()

save_comic=os.path.join(path,download_comic)

try:
    os.mkdir(save_comic)
except:
    ()

save_vol=os.path.join(save_comic,"第"+download_vol.replace("c","")+"集")
try:
    os.mkdir(save_vol)
except:
    ()

for now_page in range(300):
    try:
        wait("controlimg")
        page=driver.find_element_by_id("TheImg")
        save_page=os.path.join(save_vol,"page"+str(now_page+1)+".jpg")
        #print(page.get_attribute("src")) 檢查圖片網址
        wget.download(page.get_attribute("src"),save_page)
        #urllib.request.urlretrieve(page.get_attribute("src"),save_page) 第二種方法
        next_page=driver.find_element_by_id("next")
        next_page.click()
    except:
        print("end!")
        break
