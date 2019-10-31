from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from threading import Thread
import requests
import time
import json
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Base_tr(Thread):

    def __init__(self, scenario_settings):
        Thread.__init__(self)
        self.settings = scenario_settings
        self.answer = {"id_scenarios":scenario_settings["id_scenarios"],

                        "type_scenario": scenario_settings["type_scenario"],
                        "output_data":{},
                        "comment":"",
                        "status":"",
                        }

    def find_xpath(self, xpath, circle=60, time_sleep=2):
        summ = 0
        while summ != circle:
            try:
                self.driver.find_element_by_xpath(xpath)
                return (True)
            except NoSuchElementException:
                time.sleep(time_sleep)
            summ += 1
        self.answer["status"] = "Ошибка"
        self.answer["comment"] = f"Не удалось найти {xpath}"
        return (False)

    def connect_to_multilogin(self):
        for i in range(2):
            try:
                mla_url = 'http://127.0.0.1:35000/api/v1/profile/start?automation=true&profileId=' + self.settings["ml_token"]
                resp = requests.get(mla_url)
                json = resp.json()
                # print(json)
                if json["status"] == "ERROR":
                    if "value" in json:
                        index =  json["value"].find("active already")
                
                        if index > -1:
                            json = {"answer": False, "comment": "Аккаунт уже запущен"}
                            return json

                    json = {"answer":False, "comment":"Не удалось запустить аккаунт"}
                    return json

                else:
                    self.driver = webdriver.Remote(command_executor=json['value'])
                    time.sleep(5)
                    json = {"answer":True}
                    return json

            except:
                time.sleep(10)

        json = {"answer":False, "comment":"Ошибка подключения к мультилогину(Возможно он не запущенн)"}
        return json

    def check_xpath(self, xpath):
        try:
            self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True

    def click_to_xpath(self, xpath, circle=60, time_sleep=2):
        summ = 0
        while summ != circle:
            try:
                self.driver.find_element_by_xpath(xpath).click()
                return (True)
            except :
                summ += 1
                time.sleep(time_sleep)

        if not self.check_block():
            self.answer["status"] = "Блок"
            self.answer["comment"] = f"Аккаун заблокированн во время работы скрипта"
            return (False)

        self.answer["status"] = "Ошибка"
        self.answer["comment"] = f"Не удалось найти {xpath}"
        return (False)

    def click_to_element(self, element, circle=60, time_sleep=2):
        summ = 0
        while summ != circle:
            try:
                element.click()
                return (True)
            except:
                webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
                time.sleep(1)
                summ += 1
                time.sleep(time_sleep)

        if not self.check_block():
            self.answer["status"] = "Блок"
            self.answer["comment"] = f"Аккаун заблокированн во врем работы скрипта"
            return (False)
        self.answer["status"] = "Ошибка"
        self.answer["comment"] = f"Не удалось найти елемент"
        return (False)

    def get_tu_link(self, link):
        try:
            self.driver.get(link)
            return (True)
        except:
            return (False)

    def set_text(self, xpath , text, delay=0.1):
        summ = 0
        while summ != 10:
            if self.check_xpath(xpath):
                element = self.driver.find_element_by_xpath(xpath)
                element.clear()
                for c in text :
                    # endtime = time.time() + delay
                    element.send_keys(c)
                    time.sleep(delay)
                return (True)
            else:
                summ += 1
                time.sleep(1)

        if not self.check_block():
            self.answer["status"] = "Блок"
            self.answer["comment"] = f"Аккаун заблокированн"
            return (False)
        return False

    def window_handles_go(self, handles):
        lenght = len( self.driver.window_handles)
        if handles >= lenght:
            return False
        try:
            window = self.driver.window_handles[1]
            self.driver.switch_to.window(window)
            return True
        except:
            return False

    def enter_click(self, xpath):
        if self.check_xpath(xpath):
            element = self.driver.find_element_by_xpath(xpath)
            element.send_keys(Keys.ENTER)
            return (True)
        else:
            return (False)

    def scroll_page_down(self, down=300):
        html = self.driver.find_element_by_tag_name('html')
        for i in range(down):
            html.send_keys(Keys.DOWN)
        return True

    def scroll_page_up(self, up=300):

        html = self.driver.find_element_by_tag_name('html')
        for i in range(up):
            html.send_keys(Keys.UP)
        return True

    def selected_chec_boxs(self, xpath, index):
        summ = 0
        while summ != 10:
            if self.check_xpath(xpath):
                elements = self.driver.find_elements_by_xpath(xpath)
                if len(elements) <= index:
                    return False
                element = elements[index]
                element.click()
                return (True)
            else:
                summ += 1
                time.sleep(1)
        return (False)

    def set_current_index(self, xpath,index):
        summ = 0
        while summ != 20:
            if self.check_xpath(xpath):
                element = self.driver.find_element_by_xpath(xpath)
                select = Select(element)
                
                select.select_by_index(index)
                return (True)
            else:
                summ += 1
                time.sleep(1)
        return (False)

    def check_block(self):
        if "facebook.com/checkpoint" in  self.driver.current_url:
            return (False)
        return (True)

    def check_login_or_not(self):
        ar = ["https://www.facebook.com/", "https://www.facebook.com"]
        if self.driver.current_url in ar:
            return (True)
        return (False)

    def to_start_page(self):
        try:
            self.driver.get("https://www.facebook.com/")
            try:
                xpath = "//a[@class=' layerButton _4jy0 _4jy4 _4jy1 _51sy selected _42ft']"
                if self.check_xpath(xpath):
                    self.click_to_xpath(xpath)
            except:
                pass

            try:
                xpath = "//input[@name='email']"
                element = self.driver.find_element_by_xpath(xpath)
                element.clear()
                element.send_keys(self.settings["email_f"])

                xpath = "//input[@name='pass']"
                element = self.driver.find_element_by_xpath(xpath)
                element.clear()
                element.send_keys(self.settings["fb_password"])

                xpath = "//input[@type='submit']"
                element = self.driver.find_element_by_xpath(xpath)
                element.click()
            except:
                pass
            try:
                xpath = "//input[@name='email']"
                element = self.driver.find_element_by_xpath(xpath)
                element.clear()
                element.send_keys(self.settings["email_f"])
                time.sleep(2)
                xpath = "//input[@name='pass']"
                element = self.driver.find_element_by_xpath(xpath)
                element.clear()
                element.send_keys( self.settings["fb_password"])
                time.sleep(2)
                xpath = "//button[@id='loginbutton']"
                element = self.driver.find_element_by_xpath(xpath)
                element.click()
            except:
                pass
            return (True)
        except:
            return (False)

    def check_ip_data(self):
        self.driver.get("http://ipinfo.io/json")
        el = self.driver.find_element_by_xpath("//pre")
        self.ip_settings = json.loads(el.text)

    def check(self):

        self.to_start_page()

        if not self.check_block():
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = f"Аккаунт заблокирован"
            return (False)

        webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()

        if not self.check_login_or_not():
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = f"Не удалось залогиниться"
            return (False)

        webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
        time.sleep(3)
        webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()


        xpath = "//div[@data-tooltip-display='overflow' and text()='Continue']"
        if self.find_xpath(xpath=xpath,circle=7,time_sleep=1):
            self.click_to_xpath(xpath)

            xpath = "//div[@data-tooltip-display='overflow' and text()='Keep Off']"
            self.click_to_xpath(xpath)

            xpath = "//div[@data-tooltip-display='overflow' and text()='Close']"
            self.click_to_xpath(xpath)
        else:
            xpath = "//div[@data-tooltip-display='overflow' and text()='Review Setting']"
            if self.find_xpath(xpath=xpath,circle=7,time_sleep=1):
                self.click_to_xpath(xpath)

                xpath = "//div[@data-tooltip-display='overflow' and text()='Keep Off']"
                self.click_to_xpath(xpath)

                xpath = "//div[@data-tooltip-display='overflow' and text()='Close']"
                self.click_to_xpath(xpath)

        return (True)
