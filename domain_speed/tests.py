rom django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from domain_speed.views import speed

class DomainSpeedTest(TestCase):
    def test_root_url_resolves_to_domain_speed_view(self):
        found = resolve('/')
        self.assertEqual(found.func, speed)

    def test_speed_returns_correct_html(self):
        request = HttpRequest()
        response = speed(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>To-Do lists</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))
