from selenium.webdriver.common.by import By


class NavigationBarLocator():
    searchFieldElementLocator = (By.ID, "twotabsearchtextbox")

class NavigationBarPage(NavigationBarLocator):
    def __init__ (self, driver):
        self.driver = driver

    def fill_Saerch_field(self, text):
        searchFieldElement = self.driver.find_element(*(self.searchFieldElementLocator))
        searchFieldElement.clear()
        searchFieldElement.send_keys(text)


    def click_to_card_button(self):
        pass

    def click_to_search_button(self):
        pass

    def go_to_home_page(self):
        pass
