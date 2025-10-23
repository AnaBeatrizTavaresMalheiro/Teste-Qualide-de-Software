def test_login_sucesso(chrome_driver):
    driver = chrome_driver
    driver.get("https://practicetestautomation.com/practice-test-login/")
    
    # Preencher formulário
    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()
    
    # Verificar sucesso
    assert "Logged In Successfully" in driver.page_source

def test_login_erro_email(chrome_driver):
    driver = chrome_driver
    driver.get("https://practicetestautomation.com/practice-test-login/")
    
    # Preencher formulário
    driver.find_element(By.ID, "username").send_keys("")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()
    
    # Verificar erro
    assert "Your username is invalid!" in driver.page_source


def test_login_erro_senha(chrome_driver):
    driver = chrome_driver
    driver.get("https://practicetestautomation.com/practice-test-login/")
    
    # Preencher formulário
    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("")
    driver.find_element(By.ID, "submit").click()
    
    # Verificar erro
    assert "Your password is invalid!" in driver.page_source


def test_login_erro_vazio(chrome_driver):
    driver = chrome_driver
    driver.get("https://practicetestautomation.com/practice-test-login/")
    
    # Preencher formulário
    driver.find_element(By.ID, "username").send_keys("")
    driver.find_element(By.ID, "password").send_keys("")
    driver.find_element(By.ID, "submit").click()
    
    # Verificar erro
    assert "Your username is invalid!" in driver.page_source


