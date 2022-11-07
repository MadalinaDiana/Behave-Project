from browser import Browser
from pages.homepage import HomePage
from pages.form_page import FormPage
from pages.thanks_page import ThanksPage
from pages.switch_window import SwitchWindow


def before_all(context):
    context.browser = Browser()
    context.homepage = HomePage(context.browser.driver)
    context.form_page = FormPage(context.browser.driver)
    context.thanks_page = ThanksPage(context.browser.driver)
    context.switch_window = SwitchWindow(context.browser.driver)


def after_all(context):
    context.browser.close()
