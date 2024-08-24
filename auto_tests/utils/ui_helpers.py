from selenium.webdriver.common.by import By


def login(browser, username, password):
    browser.get("https://demowebshop.tricentis.com/")
    browser.find_element_by_name("username").send_keys(username)
    browser.find_element_by_name("password").send_keys(password)
    browser.find_element_by_name("submit").click()


def register(browser, first_name, last_name, email, password):
    browser.get("https://demowebshop.tricentis.com/")

    browser.find_element(By.XPATH, "//a[@class='ico-register']").click()
    browser.find_element(By.XPATH, "//h1[contains(text(),'Register')]").is_displayed()

    browser.find_element(By.XPATH, "//input[@value='M']").click()
    browser.find_element(By.XPATH, "//input[@id='FirstName']").send_keys(first_name)
    browser.find_element(By.XPATH, "//input[@id='LastName']").send_keys(last_name)
    browser.find_element(By.XPATH, "//input[@id='Email']").send_keys(email)
    browser.find_element(By.XPATH, "//input[@id='Password']").send_keys(password)
    browser.find_element(By.XPATH, "//input[@id='ConfirmPassword']").send_keys(password)
    browser.find_element(By.XPATH, "//input[@id='register-button']").click()
