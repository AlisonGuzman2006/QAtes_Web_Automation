import subprocess

def run_tests():
    # Ejecutar las pruebas de Behave con el formato de Allure
    subprocess.run(["behave", "-f", "allure_behave.formatter:AllureFormatter", "-o", "tests/reports/allure/results"])

    # Generar el reporte de Allure
    subprocess.run(["allure", "serve", "tests/reports/allure/results"])

if __name__ == "__main__":
    run_tests()
