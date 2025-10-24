from selenium.webdriver.common.by import By
from .base_page import BasePage

class DashboardPage(BasePage):
    SUCCESS_MESSAGE = (By.CLASS_NAME, "post-title")

    def esta_logado(self):
        return "/logged-in-successfully/" in self.driver.current_url

    def obter_mensagem_boas_vindas(self):
        return self.obter_texto(self.SUCCESS_MESSAGE)
