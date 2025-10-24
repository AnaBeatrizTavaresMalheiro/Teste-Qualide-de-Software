from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from pages.dahsboard_page import DashboardPage

CHROMEDRIVER_PATH = r"C:/Users/GUILHERME MALHEIRO/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"

def iniciar_driver():
    options = Options()
    # options.add_argument("--headless")  # Descomente se quiser rodar sem abrir o navegador
    driver = webdriver.Chrome(service=Service(CHROMEDRIVER_PATH), options=options)
    driver.maximize_window()
    return driver

def test_login_credenciais_valida():
    driver = iniciar_driver()
    login = LoginPage(driver)
    login.abrir()
    login.fazer_login("student", "Password123")
    assert "Logged In Successfully" in driver.page_source
    print("Login efetuado com sucesso!")
    driver.quit()

def test_login_email_invalido():
    driver = iniciar_driver()
    login = LoginPage(driver)
    login.abrir()
    login.fazer_login("teacher", "Password123")
    assert "Your username is invalid!" in driver.page_source
    print("Usuário informado inválido!")
    driver.quit()

def test_login_senha_incorreta():
    driver = iniciar_driver()
    login = LoginPage(driver)
    login.abrir()
    login.fazer_login("student", "test123")
    assert "Your password is invalid!" in driver.page_source
    print("Senha informada inválida")
    driver.quit()

def test_login_sem_preencher_campos():
    driver = iniciar_driver()
    login = LoginPage(driver)
    login.abrir()
    login.fazer_login("", "")
    assert "Your username is invalid!" in driver.page_source
    print("Usuário informado inválido!")
    driver.quit()

def test_login_verificar_mensagens_erro_apropriadas():
    driver = iniciar_driver()
    login = LoginPage(driver)

    # Login válido
    login.abrir()
    login.fazer_login("student", "Password123")
    assert "Logged In Successfully" in driver.page_source
    print("Login efetuado com sucesso!")

    # Email inválido
    login.abrir()
    login.fazer_login("teacher", "Password123")
    assert "Your username is invalid!" in driver.page_source
    print("Usuário informado inválido!")

    # Senha incorreta
    login.abrir()
    login.fazer_login("student", "test123")
    assert "Your password is invalid!" in driver.page_source
    print("Senha informada inválida")

    # Campos vazios
    login.abrir()
    login.fazer_login("", "")
    assert "Your username is invalid!" in driver.page_source
    print("Usuário informado inválido!")

    driver.quit()
