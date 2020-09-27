
def login(username, password):
    driver.get('https://www.webassign.net/wa-auth/login')
    driver.find_element_by_id('email').send_keys(username)
    driver.find_element_by_id('cengagePassword').send_keys(password)
    driver.find_element_by_name('Login').click()
    time.sleep(10)


def go_to_class(class_name):
    driver.find_element_by_xpath('//*[@id="list"]/li[5]/a').click()
    driver.find_element_by_xpath('//*[@id="list"]/li[5]/ul/li[3]/a').click()
    select = Select(driver.find_element_by_id('scourse'))
    select.select_by_visible_text(class_name)


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


if __name__ == "__main__":

    import yaml
    import time
    import gspread
    import requests
    import datetime
    from bs4 import BeautifulSoup
    from selenium import webdriver
    from selenium.webdriver.support.ui import Select

    driver = webdriver.Chrome(executable_path='wa_worker/chromedriver.exe')

    WA_email = 'stevenwilsonnunez@ufm.edu'
    WA_password = 'Kelpforest13?'

    login(WA_email, WA_password)
    go_to_class("MC 106, section A, Fall 2020")

    current_url = driver.current_url

    soup = request(current_url)
    output(soup)
