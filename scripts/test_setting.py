import os, sys
sys.path.append(os.getcwd())

from base.base_driver import init_driver
from page.setting_page import SettingPage

class TestSetting:

    def setup(self):
        self.driver = init_driver()
        # self.setting_page = SettingPage(self.driver)


    def teardown(self):
        self.driver.quit()

    def test_search(self):

        # 点击 搜索
        # 输入 文字
        # 点击 返回



        self.setting_page.click_search()
        self.setting_page.input_text_view("nihao")
        self.setting_page.click_back()
