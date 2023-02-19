import time

from selenium import webdriver
import unittest
from Sourse.SignInPage import SignInPage
from Sourse.Navigation import NavigationBarPage
from Sourse.SearchResult import WantedElement
from Sourse.ProductDetalis import ProductPage




class MyTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        self.driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")
        self.signInPageObject = SignInPage(self.driver)
        self.navigationBarObj = NavigationBarPage(self.driver)
        self.wantedResultObj = WantedElement(self.driver)
        self.ProductPageObj = ProductPage(self.driver)


    def test_signIn(self):
        self.signInPageObject.fill_Login_Field("bobsmithamazon7@gmail.com")
        self.signInPageObject.click_to_continue_button()
        time.sleep(10)
        self.signInPageObject.fill_password_field("amazonpass")
        self.signInPageObject.click_to_sign_in_button()
        time.sleep(6)
        self.navigationBarObj.fill_Saerch_field("glasses")
        self.signInPageObject.click_to_sign_in_button()
        time.sleep(6)
        self.wantedResultObj.fill_Saerch_field("product")
        self.signInPageObject.click_to_sign_in_button()
        time.sleep(6)
        self.ProductPageObj.fill_Saerch_field()
        self.signInPageObject.click_to_sign_in_button()
        time.sleep(6)





    def tearDown(self) -> None:
        self.driver.close()