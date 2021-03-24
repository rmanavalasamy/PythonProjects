from behave import *
from selenium.webdriver.common.keys import Keys
from SeleniumAutomation.PageObjects.SearchObj import search_obj
from SeleniumAutomation.Pages.SearchPage import search_page


@given("Open Google Search Page")
def step_impl(context):
    context.helperfunc.open(search_page.google_url)


@given("Open Yahoo Search Page")
def step_impl(context):
    context.helperfunc.open(search_page.yahoo_url)


@when("I do search")
def step_impl(context):
    context.helperfunc.find_by_xpath(search_obj.search_box).send_keys("Automation")
    context.helperfunc.find_by_xpath(search_obj.search_box).send_keys(Keys.RETURN)


@step("I click Result")
def step_impl(context):
    context.helperfunc.find_by_xpath(search_obj.search_result).click()
