from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


def configure_chrome_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    # options.add_argument('--headless')

    # driver = webdriver.Chrome(
    #     executable_path="/usr/local/bin/chromedriver.exe", options=options)
    driver = webdriver.Chrome(options=options)

    return driver
