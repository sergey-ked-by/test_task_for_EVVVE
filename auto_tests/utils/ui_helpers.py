from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


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


def login(browser, email, password):
    browser.get("https://demowebshop.tricentis.com/")
    browser.find_element(By.XPATH, "//a[@class='ico-login']").click()
    browser.find_element(By.XPATH, "//input[@id='Email']").send_keys(email)
    browser.find_element(By.XPATH, "//input[@id='Password']").send_keys(password)
    browser.find_element(By.XPATH, "//input[@value='Log in']").click()


def search_product(browser, product):
    browser.get("https://demowebshop.tricentis.com/")
    browser.find_element(By.XPATH, "//input[@id='small-searchterms']").send_keys(product)
    browser.find_element(By.XPATH, "//input[@value='Search']").click()


def add_product_to_cart(browser, product):
    browser.get("https://demowebshop.tricentis.com/")
    browser.find_element(By.XPATH, "//a[text()='" + product + "']/../following-sibling::div//input[@type='button']").click()
    browser.find_element(By.XPATH, "///li[@id='topcartlink']/a[@class='ico-cart']").click()


def checkout(browser, first_name, last_name, email, country, city, address, postal_code, phone):
    browser.find_element(By.XPATH, "//label[@id='BillingNewAddress_FirstName']").sendkeys(first_name)
    browser.find_element(By.XPATH, "//label[@id='BillingNewAddress_LastName']").sendkeys(last_name)
    browser.find_element(By.XPATH, "//label[@id='BillingNewAddress_Email']").sendkeys(email)
    Select(browser.find_element(By.XPATH, "//label[@id='BillingNewAddress_CountryId']")).select_by_visible_text(country)
    browser.find_element(By.XPATH, "//label[@id='BillingNewAddress_City']").sendkeys(city)
    browser.find_element(By.XPATH, "//label[@id='BillingNewAddress_Address1']").sendkeys(address)
    browser.find_element(By.XPATH, "//label[@id='BillingNewAddress_ZipPostalCode']").sendkeys(postal_code)
    browser.find_element(By.XPATH, "//label[@id='BillingNewAddress_PhoneNumber']").sendkeys(phone)
    browser.find_element(By.XPATH, "//input[@title='Continue']").click()
    browser.find_element(By.XPATH, "//input[@title='Continue']").click()
    browser.find_element(By.XPATH, "//input[@id='shippingoption_0']").click()
    browser.find_element(By.XPATH, "//input[@title='Continue']").click()
    browser.find_element(By.XPATH, "//input[@id='paymentmethod_0']").click()
    browser.find_element(By.XPATH, "//input[@title='Continue']").click()
    browser.find_element(By.XPATH, "//input[@title='Continue']").click()
    browser.find_element(By.XPATH, "//input[@value='Confirm']").click()
