from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def abrir_url(self, url):
        self.driver.get(url)
    
    def encontrar_elemento(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def encontrar_elementos(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))
    
    def clicar(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
    
    def digitar(self, locator, texto):
        element = self.encontrar_elemento(locator)
        element.clear()
        element.send_keys(texto)
    
    def obter_texto(self, locator):
        element = self.encontrar_elemento(locator)
        return element.text
    
    def elemento_visivel(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False
