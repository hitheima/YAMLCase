import os, sys, pytest
sys.path.append(os.getcwd())

from base.base_driver import init_driver
from page.setting_page import SettingPage
from base.base_analyze_yml import analyze_yml

def analyze_key(func_name):
    dict = analyze_yml("setting_data")
    return dict[func_name]


class TestSetting:

    def setup(self):
        self.driver = init_driver()
        self.setting_page = SettingPage(self.driver)

    def teardown(self):
        self.driver.quit()

    # analyze_keyxxxxxx("file_name" , "key")
    @pytest.mark.parametrize("content", analyze_key("test_search_english"))
    def test_search_english(self, content):
        self.setting_page.click_search()
        self.setting_page.input_text_view(content)
        self.setting_page.click_back()

    @pytest.mark.parametrize("content", analyze_key("test_search_chinese"))
    def test_search_chinese(self, content):
        self.setting_page.click_search()
        self.setting_page.click_back()
        self.setting_page.click_search()
        self.setting_page.input_text_view(content)
        self.setting_page.click_back()
