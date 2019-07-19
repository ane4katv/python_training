import unittest
import pytest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

class TestPaystop():
    def setup_method(self):
        #self.driver = webdriver.Firefox(executable_path='/Users/atvelova/Documents/python_training/geckodriver')
        self.driver = webdriver.Chrome(executable_path='/Users/atvelova/Documents/python_training/chromedriver')
        self.vars = {}

    def teardown_method(self):
        self.driver.quit()

    def test_paystop(self):
        self.driver.get("https://www.youtube.com/")
        self.driver.find_element(By.LINK_TEXT, "Trending").click()
        self.driver.find_element(By.LINK_TEXT, "Music").click()
        self.driver.find_element(By.LINK_TEXT, "Sports").click()

        sleep(4)

        # link = self.driver.find_element_by_link_text("Sports")
        #
        # self.assertTrue("Sports", link)

if __name__=='__main__':
    pytest.main()
