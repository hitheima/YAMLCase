import os, sys, pytest
sys.path.append(os.getcwd())

from base.base_driver import init_driver
from page.setting_page import SettingPage
from base.base_analyze_yml import analyze_yml

class TestSetting:

    def setup(self):
        self.driver = init_driver()
        self.setting_page = SettingPage(self.driver)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize("content", analyze_yml("setting_data"))
    def test_search(self, content):
        self.setting_page.click_search()
        self.setting_page.input_text_view(content)
        self.setting_page.click_back()
