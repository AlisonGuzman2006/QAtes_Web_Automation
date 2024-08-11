from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By


@when('I create a new filter "{filter_name}"')
def step_impl(context, filter_name):
    context.component_pages.click_button_by_css(context.filters_page.NEW_FILTER_BUTTON_SELECTOR)
    context.component_pages.click_button_by_css(context.filters_page.TRY_IT_BUTTON_SELECTOR)
    context.component_pages.click_button_by_css(context.filters_page.FILTER_ASSIST_BUTTON_SELECTOR)
    context.component_pages.click_button_by_css(context.filters_page.SEND_BUTTON_SELECTOR)
    context.component_pages.click_button_by_css(context.filters_page.ADD_FILTER_BUTTON_SELECTOR)



@when('I added the filter to favorites')
def step_impl(context):
    # Agregar el filtro a favoritos
    context.driver.implicitly_wait(5)
    favorite_button = context.driver.find_element(By.XPATH, '//button[@aria-label="Add to favorites"]')
    favorite_button.click()


@then('I should see the filter in favorites section')
def step_impl(context):
    # Verificar que el filtro aparezca en la sección de favoritos
    favorites_section = context.driver.find_element(By.XPATH, '//span[text()="Favorites"]/..')
    assert context.driver.find_element(By.XPATH, f'//span[text()="{context.new_filter}"]') in favorites_section.text, \
        f'El filtro "{context.new_filter}" no fue encontrado en la sección de favoritos.'
    context.driver.quit()
