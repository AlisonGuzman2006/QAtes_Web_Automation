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
si no funciona usar estos comandos 
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\activate
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
## Reportes
### Requisitos previos
1. JAVA https://www.oracle.com/java/technologies/downloads/#jdk22-windows
2. Allure https://github.com/allure-framework/allure2/releases/tag/2.30.0

### Configuración
1. Instalación dependencias 
```bash
pip install allure-behave
pip install allure-python-commons
 ``` 
2. Ejecución de pruebas con behave para guardar en results
```bash
behave -f allure_behave.formatter:AllureFormatter -o reports/allure-results ./features

 ``` 
3. Generar el reporte
```bash
allure generate reports/allure-results -o reports/allure-report --clean

 ``` 
4. Visualizar el reporte
```bash
allure open reports/allure-report
``` 


