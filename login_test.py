import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

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
        driver.get("https://www.saucedemo.com/")
        user = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")
        user.send_keys("standard_user")
        password.send_keys("secret_sauce")
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
        driver.get("https://www.saucedemo.com/")
        user = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")
        user.send_keys("standard_user")
        password.send_keys("1234")
        btn_login = driver.find_element(By.ID, "login-button")
        btn_login.click()

        self.assertTrue(driver.find_element(By.CLASS_NAME, "error-button"))
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()