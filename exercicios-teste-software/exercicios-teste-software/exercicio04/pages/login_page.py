from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    EMAIL_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "submit")
    
    def abrir(self):
        self.abrir_url("https://practicetestautomation.com/practice-test-login/")

    def preencher_email(self, email):
        self.digitar(self.EMAIL_INPUT, email)

    def preencher_senha(self, password):
        self.digitar(self.PASSWORD_INPUT, password)
    
    def clicar_login(self):
        self.clicar(self.LOGIN_BUTTON)

    def fazer_login(self, username, password):
        self.preencher_email(username)
        self.preencher_senha(password)
        self.clicar_login()
