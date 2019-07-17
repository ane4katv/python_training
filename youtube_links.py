from selenium import webdriver
from selenium.webdriver.common.by import By

class TestPaystop():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_paystop(self):
    self.driver.get("https://www.youtube.com/")
    self.driver.find_element(By.LINK_TEXT, "Trending").click()
    self.driver.find_element(By.LINK_TEXT, "Music").click()
    self.driver.find_element(By.LINK_TEXT, "Sports").click()


