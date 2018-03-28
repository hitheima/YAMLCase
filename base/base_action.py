from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def click(self, loc, time=10, poll=1):
        self.find_element(loc, time, poll).click()

    def input_text(self, loc, text, time=10, poll=1):
        self.find_element(loc, time, poll).send_keys(text)

    def find_element(self, loc, time, poll):
        # By.XPATH,            ("text", "显示")
        loc_by, loc_value = loc
        if loc_by == By.XPATH:
            # //*[contains(@text,'显示')]

            # str = 456
            # "123%s789" % str <==> "123" + str + "789"
            # 结果 123456
            loc_value = "//*[contains(@" + loc_value[0] + ",'" + loc_value[1] + "')]"
        # return self.driver.find_element(loc_by, loc_value)
        return WebDriverWait(self.driver, time, poll).until(lambda x: x.find_element(loc_by, loc_value))

    def find_elements(self, loc, time, poll):
        # By.XPATH,            ("text", "显示")
        loc_by, loc_value = loc
        if loc_by == By.XPATH:
            # //*[contains(@text,'显示')]

            # str = 456
            # "123%s789" % str <==> "123" + str + "789"
            # 结果 123456789
            loc_value = "//*[contains(@" + loc_value[0] + ",'" + loc_value[1] + "')]"
        # return self.driver.find_element(loc_by, loc_value)
        return WebDriverWait(self.driver, time, poll).until(lambda x: x.find_elements(loc_by, loc_value))
