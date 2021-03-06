import unittest
import time
import HtmlTestRunner

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys




class Test_Luma(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome('C:\dev1\week5\chromedriver.exe')
        cls.driver.get('http://demo-acm-2.bird.eu/blog')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_can_search(self):

        search_box = self.driver.find_element_by_name("q")
        search_box.send_keys("pants")
        search_box.submit()

        time.sleep(5)

    def test_first_result(self):
        
        links = self.driver.find_elements_by_css_selector(".product-item-link")
        links[0].click()

        time.sleep(5)


        

    


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output = "./report"))


i#f __name__ == "__main__":
    #unittest.main()
