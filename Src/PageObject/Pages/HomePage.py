from selenium.webdriver.common.by import By
from Src.PageObject.Locators.HomeLocators import Locator


class Home():
    def __init__(self, driver):
        self.driver = driver
        self.search_text = driver.find_element(By.XPATH, Locator.search_box)

    def getSearchText(self):
        return self.search_text
    def PressSumbit(self):
        self.search_text.submit()

    def ClickonSearchbox(self):
         self.search_text.click()
    def AddSearchWord(self,SearchKeyWord):
        self.search_text.send_keys(SearchKeyWord)


