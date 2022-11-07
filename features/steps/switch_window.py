import time

from behave import *


@given("I am on the switch-window page")
def step_impl(context):
    context.switch_window.go_home()


@when('I click on the open "{button}"')
def step_impl(context, button):
    context.switch_window.click_open_alert(button)
    time.sleep(3)


@then('I get the "{text}" is displayed')
def step_impl(context, text):
    assert context.switch_window.message_display()[1] == text


@then(u'I get the "This is a test alert!" is not displayed')
def step_impl(context):
    assert context.switch_window.message_display()[0] == False #error here