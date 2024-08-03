import subprocess

def run_tests():
    # Ejecutar las pruebas de Behave con el formato de Allure
    subprocess.run(["behave", "-f", "allure_behave.formatter:AllureFormatter", "-o", "reports/allure"])

    # Generar el reporte de Allure (opcional, si tienes Allure CLI instalado)
    subprocess.run(["allure", "serve", "reports/allure"])

if __name__ == "__main__":
    run_tests()
