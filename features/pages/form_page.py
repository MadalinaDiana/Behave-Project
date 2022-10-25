from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class FormPage(BasePage):

    URL = "https://formy-project.herokuapp.com/form"
    PAGE_TITLE = "Complete Web Form"

    def input_first_name(self, first_name):
        first_name_element = self.driver.find_element("first-name")
        first_name_element.send_keys(first_name)

    def click_submit(self):
        submit_button = self.driver.find_element(By.CLASS_NAME, "btn-primary")
        submit_button.click()
