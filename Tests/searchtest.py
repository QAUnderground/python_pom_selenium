from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import unittest
from PageObjects.homepage import HomePage

class GoogleSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"

    def test_google_search(self):
        driver = self.driver
        driver.get(self.base_url)
        homepage = HomePage(driver)
        homepage.enter_search_text("QA Underground Tutorial for beginners")
        homepage.press_return_key_search_field()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()