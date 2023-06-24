import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class ShoppingCart(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def login(self, driver):
        """
        Función que nos permite loguearnos y reutilizarse en las diferentes tests.
        """
        driver.get("https://www.saucedemo.com/")
        user = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")
        user.send_keys("standard_user")
        password.send_keys("secret_sauce")
        btn_login = driver.find_element(By.ID, "login-button")
        btn_login.click()
    
    def add_element(self, driver, id_btn_product):
        """
        Agregamos una función que nos permite agregar elementos al carrito de compras.
        """
        btn_add_to_cart = driver.find_element(By.ID, id_btn_product)
        btn_add_to_cart.click()


    def test_add_element_to_cart(self):
        """
        Probaremos agregar un elemento al carrito de compras.

        Condición de éxito:
        - Deberá aparecer el botón "Remove"
        - Deberá aparecer el valor 1 en el carrito de compras
        """
        driver = self.driver
        exist = False
        self.login(driver)
        self.add_element(driver, "add-to-cart-sauce-labs-backpack")
        btn_remove = driver.find_element(By.ID, "remove-sauce-labs-backpack")
        counter = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge')
        if "1" in counter.text and btn_remove:
            exist = True
        self.assertTrue(exist)

    def tearDown(self):
        self.driver.close()
    
    

if __name__ == "__main__":
    unittest.main()