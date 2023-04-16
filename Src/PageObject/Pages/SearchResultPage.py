from selenium.webdriver.common.by import By

class SearchResult():
    def __init__(self, driver):
        self.driver = driver
    def ReturnURLs(self):
        AssertionFlag=0
        Counter = 1
        elems = self.driver.find_elements(By.XPATH, "//a[@href]")
        for elem in elems:
            if "LambdaTest" in elem.get_attribute("title"):
                print(elem.get_attribute("href"))
                Counter = Counter + 1
            if Counter >= 10:
                AssertionFlag = 1
                print("done")
                break
        return AssertionFlag

