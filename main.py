from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import requests
import random
import undetected_chromedriver.v2 as uc
import os
import pyautogui
import threading


def lay_ip(api_key): # Hàm để lấy IP Privater Vip 16k/ngày của https://tinsoftproxy.com/
    url_get_ip = 'http://proxy.tinsoftsv.com/api/changeProxy.php?key='+api_key
    ip_about = requests.get(url_get_ip).json()
    try:
        ip = ip_about['proxy'] # Lấy IP
        print(ip)
        return ip
    except:
        time_dely = ip_about['next_change']
        print('Vui lòng đợi '+str(time_dely)+'s để lấy IP mới')
        time.sleep(int(time_dely))
        return lay_ip(api_key)






def runnow(n):
    link = open('link.txt','r',encoding='utf-8').read()
    while True:
        try:    
                api_key = open('api_key.txt','r',encoding='utf-8')
                api_key = api_key.read().splitlines() # Lấy api_key để sử dụng 
                name = open('name.txt','r',encoding='utf-8').read().splitlines()
                tele = random.choice(name)
                tw = random.choice(name)
                opts = uc.ChromeOptions()
                opts.add_argument(f'--proxy-server='+lay_ip(api_key[n]))
                driver = uc.Chrome(options=opts)
                x = 384*n
                driver.set_window_rect(x,0,384,1080)
                driver.get(link)
                time.sleep(10)
                pyautogui.scroll(-4000)
                time.sleep(1)
                driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[3]/div[2]/div[1]/input').send_keys(random.choice(name))
                gmail = open('gmail.txt','r',encoding='utf-8').read().splitlines()[n]
                driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[3]/div[2]/div[2]/input').send_keys(gmail)
                time.sleep(5)
                driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[3]/div[2]/div[4]/button').click()
                time.sleep(5)
                try:
                    if driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[5]/div/div').text == 'This entry has been flagged by our anti-spam system. (31)':
                        print("Lỗi IP, chờ đổi IP mới.")
                        driver.quit()
                        continue
                except:
                    pass
                try:
                    driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[5]/div/div[6]/div[1]/div/div[1]/div[2]').click()
                    time.sleep(1)
                    u = open('gmail.txt','r',encoding='utf-8').read().splitlines()
                    u.remove(gmail)
                    updategmail = '\n'.join(u)
                    u1 = open('gmail.txt','w',encoding='utf-8')
                    u1.write(updategmail)
                    u1.close()
                    
                    driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[5]/div/div[6]/div[1]/div/div[2]/div[1]/div/div/a').click()
                    time.sleep(1)
                    driver.switch_to.window(driver.window_handles[0])
                    time.sleep(1)
                    driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[5]/div/div[6]/div[1]/div/div[2]/div[2]/div/div/input[1]').send_keys(tele)
                    time.sleep(1)
                    driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[5]/div/div[6]/div[1]/div/div[2]/div[2]/div/div/input[1]').send_keys(Keys.ENTER)
                    time.sleep(1)
                    driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[5]/div/div[6]/div[1]/div/div[1]/div[2]').click()
                    time.sleep(1)
                    driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[5]/div/div[6]/div[2]/div/div[1]/div[2]').click()
                    time.sleep(1)
                    driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[5]/div/div[6]/div[2]/div/div[2]/div[1]/div/div/a').click()
                    time.sleep(1)
                    driver.switch_to.window(driver.window_handles[0])
                    time.sleep(1)
                    driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[5]/div/div[6]/div[2]/div/div[2]/div[2]/div/div/input[1]').send_keys(tele)
                    time.sleep(1)
                    driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[5]/div/div[6]/div[2]/div/div[2]/div[2]/div/div/input[1]').send_keys(Keys.ENTER)
                    time.sleep(1)
                    driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[5]/div/div[6]/div[2]/div/div[1]/div[2]').click()
                    time.sleep(1)
                    driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[5]/div/div[6]/div[3]/div/div[1]/div[2]').click()
                    time.sleep(1)
                    driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[5]/div/div[6]/div[3]/div/div[2]/div[1]/div/div/a').click()
                    time.sleep(1)
                    driver.switch_to.window(driver.window_handles[0])
                    time.sleep(1)
                    driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[5]/div/div[6]/div[3]/div/div[2]/div[2]/div/div/input[1]').send_keys(tele)
                    time.sleep(1)
                    driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[5]/div/div[6]/div[3]/div/div[2]/div[2]/div/div/input[1]').send_keys(Keys.ENTER)
                    time.sleep(1)
                    driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[5]/div/div[6]/div[3]/div/div[1]/div[2]').click()
                    time.sleep(1)
                    driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[5]/div/div[6]/div[4]/div/div[1]/div[2]').click()
                    time.sleep(1)
                    driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[5]/div/div[6]/div[4]/div/div[2]/div[1]/div/div/a').click()
                    time.sleep(1)
                    driver.switch_to.window(driver.window_handles[0])
                    time.sleep(1)
                    driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[5]/div/div[6]/div[4]/div/div[2]/div[2]/div/div/input[1]').send_keys(tw)
                    time.sleep(1)
                    driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[5]/div/div[6]/div[4]/div/div[2]/div[2]/div/div/input[1]').send_keys(Keys.ENTER)
                    time.sleep(1)
                    driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[5]/div/div[6]/div[4]/div/div[1]/div[2]').click()
                    time.sleep(1)
                    driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[5]/div/div[6]/div[5]/div/div[1]/div[2]').click()
                    time.sleep(1)
                    driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[5]/div/div[6]/div[5]/div/div[2]/div[1]/div/div/a').click()
                    time.sleep(1)
                    driver.switch_to.window(driver.window_handles[0])
                    time.sleep(1)
                    driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[5]/div/div[6]/div[5]/div/div[2]/div[2]/div/div/input[1]').send_keys(tw)
                    time.sleep(1)
                    driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[5]/div/div[6]/div[5]/div/div[2]/div[2]/div/div/input[1]').send_keys(Keys.ENTER)
                    time.sleep(1)
                    driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[5]/div/div[6]/div[5]/div/div[1]/div[2]').click()
                    time.sleep(1)
                    driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[5]/div/div[6]/div[6]/div/div[1]/div[2]').click()
                    time.sleep(1)
                    
                    
                    vi  = open('vi.txt','r',encoding='utf-8').read().splitlines()[n]
                    driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[5]/div/div[6]/div[6]/div/div[2]/div/div/div/div/input[1]').send_keys(vi)
                    time.sleep(1)
                    driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[5]/div/div[6]/div[6]/div/div[2]/div/div/div/div/input[1]').send_keys(Keys.ENTER)
                    z = open('vi.txt','r',encoding='utf-8').read().splitlines()
                    z.remove(vi)
                    vizz = '\n'.join(z)
                    z1 = open('vi.txt','w',encoding='utf-8')
                    z1.write(vizz)
                    z1.close()
                    time.sleep(5)
                except:
                    
                    u = open('gmail.txt','r',encoding='utf-8').read().splitlines()
                    u.remove(gmail)
                    updategmail = '\n'.join(u)
                    u1 = open('gmail.txt','w',encoding='utf-8')
                    u1.write(updategmail)
                    u1.close()
                    z = open('vi.txt','r',encoding='utf-8').read().splitlines()
                    z.remove(vi)
                    vizz = '\n'.join(z)
                    z1 = open('vi.txt','w',encoding='utf-8')
                    z1.write(vizz)
                    z1.close()
                    driver.quit()
                
                
                driver.quit()
        except:
                driver.quit()
def thread():
    ths = []
    for i in range(4):
        ths.append(threading.Thread(target=runnow,args={i,}))
    for iii in ths:
        iii.start()
        time.sleep(10)
    for iii in ths:
        iii.join()
thread()