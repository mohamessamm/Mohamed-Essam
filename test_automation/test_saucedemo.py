from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'http://www.saucedemo.com'
browser_str = "Chrome"
username_textbox_id = "user-name"
password_textbox_id = "password"
login_button_id = "login-button"
error_box_xpath = '//*[@id="login_button_container"]/div/form/div[contains(@class, "error-message-container")]/h3'

def setup():
    browser = webdriver.Chrome()
    browser.get(url)
    username_textbox = browser.find_element(By.ID, username_textbox_id)
    password_textbox = browser.find_element(By.ID, password_textbox_id)
    login_button = browser.find_element(By.ID, login_button_id)
    return browser, username_textbox, password_textbox, login_button

def teardown(browser):
    browser.close()

def test_page_info():
    browser, _, _, _ = setup()
    try:
        assert browser.current_url == 'https://www.saucedemo.com/'
        assert browser.title == "Sauce Demo"
    finally:
        teardown(browser)

def test_username_validation():
    browser, _, _, login_button = setup()
    try:
        login_button.click()
        error_box = browser.find_elements(By.XPATH, error_box_xpath)
        assert len(error_box) > 0
        assert 'Username is required' in error_box[0].text
    finally:
        teardown(browser)

def test_password_validation():
    browser, username_textbox, _, login_button = setup()
    try:
        username_textbox.send_keys("my username")
        login_button.click()
        error_box = browser.find_elements(By.XPATH, error_box_xpath)
        assert len(error_box) > 0
        assert 'Password is required' in error_box[0].text
    finally:
        teardown(browser)

def test_login_success():
    browser, username_textbox, password_textbox, login_button = setup()
    try:
        username_textbox.send_keys("standard_user")
        password_textbox.send_keys("secret_sauce")
        login_button.click()
        assert browser.current_url == "https://www.saucedemo.com/inventory.html"
    finally:
        teardown(browser)

def test_login_failure():
    browser, username_textbox, password_textbox, login_button = setup()
    try:
        username_textbox.send_keys("123456")
        password_textbox.send_keys("123456")
        login_button.click()
        error_box = browser.find_elements(By.XPATH, error_box_xpath)
        assert len(error_box) > 0
        assert 'Username and password do not match any user in this service' in error_box[0].text
    finally:
        teardown(browser)

def test_login_locked_user():
    browser, username_textbox, password_textbox, login_button = setup()
    try:
        username_textbox.send_keys("locked_out_user")
        password_textbox.send_keys("secret_sauce")
        login_button.click()
        error_box = browser.find_elements(By.XPATH, error_box_xpath)
        assert len(error_box) > 0
        assert 'Sorry, this user has been locked out.' in error_box[0].text
    finally:
        teardown(browser)
