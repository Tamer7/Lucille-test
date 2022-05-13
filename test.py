from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class Tester(unittest.TestCase):
    def setUp(self):

        self.driver = webdriver.Chrome("C:\\Users\\leila\\Desktop\\chromedriver.exe") // replace this with the path to ur chromedriver
        self.driver.implicitly_wait(30)
        self.verificationErrors = []


    def test_er(self):
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com/large")
        self.assertIn("large", driver.current_url)
        time.sleep(5)
        el = driver.find_element_by_xpath("//*[@id='large-table']")
        s = el.text
        print("Element exist -" + s)




    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
