"""Selenium tests against the Kubernetes NodePort service."""
import json
import os
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

BASE_URL = os.environ.get("PALINDROME_URL", "http://localhost:30080")

class PalindromeBrowserTest(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(options=options)

    def tearDown(self):
        if hasattr(self, "driver"):
            self.driver.quit()

    def read_result(self, word):
        self.driver.get(f"{BASE_URL}/check?word={word}")
        return json.loads(self.driver.find_element("tag name", "body").text)

    def test_palindrome(self):
        result = self.read_result("MADAM")
        self.assertTrue(result["palindrome"])

    def test_not_palindrome(self):
        result = self.read_result("HELLO")
        self.assertFalse(result["palindrome"])

if __name__ == "__main__":
    unittest.main()
