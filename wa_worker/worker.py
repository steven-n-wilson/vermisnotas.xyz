import yaml
import time
import gspread
import requests
import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select


def login(url, usernameId, username, passwordId, password, submit_buttonId):
    driver.get(url)
    driver.find_element_by_id(usernameId).send_keys(username)
    driver.find_element_by_id(passwordId).send_keys(password)
    driver.find_element_by_name(submit_buttonId).click()


def request(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup


def parse(soup):
    pass


def output(notas):
    gc = gspread.service_account(filename='wa_worker/creds.json')
    sh = gc.open('scrapetosheets').sheet1

    sh.update('A1', str(notas))


conf = yaml.load(open('wa_worker/loginDetails.yml'), Loader=yaml.FullLoader)
myWA_email = conf['webAssign_user']['email']
myWA_password = conf['webAssign_user']['cengagePassword']

driver = webdriver.Chrome(executable_path='wa_worker/chromedriver.exe')
login('https://www.webassign.net/wa-auth/login', 'email',
      myWA_email, 'cengagePassword', myWA_password, 'Login')

time.sleep(10)
driver.find_element_by_xpath('//*[@id="list"]/li[5]/a').click()
driver.find_element_by_xpath('//*[@id="list"]/li[5]/ul/li[3]/a').click()
# driver.find_element_by_xpath('//*[@id="scourse"]').click()
select = Select(driver.find_element_by_id('scourse'))
select.select_by_visible_text("MC 106, section A, Fall 2020")


current_url = driver.current_url

soup = request(current_url)
output(soup)
