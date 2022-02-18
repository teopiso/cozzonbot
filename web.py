from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import pyshorteners

op = webdriver.ChromeOptions()
op.add_argument('headless')
op.add_argument("window-size=1920,1080");
op.add_argument("user-data-dir=C:/Users/PHRA/AppData/Local/Google/Chrome/User Data/Profile 3")

def get(start, end):
    web = webdriver.Chrome(executable_path='C:/Users/PHRA/Desktop/chromedriver.exe', options=op)
    web.get('https://www.viamichelin.it/')

    partenza = web.find_element_by_xpath('//*[@id="departure"]')
    arrivo = web.find_element_by_xpath('//*[@id="arrival"]')

    partenza.send_keys(start)
    arrivo.send_keys(end+'\n')
    x =web.current_url
    time.sleep(5)
    web.save_screenshot("screenshot.png")
    web.quit()
    s = pyshorteners.Shortener()
    return s.tinyurl.short(x)
