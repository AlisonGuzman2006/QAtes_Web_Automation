import subprocess

from behave.__main__ import main as behave_main

if __name__ == "__main__":
    behave_main()
    #subprocess.run(["allure", "generate", "allure-results", "--clean", "-o", "allure-report"])
