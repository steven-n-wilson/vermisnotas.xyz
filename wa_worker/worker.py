import gspread
from selenium import webdriver
from selenium.webdriver.support.ui import Select

from loginDetails import email, cengagePassword


class WebAssign():

    driver = webdriver.Chrome(executable_path='wa_worker/chromedriver.exe')

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        WebAssign.driver.get('https://www.webassign.net/wa-auth/login')
        WebAssign.driver.find_element_by_id('email').send_keys(self.username)
        WebAssign.driver.find_element_by_id(
            'cengagePassword').send_keys(self.password)
        WebAssign.driver.find_element_by_name('Login').click()

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
                '//*[@id="11588030"]/td[4]/font')]

        return scores


class Storage():

    gc = gspread.service_account(filename='wa_worker/creds.json')

    def __init__(self, spreadsheet, worksheet):
        self.spreadsheet = Storage.gc.open(spreadsheet)
        self.worksheet = self.spreadsheet.worksheet(spreadsheet)

    # def load_worksheet(sh, sheet_name):
    #     worksheet = sh.worksheet(sheet_name)
    #     return worksheet

    def update_spreadsheet_scores(self, scores):
        self.worksheet.update('J1', int(scores[0]))
        del scores[0]

        for i in range(len(scores)):
            self.worksheet.update(f'J{i+3}', int(scores[i]))


if __name__ == "__main__":

    WA_email = 'stevenwilsonnunez@ufm.edu'
    WA_password = 'Kelpforest13?'

    login(WA_email, WA_password)
    go_to_class("MC 106, section A, Fall 2020")

    student_scores = get_student_scores()
    print(student_scores)

    sh = load_gspread('wa_worker/creds.json', 'scrapetosheets')
    worksheet = load_worksheet(sh, 'NotasFinales')

    update_webassign(worksheet, student_scores)
    list_of_lists = worksheet.get_all_values()
    print(list_of_lists[0])
    print(list_of_lists[1])
    print(list_of_lists[2])
