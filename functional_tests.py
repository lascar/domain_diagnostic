import pdb
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
import time
import unittest
from domain_speed.views import speed 



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
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'dominio o IP'
        )


        inputbox.send_keys('google.com')
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
