@echo off

REM Crear directorios si no existen
if not exist "tests\reports\allure\results" mkdir "tests\reports\allure\results"

REM Ejecutar pruebas en Chrome
set BROWSER=chrome
behave -f allure_behave.formatter:AllureFormatter -o tests/reports/allure/results

REM Ejecutar pruebas en Edge
set BROWSER=edge
behave -f allure_behave.formatter:AllureFormatter -o tests/reports/allure/results

REM Generar el reporte de Allure /*headless, etc de navegadores revisar
allure generate tests/reports/allure/results -o tests/reports/allure/report --clean
allure serve tests/reports/allure/report
