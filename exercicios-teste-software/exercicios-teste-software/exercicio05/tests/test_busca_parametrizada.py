import pytest
import time
from selenium.webdriver.common.by import By

# ---------- Parte C: Busca Parametrizada ----------

@pytest.mark.parametrize("termo_busca", [
    "Python",
    "Selenium",
    "Pytest",
    "API Testing",
    "Automation"
])
def test_busca_google(chrome_driver, termo_busca):
    driver = chrome_driver
    driver.get("https://www.google.com")

    # Aceitar cookies se aparecer (opcional)
    try:
        aceitar = driver.find_element(By.ID, "L2AGLb")
        aceitar.click()
        time.sleep(1)
    except:
        pass

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(termo_busca)
    search_box.submit()

    # Aguardar resultados carregarem
    time.sleep(2)

    assert termo_busca.lower() in driver.page_source.lower()
