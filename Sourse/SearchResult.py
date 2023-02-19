from selenium.webdriver.common.by import By
class WantedElementLocator():
    wantedElementLocator = (By.XPATH, "(//img[@class='s-image'])[1]")


class WantedElement():
    def __init__(self, driver):
        self.driver = driver

def wanted_element(self, product):
    firstElement = self.driver.find_element(*(self.firstElementLocator))
    firstElement.click()
    firstElement.send_keys(product)
