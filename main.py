import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Delikateska_Tests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge()

    def test_oranges_on_mainpage(self):
         driver = self.driver
         driver.get("https://delikateska.ru")
         assert "Апельсины Сицилийские ~1кг" in driver.page_source

    def test_search_desktop(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://www.delikateska.ru")
        driver.find_element(By.ID, "search-input").send_keys("Апельсины Сицилийские" + Keys.ENTER)
        time.sleep(2)
        assert "Апельсины Сицилийские ~1кг" in driver.page_source

    def test_search_mobile(self):
        driver = self.driver
        driver.set_window_size(800, 1000)
        driver.get("https://www.delikateska.ru/")
        time.sleep(2)
        button_element = driver.find_element(By.XPATH,".//div[@id='onesignal-slidedown-container'] //button[@id='onesignal-slidedown-cancel-button']")
        button_element.click()
        time.sleep(2)
        button_element1 = driver.find_element(By.XPATH, ".//div[@class='search-mobile__icon'] //picture[@class='picture-component ']")
        button_element1.click()
        time.sleep(2)
        driver.find_element(By.XPATH, ".//div[@class='search-mobile-result'] //input").send_keys("Апельсины Сицилийские" + Keys.ENTER)
        time.sleep(2)
        assert "Апельсины Сицилийские ~1кг" in driver.page_source

    def test_login(self):
        driver = self.driver
        driver.get("https://www.delikateska.ru/")
        time.sleep(2)
        button_element = driver.find_element(By.XPATH, ".//div[@id='onesignal-slidedown-container'] //button[@id='onesignal-slidedown-cancel-button']")
        button_element.click()
        time.sleep(2)
        button_element = driver.find_element(By.XPATH, ".//div[@class='login-btn'] //picture")
        button_element.click()
        driver.find_element(By.XPATH, ".//input[@class='InputWrapper__input']").send_keys("banoga2707@necktai.com" + Keys.ENTER)
        time.sleep(1)
        driver.find_element(By.XPATH, ".//input[@class='InputWrapper__input InputWrapper__input--code']").send_keys("test123" + Keys.ENTER)
        time.sleep(3)
        driver.find_element(By.XPATH, ".//div[@class='account-btn__sub-title']")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()