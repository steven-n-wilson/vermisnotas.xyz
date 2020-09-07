from selenium import webdriver
import yaml

conf = yaml.load(open('website_login\loginDetails.yml'),
                 Loader=yaml.FullLoader)
myWA_email = conf['webAssign_user']['email']
myWA_password = conf['webAssign_user']['cengagePassword']


driver = webdriver.Chrome()


def login(url, usernameId, username, passwordId, password, submit_buttonId):
    driver.get(url)
    driver.find_element_by_id(usernameId).send_keys(username)
    driver.find_element_by_id(passwordId).send_keys(password)
    # driver.find_element_by_id(submit_buttonId).click()
    driver.find_element_by_name(submit_buttonId).click()


login('https://www.webassign.net/wa-auth/login',
      'email', myWA_email, 'cengagePassword', myWA_password, 'Login')
