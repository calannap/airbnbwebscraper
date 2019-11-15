import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import json

from info_model import InfoModel

EXE_PATH = './chromedriver'
driver = webdriver.Chrome(executable_path=EXE_PATH)

url = 'https://www.airbnb.co.uk/rooms/28299515?location=London%2C%20United%20Kingdom&toddlers=0' \
      '&_set_bev_on_new_domain=1572300146_ZKC6996OiM8G0CT3&source_impression_id=p3_1572300147_bRb1KSr%2FXjuPRPDg' \
      '&guests=1&adults=1 '

driver.get(url)

soup = BeautifulSoup(driver.page_source, "html.parser")

images = soup.find_all('img', {'src': re.compile('.jpg'), 'style': re.compile('top:0')})

description = []
for asd in soup.find_all('div', {'class': re.compile('_hgs47m')}):
    if len(asd.text) > 3:
        description.append(re.sub(r'[^\x00-\x7F]+', '', asd.text))




cookiesbutton = "/html/body/div[1]/div[2]/div[4]/div[2]/div/button"
WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, cookiesbutton))).click()
driver.find_element_by_xpath(cookiesbutton).click()

for i in range(0, 5):
    try:
        time.sleep(5)
        WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        "#amenities > div > div > div > div > div > section > div:nth-child(4) > div > button"))).click()
        driver.find_element_by_css_selector(
            "#amenities > div > div > div > div > div > section > div:nth-child(4) > div > button").click()
        break;
    except:
        print("Something didn't work")

asd = InfoModel(soup.title.text.split(' - ')[0], [i['src'] for i in images], ' '.join(description), driver.find_element_by_class_name('_7lvai1').text)

with open(soup.title.text.split(' - ')[0]+'.json', 'w') as f:
    f.write(json.dumps(asd.__dict__))
