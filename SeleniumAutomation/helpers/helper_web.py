from selenium import webdriver
from SeleniumAutomation.helpers.helper_base import HelperFunc


def get_browser(browser) -> object:
    if browser == "chrome":
        dripath = "SeleniumAutomation\\Base\\Driver\\chromedriver.exe"
        return HelperFunc(webdriver.Chrome(executable_path=dripath))
