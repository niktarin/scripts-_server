from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from threading import Thread
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base_tr(Thread):

    def __init__(self, scenario_settings):
        Thread.__init__(self)
        self.driver = None
        self.settings = scenario_settings
        self.scenario_log = []
        self.answer = {"output_data": {},
                       "comment": "",
                       "status": "",}

    def click_esc(self, circle=4, time_wait=1):
        for i in circle:
            webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
            time.sleep(time_wait)

    def check_block(self):
        if "facebook.com/checkpoint/block/" in self.driver.current_url:
            return (False, "Аккаунт заблокмрован")
        elif "facebook.com/checkpoint/" in self.driver.current_url:
            return (False, "Аккаунт на чекпоинте")
        else:
            return (True, "Аккаунт не заблокирован")

    def click_to_xpath(self, xpath, appointment=None, time_wait=60, error=True):
        try:
            WebDriverWait(self.driver, time_wait).until(EC.presence_of_element_located((By.XPATH, xpath)))
            elem = self.driver.find_element_by_xpath(xpath)
            elem.click()
            self.scenario_log.append(f"{appointment}/ нажат {xpath}")
            return True
        except:

            flag, comment = self.check_block()
            if not flag:
                self.scenario_log.append(comment)
                return False
            else:
                if error:
                    self.scenario_log.append(f"{appointment} / не удалось нати {xpath}")
                    return False
                else:
                    return False

    def click_to_element(self, element, appointment=None, circle=60, time_sleep=2):
        summ = 0
        while summ != circle:
            try:
                element.click()
                self.scenario_log.append(f"{appointment}/ нажат элемент'")
                return True
            except:
                summ += 1
                time.sleep(time_sleep)

        flag, comment = self.check_block()
        if not flag:
            self.scenario_log.append(comment)
            return False
        else:
            self.scenario_log.append(f"{appointment} / не удалось нати элемент")
            return False

    def set_text(self, xpath, text, time_wait=60, appointment=None, delay=0.1):
        try:
            WebDriverWait(self.driver, time_wait).until(EC.presence_of_element_located((By.XPATH, xpath)))
            element = self.driver.find_element_by_xpath(xpath)
            element.clear()
            for c in text:
                element.send_keys(c)
                time.sleep(delay)
            self.scenario_log.append(f"{appointment}/ в {xpath} вставлен текс: {text} ")
        except:

            flag, comment = self.check_block()
            if not flag:
                self.scenario_log.append(comment)
                return False
            else:
                self.scenario_log.append(f"{appointment} / не удалось нати элемент")
                return False

    def window_handles_go(self, handles, appointment=None):
        lenght = len(self.driver.window_handles)
        url = self.driver.current_url
        if handles >= lenght:
            self.scenario_log.append(
                f"{appointment}/ переход в вкладку {handles}  количесство вкладок {lenght} текущая ссылка {url}")
            return False
        try:
            window = self.driver.window_handles[1]
            self.driver.switch_to.window(window)
            new_href = self.driver.current_url
            self.scenario_log.append(f"{appointment}/ переход во вкладку {new_href} из вкладки  {url}")
            return True
        except:
            self.scenario_log.append(
                f"{appointment}/ ОШИБКА переход в вкладку {handles}  количесство вкладок {lenght} текущая ссылка {url}")
            return False

    def enter_click(self, xpath, appointment=None, time_wait=60):
        try:
            WebDriverWait(self.driver, time_wait).until(EC.presence_of_element_located((By.XPATH, xpath)))
            element = self.driver.find_element_by_xpath(xpath)
            element.send_keys(Keys.ENTER)
            self.scenario_log.append(f"{appointment}/ нажат ENTER {xpath}")
        except:

            flag, comment = self.check_block()
            if not flag:
                self.scenario_log.append(comment)
                return False
            else:
                self.scenario_log.append(f"{appointment} / не удалось нати элемент")
                return False

    def scroll_page_down(self, down=300, appointment=None):
        html = self.driver.find_element_by_tag_name('html')
        for i in range(down):
            html.send_keys(Keys.DOWN)
        self.scenario_log.append(f"{appointment} / скролл в низ на {down} )")
        return True

    def scroll_page_up(self, up=300, appointment=None):

        html = self.driver.find_element_by_tag_name('html')
        for i in range(up):
            html.send_keys(Keys.UP)
        self.scenario_log.append(f"{appointment} / скролл в верх на {up} )")
        return True

    def selected_chec_boxs(self, xpath, index, time_wait=60, appointment=None):
        try:
            WebDriverWait(self.driver, time_wait).until(EC.presence_of_element_located((By.XPATH, xpath)))
            elements = self.driver.find_elements_by_xpath(xpath)
            if len(elements) <= index:
                self.scenario_log.append(f"{appointment} / чекбоксов {xpath} меньше индека {index}")
                return False
            element = elements[index]
            element.click()
            self.scenario_log.append(f"{appointment} / чекбокс {xpath} выбран {index}")

            return True
        except:
            flag, comment = self.check_block()
            if not flag:
                self.scenario_log.append(comment)
                return False
            else:
                self.scenario_log.append(f"{appointment} / не удалось нати {xpath}")
                return False

    def set_current_index(self, xpath, index, time_wait=60, appointment=None):
        try:
            WebDriverWait(self.driver, time_wait).until(EC.presence_of_element_located((By.XPATH, xpath)))
            element = self.driver.find_element_by_xpath(xpath)
            select = Select(element)
            select.select_by_index(index)
            self.scenario_log.append(f"{appointment} / элемент{xpath} выбран индекс {index}")
            return True
        except:
            flag, comment = self.check_block()
            if not flag:
                self.scenario_log.append(comment)
                return False
            else:
                self.scenario_log.append(f"{appointment} / не удалось нати {xpath}")
                return False

    def check_login_or_not(self):
        ar = ["https://www.facebook.com/", "https://www.facebook.com"]
        if self.driver.current_url in ar:
            return (True)
        return (False)

    def check_xpath(self, xpath, time_wait=60):
        try:
            WebDriverWait(self.driver, time_wait).until(EC.presence_of_element_located((By.XPATH, xpath)))
            return True
        except:
            return False

    def to_start_page(self):

        self.driver.get("https://www.facebook.com/")
        try:
            xpath = "//a[@class=' layerButton _4jy0 _4jy4 _4jy1 _51sy selected _42ft']"
            if self.check_xpath(xpath):
                self.click_to_xpath(xpath)
        except:
            pass

        try:
            xpath = "//input[@name='email']"
            text = self.settings["email_f"]
            self.set_text(xpath=xpath, text=text, appointment="Вход в аккаунт")

            xpath = "//input[@name='pass']"
            text = self.settings["fb_password"]
            self.set_text(xpath=xpath, text=text, appointment="Вход в аккаунт")

            xpath = "//input[@type='submit']"
            self.click_to_xpath(xpath=xpath)
            return True

        except:
            pass

        try:
            xpath = "//input[@name='email']"
            text = self.settings["email_f"]
            self.set_text(xpath=xpath, text=text, appointment="Вход в аккаунт")

            xpath = "//input[@name='pass']"
            text = self.settings["fb_password"]
            self.set_text(xpath=xpath, text=text, appointment="Вход в аккаунт")

            xpath = "//button[@id='loginbutton']"
            self.click_to_xpath(xpath=xpath)
            return True
        except:
            pass

        return False

    def check(self):

        self.to_start_page()

        flag, ans = self.check_block()
        if not flag:
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = ans
            return False

        self.click_esc(circle=2)

        if not self.check_login_or_not():
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = "Не удалось залогиниться"
            return False

        self.click_esc(circle=4, time_wait=1)

        xpath = "//div[@data-tooltip-display='overflow' and text()='Continue']"
        if self.check_xpath(xpath=xpath, time_wait=5):
            self.click_to_xpath(xpath)

            xpath = "//div[@data-tooltip-display='overflow' and text()='Keep Off']"
            self.click_to_xpath(xpath)

            xpath = "//div[@data-tooltip-display='overflow' and text()='Close']"
            self.click_to_xpath(xpath)

        return (True)
