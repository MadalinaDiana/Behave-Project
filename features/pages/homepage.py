from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):

    URL = "https://formy-project.herokuapp.com"

    def go_to(self, url_text):
        element = self.driver.find_element(By.LINK_TEXT, url_text)
        element.click()
