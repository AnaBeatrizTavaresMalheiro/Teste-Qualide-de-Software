import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

CHROMEDRIVER_PATH = r"C:/Users/GUILHERME MALHEIRO/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"

def test_login_credenciais_valida():
    options = Options()
    driver = webdriver.Chrome(service=Service(CHROMEDRIVER_PATH), options=options)
    try:
        driver.get("https://practicetestautomation.com/practice-test-login/")
        driver.find_element(By.ID, "username").send_keys("student")
        driver.find_element(By.ID, "password").send_keys("Password123")
        driver.find_element(By.ID, "submit").click()
        assert "Logged In Successfully" in driver.page_source
        print("Login Efetuado com sucesso!")
    finally:
        driver.quit()

def test_login_email_invalido():
    options = Options()
    driver = webdriver.Chrome(service=Service(CHROMEDRIVER_PATH), options=options)
    try:
        driver.get("https://practicetestautomation.com/practice-test-login/")
        driver.find_element(By.ID, "username").send_keys("teacher")
        driver.find_element(By.ID, "password").send_keys("Password123")
        driver.find_element(By.ID, "submit").click()
        assert "Your username is invalid!" in driver.page_source
        print("Usuário informado inválido!")
    finally:
        driver.quit()

def test_login_senha_incorreta():
    options = Options()
    driver = webdriver.Chrome(service=Service(CHROMEDRIVER_PATH), options=options)
    try:
        driver.get("https://practicetestautomation.com/practice-test-login/")
        driver.find_element(By.ID, "username").send_keys("student")
        driver.find_element(By.ID, "password").send_keys("teste123")
        driver.find_element(By.ID, "submit").click()
        assert "Your password is invalid!" in driver.page_source
        print("Senha informada inválida")
    finally:
        driver.quit()

def test_login_sem_preencher_campos():
    options = Options()
    driver = webdriver.Chrome(service=Service(CHROMEDRIVER_PATH), options=options)
    try:
        driver.get("https://practicetestautomation.com/practice-test-login/")
        driver.find_element(By.ID, "submit").click()
        assert "Your username is invalid!" in driver.page_source
        print("Usuário informado inválido!")
    finally:
        driver.quit()
