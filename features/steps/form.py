from behave import *


@Given("I am on the Form page")
def step_impl(context):
    context.form_page.go_home()


@When("I fill out the form correctly")
def step_impl(context):
    context.form_page.input_first_name("Adela")
    # aici as mai apela metode de completare a formului
    context.form_page.clean_first_name()
    context.form_page.click_components_menu()


@When("I click Submit")
def step_impl(context):
    context.form_page.click_submit()


@Then("I am redirected to the Thanks page")
def step_impl(context):
    # Expected URL = cel al paginii de Thank you
    expected_url = context.thanks_page.URL
    context.browser.check_url(expected_url)
    # assert context.browser.get_current_url() == context.thanks_page.URL


@Then("I get a success message")
def step_impl(context):
    assert context.thanks_page.get_message_text() == "The form was successfully submitted!"
