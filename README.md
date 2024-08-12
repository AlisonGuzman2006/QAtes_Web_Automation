# Todoist Web Automation
## Team: Qates
Este repositorio contiene pruebas automatizadas para la aplicación web Todoist. Utiliza Behave como herramienta de pruebas con formato Gherkin y Selenium como suite de herramientas de automatización, y Python como lenguaje de programación.
## Instalación
### Requisitos Previos
- Python [download link](https://www.python.org/downloads/)
- Allure [download link](https://allurereport.org/docs/install/)
- Chrome drive [download link](https://googlechromelabs.github.io/chrome-for-testing/#stable)
- Selenium 
### Setup e instalación de dependencias
1. Clonar el repositorio y navegar al directorio del proyecto:
```bash
git clone https://github.com/AlisonGuzman2006/QAtes_Web_Automation.git
cd QAtes_Web_Automation
```
2. Crear un entorno virtual e instalar las dependencias:


```bash
python -m venv venv
source venv/bin/activate 
pip install -r requirements.txt
 ```
3. Para ejecutar los test usar el siguiente comando (Si desa usar otro navegador cambiar la opcion browser):
```bash
behave --define browser=chrome
 ``` 
## Ejecución en paralelo
 1. Para ejecutar el proyecto en paralelo se debe correr el siguiente comando
 ```bash
python .\tests\parallel_runner.py
```
2. Para cambiar el número de navegadores, cambiar la variable `MAX_CONCURRENT_BROWSERS` que se encuentra en el archivo parallel_runner.py
