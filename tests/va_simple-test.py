# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Testbasicoleroymerlinv2(unittest.TestCase):
    def setUp(self):
    	profile = webdriver.FirefoxProfile()
    	profile.accept_untrusted_certs = True
    	options = Options()
    	options.add_argument("--headless")
        self.driver = webdriver.Firefox(firefox_profile=profile, firefox_options=options)
        self.driver.implicitly_wait(30)
        self.base_url = "https://hybrissitlm:9002/va/lmbr/pt/BRL/login"
        #self.base_url = "https://vahomolog.leroymerlin.com.br/va/lmbr/pt/BRL/login"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_basicoleroymerlinv2(self):
        driver = self.driver
        # //Acesso ao Hybri
        driver.get("https://hybrissitlm:9002/va/lmbr/pt/BRL/login")
        #driver.get("https://vahomolog.leroymerlin.com.br/va/lmbr/pt/BRL/login")
        # // login Hybris
        driver.find_element_by_id("j_username").clear()
        driver.find_element_by_id("j_username").send_keys("51001191")
        driver.find_element_by_id("j_password").clear()
        driver.find_element_by_id("j_password").send_keys("1234")
        driver.find_element_by_xpath("(//button[@type='submit'])[2]").click()
        # //  Criar Carrinho
        driver.find_element_by_link_text("Criar carrinho...").click()
        # // Inserir produto no carrinho via hybris
        driver.find_element_by_name("eanOrCode").clear()
        driver.find_element_by_name("eanOrCode").send_keys("89669160")
        driver.find_element_by_xpath("(//button[@type='submit'])[3]").click()
        # // Logout
        driver.find_element_by_xpath("//li[5]/a/span").click()
        # // Fechar janela
        # // driver.close()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
