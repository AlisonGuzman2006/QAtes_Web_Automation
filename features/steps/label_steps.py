import time

from behave import given, when, then
from main.ui.component_pages import ComponentPages
from main.ui.filters_page import Filters
from main.ui.label_page import Label


@given('I want to go to the filters and labels page')
def want_to_go_to_filters_page(context):
    context.component_pages = ComponentPages(context.driver)
    context.label = Label(context.driver)
    context.filters_page = Filters(context.driver)


@given('I am on the Filters and labels page')
def step_go_filters_and_labels(context):
    time.sleep(3)
    context.component_pages.click_button_by_css(context.label.FILTERS_AND_LABEL_SELECTOR)


@when('I create a new label {label_name}')
def step_click_new_label(context, label_name):
    context.component_pages.click_button_by_css(context.label.NEW_LABEL_BUTTON_SELECTOR)
    context.component_pages.search_and_fill_by_id(context.label.LABEL_NAME_FIELD_SELECTOR, label_name)
    context.component_pages.click_button_by_css(context.label.ADD_LABEL_BUTTON_SELECTOR)


@when('I create a new task {task_name}')
def step_creation_new_task(context, task_name):
    context.component_pages.click_button_by_css(context.label.ADD_NEW_TASK_BUTTON_SELECTOR)
    time.sleep(3)
    context.component_pages.search_and_fill_by_css(context.label.NAME_TASK_FIELD_SELECTOR, task_name)
    context.component_pages.click_button_by_css(context.label.ADD_TASK_BUTTON_SELECTOR)


@then('I should see the task {task_name} created with the label assigned in the filtered results')
def step_impl(context, task_name):
    text = context.component_pages.get_text_by_class(context.label.TASK_TITTLE_SELECTOR)
    assert text == task_name, "Wrong text"


@when('I click on the delete option of the "{label_name}" label')
def step_creation_new_task(context, label_name):
    labels = context.component_pages.get_elements_by_class(context.label.LABELS_SELECTOR)
    target_label = None
    for label in labels:
        if label_name in label.text:
            target_label = label
            break
    target_label.click()
    context.component_pages.click_button_by_css(context.label.LABEL_MENU_SELECTOR)
    context.component_pages.click_button_by_css(context.label.LABEL_DELETE_BUTTON_SELECTOR)
    time.sleep(3)
    context.component_pages.click_button_by_css(context.label.DELETE_BUTTON_SELECTOR)


@then('I should not see the "{label_name}" label')
def step_creation_new_task(context, label_name):
    labels = context.component_pages.get_elements_by_class(context.label.LABELS_SELECTOR)
    target_label = None
    for label in labels:
        if label_name in label.text:
            target_label = label
            break
    assert target_label is None, f"Target label is not equal to none, it is {label_name}"
