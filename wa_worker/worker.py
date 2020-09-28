
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


def get_student_scores():
    table = driver.find_element_by_xpath(
        '//*[@id="table-wrapper"]/div[1]/div[2]/table')
    scores = []
    for row in table.find_elements_by_xpath(".//tr"):
        [scores.append(td.text) for td in row.find_elements_by_xpath(
            '//*[@id="11475531"]/td[4]/font')]
    return scores


def request(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup


def parse(soup):
    pass


def output(notas):
    gc = gspread.service_account(filename='wa_worker/creds.json')
    sh = gc.open('scrapetosheets').sheet1
    sh.update('J1', int(notas[0]))
    notas.pop(0)
    for i in range(len(notas)):
        sh.update(f'J{3 + i}', int(notas[i]))


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

    student_scores = get_student_scores()
    output(student_scores)

    # current_url = driver.current_url
    # soup = request(current_url)
