from behave import *


@given("I am on Homepage")
def step_impl(context):
    context.homepage.go_home()


@when('I click "{page_link_text}" link')
def step_impl(context, page_link_text):
    context.homepage.go_to(page_link_text)


@then("I am redirected to Form Page")
def step_impl(context):
    assert context.browser.get_current_url() == context.form_page.URL

@then("I am redirected to switch-window Page")
def step_impl(context):
    assert context.browser.get_current_url() == context.switch_window.URL