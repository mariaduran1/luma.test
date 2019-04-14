import unittest
import time
import HtmlTestRunner

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys




class Test_youtube(unittest.TestCase):
    def test_can_search(self):
        driver = webdriver.Chrome('C:\dev1\week5\chromedriver.exe')
        driver.get('https://www.youtube.com')

        search_youtube = driver.find_element_by_id("search")
        submit = driver.find_element_by_id("search-icon-legacy")

        search_youtube.send_keys("chopin")
        submit.click()
       

        first_result = driver.find_element_by_id("video-title")
        first_result.click()
        

        time.sleep(5)

        driver.quit()
    


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output = "./report"))

