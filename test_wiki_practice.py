import os

from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest


@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome(executable_path="D:\\NeoTest\\chromedriver.exe")
    driver.get("https://en.wikipedia.org/wiki/India")
    return driver

class Test_Wiki_Main_Menu():

    def test_wiki_geo(self,browser):
        browser.find_element(By.XPATH,"//li[@id='toc-Geography']//div[1]").click()
        browser.find_element(By.XPATH,"//input[@id='vector-main-menu-dropdown-checkbox']").click()
        assert browser.current_url == "https://en.wikipedia.org/wiki/India#Geography"

    def test_wiki_main_page(self,browser):
        browser.find_element(By.XPATH, "//input[@id='vector-main-menu-dropdown-checkbox']").click()
        browser.find_element(By.XPATH,"//span[normalize-space()='Main page']").click()
        assert browser.current_url == "https://en.wikipedia.org/wiki/Main_Page"

    def test_wiki_content(self,browser):
        browser.find_element(By.XPATH, "//input[@id='vector-main-menu-dropdown-checkbox']").click()
        browser.find_element(By.XPATH,"//span[normalize-space()='Contents']").click()
        assert browser.current_url == "https://en.wikipedia.org/wiki/Wikipedia:Contents"

    def test_wiki_current_event(self,browser):
        browser.find_element(By.XPATH, "//input[@id='vector-main-menu-dropdown-checkbox']").click()
        browser.find_element(By.XPATH,"//span[normalize-space()='Current events']").click()
        assert browser.current_url == "https://en.wikipedia.org/wiki/Portal:Current_events"

    def test_wiki_donate(self,browser):
        browser.find_element(By.XPATH, "//input[@id='vector-main-menu-dropdown-checkbox']").click()
        browser.find_element(By.XPATH,"//span[normalize-space()='Donate']").click()
        assert browser.current_url == "https://donate.wikimedia.org/w/index.php?title=Special:LandingPage&country=IN&uselang=en&utm_medium=sidebar&utm_source=donate&utm_campaign=C13_en.wikipedia.org"

    def test_wiki_about_wiki(self,browser):
        browser.find_element(By.XPATH, "//input[@id='vector-main-menu-dropdown-checkbox']").click()
        browser.find_element(By.XPATH,"//span[normalize-space()='About Wikipedia']").click()
        assert browser.current_url == "https://en.wikipedia.org/wiki/Wikipedia:About"

    def test_wiki_note(self,browser):
        browser.find_element(By.XPATH,"//a[@href='#Notes']//div[@class='vector-toc-text']").click()
        assert browser.current_url == "https://en.wikipedia.org/wiki/India#Not"

