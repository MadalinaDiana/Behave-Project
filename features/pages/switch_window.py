from features.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common import NoAlertPresentException


class SwitchWindow(BasePage):
    URL = "https://formy-project.herokuapp.com/switch-window"

    def click_open_alert(self, value):
        btn = self.driver.find_element(By.ID, value)
        btn.click()

    def message_display(self):
        alert_message = self.driver.switch_to.alert

        try:
            displayed = alert_message.text
            print(displayed)
        except NoAlertPresentException:
            displayed = False

        if displayed:
            text = alert_message.text
            alert_message.accept()
        else:
            text = "alert does not Exist in page"
        return displayed, text
