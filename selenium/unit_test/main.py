import os.path
import unittest

import page
from selenium import webdriver


class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        project_directory = os.path.dirname(__file__)
        PATH = (os.path.join(project_directory, "../cookie/./chromedriver"))
        print(PATH)
        self.driver = webdriver.Chrome(PATH)
        self.driver.get("http://www.python.org")

    def test_search_python(self):
        main_page = page.MainPage(self.driver)
        assert main_page.is_title_matches()
        main_page.search_text_element = "pydoc"
        main_page.click_go_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_results_found()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
