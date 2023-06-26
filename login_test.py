import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.values = {
            "id_user": "user-name",
            "id_password" : "password",
            "id_btn_login" : "login-button",
            "url": "https://www.saucedemo.com/"
        }
    
    def find_elements(self, driver, test_values):
        driver.get(self.values["url"])
        user = driver.find_element(By.ID, self.values["id_user"])
        password = driver.find_element(By.ID, self.values["id_password"])
        user.send_keys(test_values["user"])
        password.send_keys(test_values["password"])

    def test_happy_login(self):
        """
        Probaremos que podemos iniciar sesión con
        usuario y contraseña correctas.
        Datos utilizados:
        - username: standard_user
        - pass: secret_sauce

        Condición de éxito: encontrar el botón "Add to car",
        cuyo id es "add-to-cart-sauce-labs-backpack"
        """
        driver = self.driver
        test_values = {
            "user": "standard_user",
            "password": "secret_sauce"
        }
        self.find_elements(driver, test_values)

        btn_login = driver.find_element(By.ID, "login-button")
        btn_login.click()
        self.assertTrue(driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack"))

    def test_wrong_password(self):
        """
        Probaremos que al utilizar una constraseña errónea,
        el sitio nos indicará que los datos ingresados no son
        correctos.
        Datos utilizados:
        - username: standard_user
        - password: 1234

        Condición de éxito: deberá aparecer un cartel rojo que nos indicará
        que los datos ingresados no son correctos cuyo class es "error-button".        
        """
        driver = self.driver
        test_values = {
            "user": "standard_user",
            "password": "1234"
        }
        self.find_elements(driver, test_values)

        btn_login = driver.find_element(By.ID, "login-button")
        btn_login.click()

        self.assertTrue(driver.find_element(By.CLASS_NAME, "error-button"))
    
    def test_locked_out_user(self):
        """
        Probaremos que al loguearnos con un usuario bloqueado, no podemos iniciar sesión.
        Datos utilizados:
        - username: locked_out_user
        - password: secret_sauce
        Condición de éxito: Encontrar el texto "Epic sadface: Sorry, this user has been locked out."
        """
        driver = self.driver
        test_values = {
            "user": "locked_out_user",
            "password": "secret_sauce"
        }
        self.find_elements(driver, test_values)

        btn_login = driver.find_element(By.ID, "login-button")
        btn_login.click()
        error_text = "Epic sadface: Sorry, this user has been locked out."
        self.assertTrue(driver.find_elements(By.XPATH, "//*[contains(text(), '{}')]".format(error_text)))

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()