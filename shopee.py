from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time

opsi = webdriver.ChromeOptions()
opsi.add_argument('--headless')
servis = Service('chromedriver.exe')
driver = webdriver.Chrome(service=servis, options=opsi)


link = "https://shopee.co.id/search?keyword=vga%20nvidia"
driver.get(link)
time.sleep(5)

content = driver.page_source
driver.quit()

data = BeautifulSoup(content, 'html.parser')


i=1
for area in data.find_all('div', class_ ="col-xs-2-4 shopee-search-item-result__item"):
    print (i)
    nama = area.find('div', class_="ie3A+n bM+7UW Cve6sh").get_text()
    harga = area.find('span', class_="ZEgDH9").get_text()
    print(nama)
    print(harga)
    i+=1
    print('---------------------------------------------------')


    rentang = 500
    for i in range(1,7):
        akhir = rentang * i
        perintah = "window.scrollTo(0,"+str(akhir)+")"
        driver.execute_script(perintah)
        print("loading ke-"+str(i))
        time.sleep(1)