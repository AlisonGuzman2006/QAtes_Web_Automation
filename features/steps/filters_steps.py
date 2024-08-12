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
