
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
            '//*[@id="11588030"]/td[4]/font')]

    return scores


def parse(soup):
    pass


def load_gspread(creds_file_path, spread_name):
    gc = gspread.service_account(filename=creds_file_path)
    sh = gc.open(spread_name)
    return sh


def update_webassign(sh, sheet_name, scores):
    worksheet = sh.worksheet(sheet_name)
    worksheet.update('J1', int(scores[0]))
    scores.pop(0)
    for i in range(len(scores)):
        worksheet.update(f'J{3 + i}', int(scores[i]))


if __name__ == "__main__":

    import yaml
    import time
    import gspread
    import datetime
    from selenium import webdriver
    from selenium.webdriver.support.ui import Select

    driver = webdriver.Chrome(executable_path='wa_worker/chromedriver.exe')

    WA_email = 'stevenwilsonnunez@ufm.edu'
    WA_password = 'Kelpforest13?'

    login(WA_email, WA_password)
    go_to_class("MC 106, section A, Fall 2020")

    student_scores = get_student_scores()
    print(student_scores)

    sh = load_gspread('wa_worker/creds.json', 'scrapetosheets')
    update_webassign(sh,
                     'NotasFinales',  student_scores)
