from selenium import webdriver
import yaml
import time

conf = yaml.load(open('loginDetails.yml'),
                 Loader=yaml.FullLoader)
myWA_email = conf['webAssign_user']['email']
myWA_password = conf['webAssign_user']['cengagePassword']


driver = webdriver.Chrome()


def login(url, usernameId, username, passwordId, password, submit_buttonId):
    driver.get(url)
    driver.find_element_by_id(usernameId).send_keys(username)
    driver.find_element_by_id(passwordId).send_keys(password)
    driver.find_element_by_name(submit_buttonId).click()


login('https://www.webassign.net/wa-auth/login',
      'email', myWA_email, 'cengagePassword', myWA_password, 'Login')

time.sleep(10)
driver.find_element_by_partial_link_text('Grades').click()
