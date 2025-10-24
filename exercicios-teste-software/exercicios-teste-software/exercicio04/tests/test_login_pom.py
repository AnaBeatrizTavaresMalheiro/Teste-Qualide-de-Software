import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from pages.dahsboard_page import DashboardPage

CHROMEDRIVER_PATH = r"C:/Users/GUILHERME MALHEIRO/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"

@pytest.fixture
def chrome_driver():
    options = Options()
    driver = webdriver.Chrome(service=Service(CHROMEDRIVER_PATH), options=options)
    yield driver
    driver.quit()

def test_login_credenciais_valida(chrome_driver):
    login = LoginPage(chrome_driver)
    login.abrir()
    login.fazer_login("student", "Password123")

    dash = DashboardPage(chrome_driver)
    assert dash.esta_logado()
    print("Login efetuado com sucesso!")

def test_login_email_invalido(chrome_driver):
    login = LoginPage(chrome_driver)
    login.abrir()
    login.fazer_login("teacher", "Password123")

    assert "Your username is invalid!" in chrome_driver.page_source
    print("Usuário informado inválido!")

def test_login_senha_incorreta(chrome_driver):
    login = LoginPage(chrome_driver)
    login.abrir()
    login.fazer_login("student", "test123")

    assert "Your password is invalid!" in chrome_driver.page_source
    print("Senha informada inválida")

def test_login_sem_preencher_campos(chrome_driver):
    login = LoginPage(chrome_driver)
    login.abrir()
    login.fazer_login("", "")

    assert "Your username is invalid!" in chrome_driver.page_source
    print("Usuário informado inválido!")

def test_login_verificar_mensagens_erro_apropriadas(chrome_driver):
    login = LoginPage(chrome_driver)
    login.abrir()
    login.fazer_login("student", "Password123")
    assert "Logged In Successfully" in chrome_driver.page_source

    login.abrir()
    login.fazer_login("teacher", "Password123")
    assert "Your username is invalid!" in chrome_driver.page_source

    login.abrir()
    login.fazer_login("student", "test123")
    assert "Your password is invalid!" in chrome_driver.page_source

    login.abrir()
    login.fazer_login("", "")
    assert "Your username is invalid!" in chrome_driver.page_source
