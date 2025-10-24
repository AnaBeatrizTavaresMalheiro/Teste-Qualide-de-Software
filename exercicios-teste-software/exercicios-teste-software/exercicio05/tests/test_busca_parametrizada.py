import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CHROMEDRIVER_PATH = r"C:/Users/GUILHERME MALHEIRO/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"

@pytest.fixture
def chrome_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=options)
    yield driver
    driver.quit()

# ---------- Parte C: Busca Parametrizada (Bing) ----------

@pytest.mark.parametrize("termo_busca", [
    "Python",
    "Selenium",
    "Pytest",
    "API Testing",
    "Automation"
])
def test_busca_bing(chrome_driver, termo_busca):
    driver = chrome_driver
    driver.get("https://www.bing.com")

    # Localizar a barra de pesquisa
    search_box = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    search_box.clear()
    search_box.send_keys(termo_busca)
    search_box.submit()

    # Aguardar resultados carregarem
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "b_content"))
    )

    # Verificar se o termo de busca aparece na página
    assert termo_busca.lower() in driver.page_source.lower()
