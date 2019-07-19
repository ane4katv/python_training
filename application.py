from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Application:

    def __init__(self):
        self.wd = webdriver.Chrome(executable_path='/Users/atvelova/Documents/python_training/chromedriver')
        self.wd.implicitly_wait(60)

    def open_page(self):
        wd = self.wd
        wd.get("http://hrm.seleniumminutes.com/symfony/web/index.php/auth/login")

    def login(self):
        wd = self.wd
        self.open_page()
        wd.find_element(By.ID, "txtUsername").click()
        wd.find_element(By.ID, "txtUsername").send_keys("admin")
        wd.find_element(By.ID, "txtPassword").send_keys("Password")
        wd.find_element(By.ID, "txtPassword").send_keys(Keys.ENTER)
        self.wd.implicitly_wait(60)

    def logout(self):
        wd = self.wd
        wd.find_element(By.ID, "welcome").click()
        self.wd.implicitly_wait(60)
        wd.find_element(By.LINK_TEXT, "Logout").click()

    def destroy(self):
        self.wd.quit()