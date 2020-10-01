import time
import gspread
import requests
import pandas as pd

from selenium import webdriver
from selenium.webdriver.support.ui import Select

from loginDetails import username, password


class WebAssign():

    driver = webdriver.Chrome(executable_path='worker/chromedriver.exe')

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        WebAssign.driver.get('https://www.webassign.net/wa-auth/login')
        WebAssign.driver.find_element_by_id('email').send_keys(self.username)
        WebAssign.driver.find_element_by_id(
            'cengagePassword').send_keys(self.password)
        WebAssign.driver.find_element_by_name('Login').click()
        time.sleep(10)

    def go_to_class(self, class_name):
        WebAssign.driver.find_element_by_xpath(
            '//*[@id="list"]/li[5]/a').click()
        WebAssign.driver.find_element_by_xpath(
            '//*[@id="list"]/li[5]/ul/li[3]/a').click()

        select = Select(WebAssign.driver.find_element_by_id('scourse'))
        select.select_by_visible_text(class_name)

    def get_student_scores(self):
        table = WebAssign.driver.find_element_by_xpath(
            '//*[@id="table-wrapper"]/div[1]/div[2]/table')

        scores = []
        for row in table.find_elements_by_xpath(".//tr"):
            [scores.append(td.text) for td in row.find_elements_by_xpath(
                './/td[4]/font')]

        total = WebAssign.driver.find_element_by_xpath(
            '//*[@id="table-wrapper"]/div[1]/div[1]/table/tbody/tr[2]/td[2]/font').text
        return scores, total


class Storage():

    gc = gspread.service_account(filename='worker/creds.json')

    def __init__(self, spreadsheet, worksheet):
        self.spreadsheet = Storage.gc.open(spreadsheet)
        self.worksheet = self.spreadsheet.worksheet(worksheet)

    def update_spreadsheet_scores(self, scores, total):
        self.worksheet.update('J1', int(total))

        for i in range(len(scores)):
            self.worksheet.update(f'J{i+3}', int(scores[i]))

    def get_all_values(self):
        return self.worksheet.get_all_values()


if __name__ == "__main__":

    user = WebAssign(username, password)

    user.login()
    user.go_to_class('MC 106, section A, Fall 2020')
    scores, total = user.get_student_scores()

    print(scores, total)

    calculo_integral_storage = Storage('scrapetosheets', 'NotasFinales')
    calculo_integral_storage.update_spreadsheet_scores(scores, total)

    data = calculo_integral_storage.get_all_values()
    data = [list[1:] for list in data]
    headers = data.pop(0)

    df = pd.DataFrame(data, columns=headers)

    API_ENDPOINT = 'http://www.vermisnotas.xyz/ver-notas'

    # r = requests.post(url=API_ENDPOINT, data=data)

    # print(r.text)
