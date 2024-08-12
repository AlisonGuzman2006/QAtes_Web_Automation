from selenium import webdriver
import json

from core.drivers.options import set_options


"""
def get_chrome_driver():
    options = webdriver.ChromeOptions()
    set_options(options)
    driver = webdriver.Chrome(options=options)
    return driver
"""

def get_chrome_driver():
    # Leer el archivo config.json
    with open('config.json', 'r') as f:
        config = json.load(f)

    # Obtener la configuración para Chrome
    chrome_config = config['browsers']['chrome']

    # Configurar las opciones de Chrome
    options = webdriver.ChromeOptions()

    # Verificar si se debe iniciar en modo headless
    if chrome_config.get('headless', False):
        options.add_argument('--headless')

    # Verificar si se debe maximizar la ventana
    if chrome_config.get('maxWindows', False):
        options.add_argument('--start-maximized')
    else:
        # Configurar la resolución de la ventana si no se maximiza
        resolution = chrome_config['resolution']
        options.add_argument(f'--window-size={resolution["width"]},{resolution["height"]}')

    # Inicializar el WebDriver con las opciones configuradas
    driver = webdriver.Chrome(options=options)

    # Configurar el tiempo de espera implícito
    driver.implicitly_wait(chrome_config['timeout'])

    return driver
