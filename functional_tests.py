import pdb
import re
import os, sys
proj_path = "."
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "domain_diagnostics.settings")
sys.path.append(proj_path)
os.chdir(proj_path)
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
from django.utils.translation import ugettext_lazy as _
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import unittest
from domain_speed.views import speed_html 



class DomainSpeedTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(1)

    def tearDown(self):
        self.browser.quit()

    def test_put_a_domain_and_get_speed(self):
        self.browser.get('http://localhost:8000')
        
        #pdb.set_trace()

        self.assertIn("Herramientas de diagnostico para dominio",
                self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Herramientas de diagnostico para dominio', header_text)

        inputbox = self.browser.find_element_by_id('id_domain')
        self.assertNotIn
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'dominio o IP'
        )

        with self.assertRaises(NoSuchElementException):
            self.browser.find_element_by_xpath("//table")
        inputbox.send_keys('google.com')
        self.browser.find_element_by_css_selector('input[type="submit"]').submit()
        table = self.browser.find_element_by_id('table-results')
        tds = table.find_elements_by_xpath('//td')
        self.assertEqual('google.com', tds[0].text)
        self.assertEqual('200', tds[1].text)
        self.assertRegex(tds[2].text, "\d+ milisegundos")

if __name__ == '__main__':
    unittest.main(warnings='ignore')
