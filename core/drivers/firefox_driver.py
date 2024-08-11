from selenium import webdriver
import json


"""
def get_firefox_driver():
    options = webdriver.FirefoxOptions()
    options.add_argument('--start-maximized')
    driver = webdriver.Firefox(options=options)
    return driver
"""
def get_firefox_driver():
    # Leer el archivo config.json
    with open('config.json', 'r') as f:
        config = json.load(f)

    # Obtener la configuración para Firefox
    firefox_config = config['browsers']['firefox']

    # Configurar las opciones de Firefox
    options = webdriver.FirefoxOptions()

    # Verificar si se debe iniciar en modo headless
    if firefox_config.get('headless', False):
        options.add_argument('--headless')
    
    # Verificar si se debe maximizar la ventana
    if firefox_config.get('maxWindows', False):
        options.add_argument('--start-maximized')
    else:
        # Configurar la resolución de la ventana si no se maximiza
        resolution = firefox_config['resolution']
        options.add_argument(f'--width={resolution["width"]}')
        options.add_argument(f'--height={resolution["height"]}')

    # Inicializar el WebDriver con las opciones configuradas
    driver = webdriver.Firefox(options=options)

    # Configurar el tiempo de espera implícito
    driver.implicitly_wait(firefox_config['timeout'])

    return driver

