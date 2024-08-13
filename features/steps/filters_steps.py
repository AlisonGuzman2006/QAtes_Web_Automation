import time

from behave import when, then
from selenium.webdriver.common.by import By


@when('I create a new filter')
def creation_new_filter(context):
    context.component_pages.click_button_by_css(context.filters_page.NEW_FILTER_BUTTON_SELECTOR)
    context.component_pages.click_button_by_css(context.filters_page.TRY_IT_BUTTON_SELECTOR)
    context.component_pages.click_button_by_css(context.filters_page.FILTER_ASSIST_BUTTON_SELECTOR)
    context.component_pages.click_button_by_css(context.filters_page.SEND_BUTTON_SELECTOR)
    context.component_pages.click_button_by_css(context.filters_page.ADD_FILTER_BUTTON_SELECTOR)


@when('I added the filter to favorites')
def filter_added_favorites(context):
    context.component_pages.click_button_by_css(context.filters_page.OPTIONS_MENU_SELECTOR)
    context.component_pages.click_button_by_css(context.filters_page.ADD_FAVORITES_SELECTOR)


@then('I should see the text "{remove_from_favorites}" inside the filter menu')
def remove_favorite_text(context, remove_from_favorites):
    context.component_pages.click_button_by_css(context.filters_page.OPTIONS_MENU_SELECTOR)
    text = context.component_pages.get_text_by_css_selector(context.filters_page.REMOVE_FAVORITES_SELECTOR)
    assert text == remove_from_favorites, "Wrong text"


@when('I delete the filter "{filter_name}"')
def step_impl(context, filter_name):
    filters = context.component_pages.get_elements_by_css(context.filters_page.FILTER_OPTION_SELECTOR)
    target_filter = None
    for filter in filters:
        filter_text = filter.find_element(By.CLASS_NAME, context.filters_page.FILTER_TEXT_SELECTOR)
        if filter_name in filter_text.text:
            target_filter = filter
            break
    target_filter.click()
    context.component_pages.click_button_by_css(context.filters_page.MORE_OPTIONS_FILTER_SELECTOR)
    context.component_pages.click_button_by_css(context.filters_page.DELETE_FILTER_BUTTON_SELECTOR)
    time.sleep(3)
    context.component_pages.click_button_by_css(context.filters_page.CONFIRM_DELETE_BUTTON_SELECTOR)


@then('I should see the text "{empty_filters}"')
def step_impl(context, empty_filters):
    text = context.component_pages.get_text_by_css_selector(context.filters_page.EMPTY_FILTERS_SELECTOR)
    assert text == empty_filters, "Wrong text"
