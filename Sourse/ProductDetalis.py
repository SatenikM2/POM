from selenium.webdriver.common.by import By
class ProductPageLocator():
    ProductPageObj = (By.XPATH, "//input[@id='add-to-cart-button']")


class ProductPage(ProductPageLocator):
    def __init__(self, driver):
        self.driver = driver


    def add_product_to_card (self):
        ProductPageObj = self.driver.find_element(*(self.ProductPageLocator))
        ProductPageObj.click()

