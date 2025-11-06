from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def reset_app_state(self):
        self.driver.find_element(By.ID, "react-burger-menu-btn").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "reset_sidebar_link").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "react-burger-cross-btn").click()

    def add_items_to_cart(self, item_names):
        for name in item_names:
            self.driver.find_element(By.XPATH, f"//div[text()='{name}']/../../button").click()

    def filter_products(self, filter_option="Name (Z to A)"):
        select = Select(self.driver.find_element(By.CLASS_NAME, "product_sort_container"))
        select.select_by_visible_text(filter_option)

    def add_first_product_to_cart(self):
        first_add_btn = self.driver.find_element(By.XPATH, "(//button[text()='Add to cart'])[1]")
        first_add_btn.click()

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    def logout(self):
        self.driver.find_element(By.ID, "react-burger-menu-btn").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "logout_sidebar_link").click()
