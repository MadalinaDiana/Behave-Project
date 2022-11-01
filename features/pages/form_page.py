import time

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


class FormPage(BasePage):

    URL = "https://formy-project.herokuapp.com/form"
    PAGE_TITLE = "Complete Web Form"

    def input_first_name(self, first_name):
        first_name_element = self.driver.find_element(By.ID, "first-name")
        first_name_element.send_keys(first_name)

    def clean_first_name(self):
        first_name_element = self.driver.find_element(By.ID, "first-name")
        first_name_element.send_keys(Keys.CONTROL + "a")
        first_name_element.send_keys(Keys.BACKSPACE)

    def click_submit(self):
        submit_button = self.driver.find_element(By.CLASS_NAME, "btn-primary")
        submit_button.click()

    def click_components_menu(self):
        ac = ActionChains(self.driver)
        components_submenu = self.driver.find_element(By.ID, "navbarDropdownMenuLink")
        ac.move_to_element(components_submenu).click().perform()
        time.sleep(3)
