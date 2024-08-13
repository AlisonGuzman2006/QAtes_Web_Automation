from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class ProjectPage:
    #Dashboard Project
    PROJECT_DASHBOARD_URL = "https://app.todoist.com/app/200206/projects/active"
    PROJECT_DASHBOARD_SELECTOR = 'div[role="navigation"]>div>div:nth-child(2)>div>div>div>a'
    VIEW_OPTION_PROJECT_SELECTOR = 'button[aria-label="Project options menu"]'
    ADD_ELEMENT_BUTTON_SELECTOR = 'main[id="content"]>div>div>div>div>div>div:nth-child(2)>div:nth-child(2)'
    ADD_PROJECT_BUTTON_SELECTOR = 'div[aria-label="Add project"] > div'
    NAME_PROJECT_SELECTOR = 'edit_project_modal_field_name'
    CREATE_PROJECT_BUTTON_SELECTOR = 'div[role="dialog"] > form > footer > div > button:nth-child(2)'
    PROJECT_DASHBOARD_SELECTOR_2 = 'div[class="project_view project_editor_instance current_editor"]>header>div>div>a:nth-child(1)'
    DUPLICATE_PROJECT_OPTION_SELECTOR = 'div[role="menuitem"]:nth-child(4)'

    ADD_FOLDER_BUTTON_SELECTOR = 'div[aria-label="Add folder"] > div'
    NAME_FOLDER_SELECTOR = 'input[name="name"]'
    SELECT_PROJECT_SELECTOR = 'button[aria-label="Select projects"]'
    SELECT_CHECK_PROJECT_SELECTOR = 'ul[id="dropdown-select-44-listbox"]>li:nth-child(1)'
    CREATE_FOLDER_BUTTON_SELECTOR = 'div[role="dialog"] > form > footer > div > button:nth-child(2)'
    OPTION_ORGANIZE_INTO_THE_FOLDER_SELECTOR = 'div[class="reactist_menubutton"]'
    CREATE_FOLDER_OPTION_SELECTOR = 'div[data-active-item="true"]:nth-child(1)'


    #Refrescar la ventana o navegar por el nav var
    PROJECT_NAMES_SELECTOR = 'div[style="min-height: 60px;"] > div>li>div>a>div:nth-child(2)>div>div'
    CREATE_FOLDER_SUCCESFULY_SELECTOR = 'div[role="alert"]>div>div'

    #Buscar el proyecto duplicado con el nombre de: Copia de 'nombre del prol proyecto creado anteriormente'


    def __init__(self, driver):
        self.driver = driver

    def get_list_of_projects(self):
        projects_elements = self.driver.find_elements(By.CSS_SELECTOR, self.PROJECT_NAMES_SELECTOR)
        return [project.text for project in projects_elements]

    def is_folder_created_message_present(self, folder_name):
        message_selector = self.CREATE_FOLDER_SUCCESFULY_SELECTOR.format(folder_name=folder_name)
        try:
            message_element = self.driver.find_element(By.CSS_SELECTOR, message_selector)
            return folder_name in message_element.text
        except:
            return False