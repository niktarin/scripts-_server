from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from threading import Thread
import time
import json
import random
import requests
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base_tr(Thread):

    def __init__(self, scenario_settings, log):
        Thread.__init__(self)
        self.driver = None
        self.settings = scenario_settings
        self.log = log
        self.flag_email_not_confirm = False
        self.tech_name = scenario_settings["tech_name"]
        self.error_comment = None
        self.accaunt_block_flag = False
        self.answer = {"output_data": {},
                       "comment": "",
                       "status": "", }

    def change_language(self, language="English (UK)"):

        self.driver.get("https://www.facebook.com/settings?tab=language&section=account&view")
        xpath = "//select[@name='new_language']"
        if not self.set_visible_text(xpath, language, appointment="выбор языка из списка"):
            self.answer["status"] = "Ошибка сервера"
            self.answer["comment"] = self.error_comment
            return False

        xpath = "//label[@class='submit uiButton uiButtonConfirm']"
        if self.find_xpath(xpath):
            if not self.click_to_xpath(xpath, appointment="подтверждение смены языка"):
                self.answer["status"] = "Ошибка сервера"
                self.answer["comment"] = self.error_comment
                return False
            time.sleep(5)
            return True

        else:
            return False

    def get_link(self, link, appointment=None, action="get_link", circle=4, time_wait=1):
        try:
            self.driver.get(link)
            self.click_esc(circle=circle, time_wait=time_wait)
            self.log.log_append(
                {"name": self.tech_name, "action": action, "text": f"{appointment}/ переход по ссылке  {link}"})
            return True
        except:
            self.log.log_append(
                {"name": self.tech_name, "action": action,
                 "text": f"{appointment}/ Не удалось перейти по ссылке  {link}"})
            return False

    def check_text_in_link(self, text, action="find", appointment="find_text_link", circle=15, time_wait=1):
        for i in range(circle):
            url = self.driver.current_url
            if text in url:
                self.log.log_append(
                    {"name": self.tech_name, "action": action, "text": f"{appointment}/ текст найден {text}"})
                return True
            else:
                time.sleep(time_wait)

        self.log.log_append(
            {"name": self.tech_name, "action": action, "text": f"{appointment}/ текст не найден {text}"})
        return False

    def click_esc(self, circle=4, time_wait=1):
        for i in range(circle):
            webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
            time.sleep(time_wait)

    def check_ip_data(self):
        self.get_link("http://ipinfo.io/json")
        el = self.return_el_by_xpath("//pre")
        if el != None:
            self.ip_settings = json.loads(el.text)
            return True
        else:
            return False

    def check_block(self):
        if "facebook.com/checkpoint/block/" in self.driver.current_url:
            self.accaunt_block_flag = True
            return (False, "Аккаунт заблокирован")
        elif "facebook.com/checkpoint/" in self.driver.current_url:
            self.accaunt_block_flag = True
            return (False, "Аккаунт на чекпоинте")
        else:
            self.accaunt_block_flag = False
            return (True, "Аккаунт не заблокирован")

    def return_el_by_xpath(self, xpath, time_wait=15, action="return_el"):
        try:
            WebDriverWait(self.driver, time_wait).until(EC.presence_of_element_located((By.XPATH, xpath)))
            element = self.driver.find_element_by_xpath(xpath)
            commant = f"найден элемент {xpath}"
            self.log.log_append({"name": self.tech_name, "action": action, "text": commant})
            return element
        except:
            commant = f"НЕ найден элемент {xpath}"
            self.log.log_append({"name": self.tech_name, "action": action, "text": commant})
            return None

    def find_xpath(self, xpath, time_wait=15, action="find"):
        try:
            WebDriverWait(self.driver, time_wait).until(EC.presence_of_element_located((By.XPATH, xpath)))
            commant = f"найден элемент {xpath}"
            self.log.log_append({"name": self.tech_name, "action": action, "text": commant})
            return True
        except:
            commant = f"НЕ найден элемент {xpath}"
            self.log.log_append({"name": self.tech_name, "action": action, "text": commant})
            return False

    def click_to_xpath(self, xpath, action="action", appointment=None, time_wait=15, esc_flag=True, error=True):
        try:
            WebDriverWait(self.driver, time_wait).until(EC.presence_of_element_located((By.XPATH, xpath)))
            elem = self.driver.find_element_by_xpath(xpath)
            elem.click()
            self.log.log_append({"name": self.tech_name, "action": action, "text": f"{appointment}/ нажат {xpath}"})
            return True
        except:
            pass

        if esc_flag:
            self.click_esc()
            try:
                WebDriverWait(self.driver, time_wait).until(EC.presence_of_element_located((By.XPATH, xpath)))
                elem = self.driver.find_element_by_xpath(xpath)
                elem.click()
                self.log.log_append(
                    {"name": self.tech_name, "action": action, "text": f"{appointment}/ нажат {xpath}"})
                return True
            except:
                pass

        flag, comment = self.check_block()
        if not flag:
            self.log.log_append({"name": self.tech_name, "action": action, "text": comment})
            self.error_comment = comment
            return False
        else:
            if error:
                comment = f"{appointment} / не удалось нажать {xpath}"
                self.log.log_append({"name": self.tech_name, "action": action, "text": comment})
                self.error_comment = comment
                return False
            else:
                self.error_comment = comment
                return False

    def click_to_element(self, element, action="action", appointment=None, circle=60, time_sleep=2):
        summ = 0
        while summ != circle:
            try:
                element.click()
                self.log.log_append(
                    {"name": self.tech_name, "action": action, "text": f"{appointment}/ нажат элемент'"})
                return True
            except:
                summ += 1
                time.sleep(time_sleep)

        flag, comment = self.check_block()
        if not flag:
            self.log.log_append({"name": self.tech_name, "action": action, "text": comment})
            self.error_comment = comment
            return False
        else:
            comment = f"{appointment} / не удалось нати элемент"
            self.log.log_append({"name": self.tech_name, "action": action, "text": comment})
            self.error_comment = comment
            return False

    def set_text(self, xpath, text, action="action", time_wait=60, appointment=None, delay=0.1):
        try:
            WebDriverWait(self.driver, time_wait).until(EC.presence_of_element_located((By.XPATH, xpath)))
            element = self.driver.find_element_by_xpath(xpath)
            element.clear()
            for c in text:
                element.send_keys(c)
                time.sleep(delay)
            self.log.log_append(
                {"name": self.tech_name, "action": action, "text": f"{appointment}/ в {xpath} вставлен текс: {text}"})
            return True
        except:

            flag, comment = self.check_block()
            if flag:
                self.log.log_append({"name": self.tech_name, "action": action, "text": comment})
                self.error_comment = comment
                return False
            else:
                comment = f"{appointment} / не удалось нати элемент"
                self.log.log_append(
                    {"name": self.tech_name, "action": action, "text": comment})
                self.error_comment = comment
                return False

    def window_handles_go(self, handles = 1, action="handles_go", appointment=None):
        lenght = len(self.driver.window_handles)
        url = self.driver.current_url
        if (handles-1) >= lenght:
            self.log.log_append({"name": self.tech_name, "action": action, "text":
                f"{appointment}/ переход в вкладку {handles}  количесство вкладок {lenght} текущая ссылка {url}"})
            return False
        try:
            window = self.driver.window_handles[handles]
            self.driver.switch_to.window(window)
            new_href = self.driver.current_url
            self.log.log_append({"name": self.tech_name, "action": action,
                                 "text": f"{appointment}/ переход во вкладку {new_href} из вкладки  {url}"})
            return True
        except:
            self.log.log_append({"name": self.tech_name, "action": action, "text":
                f"{appointment}/ Ошибка переход в вкладку {handles}  количесство вкладок {lenght} текущая ссылка {url}"})
            return False

    def enter_click(self, xpath, action="enter_clic", appointment=None, time_wait=60):
        try:
            WebDriverWait(self.driver, time_wait).until(EC.presence_of_element_located((By.XPATH, xpath)))
            element = self.driver.find_element_by_xpath(xpath)
            element.send_keys(Keys.ENTER)
            self.log.log_append(
                {"name": self.tech_name, "action": action, "text": f"{appointment}/ нажат ENTER {xpath}"})
        except:

            flag, comment = self.check_block()
            if not flag:
                self.log.log_append({"name": self.tech_name, "action": action, "text": comment})
                return False
            else:
                self.log.log_append(
                    {"name": self.tech_name, "action": action, "text": f"{appointment} / не удалось нати элемент"})
                return False

    def scroll_page_down(self, down=300, action="action", time_sleep=0.1, appointment=None):
        html = self.driver.find_element_by_tag_name('html')
        for i in range(down):
            html.send_keys(Keys.DOWN)
            time.sleep(time_sleep)
        self.log.log_append(
            {"name": self.tech_name, "action": action, "text": f"{appointment} / скролл в низ на {down})"})
        return True

    def scroll_page_up(self, up=300, action="action", time_sleep=0.1, appointment=None):

        html = self.driver.find_element_by_tag_name('html')
        for i in range(up):
            try:
                html.send_keys(Keys.UP)
            except:
                pass
            time.sleep(time_sleep)

        self.log.log_append(
            {"name": self.tech_name, "action": action, "text": f"{appointment} / скролл в верх на {up})"})
        return True

    def selected_chec_boxs(self, xpath, index, action="selected_chec",time_wait=60, appointment=None):
        try:
            WebDriverWait(self.driver, time_wait).until(EC.presence_of_element_located((By.XPATH, xpath)))
            elements = self.driver.find_elements_by_xpath(xpath)
            if len(elements) <= index:
                self.log.log_append({"name": self.tech_name, "action": action,
                                     "text": f"{appointment} / чекбоксов {xpath} меньше индека {index}"})
                return False
            element = elements[index]
            element.click()
            self.log.log_append(
                {"name": self.tech_name, "action": action, "text": f"{appointment} / чекбокс {xpath} выбран {index}"})

            return True
        except:
            flag, comment = self.check_block()
            if not flag:
                self.log.log_append({"name": self.tech_name, "action": action, "text": comment})
                return False
            else:
                self.log.log_append(
                    {"name": self.tech_name, "action": action, "text": f"{appointment} / не удалось нати {xpath}"})
                return False

    def set_visible_text(self, xpath, text, action="action", time_wait=60, appointment=None):
        try:
            WebDriverWait(self.driver, time_wait).until(EC.presence_of_element_located((By.XPATH, xpath)))
            element = self.driver.find_element_by_xpath(xpath)
            select = Select(element)
            select.select_by_visible_text(text)
            self.log.log_append({"name": self.tech_name, "action": action,
                                 "text": f"{appointment} / элемент {xpath} выбран текст '{text}'"})
            return True
        except:
            flag, comment = self.check_block()
            if not flag:
                self.log.log_append({"name": self.tech_name, "action": action, "text": comment})
                return False
            else:
                comment = f"{appointment} / не удалось нати {xpath}"
                self.log.log_append({"name": self.tech_name, "action": action, "text": comment})
                self.error_comment = comment
                return False

    def set_current_index(self, xpath, index, action="action", time_wait=60, appointment=None):
        try:
            WebDriverWait(self.driver, time_wait).until(EC.presence_of_element_located((By.XPATH, xpath)))
            element = self.driver.find_element_by_xpath(xpath)
            select = Select(element)
            select.select_by_index(index)
            self.log.log_append({"name": self.tech_name, "action": action,
                                 "text": f"{appointment} / элемент {xpath} выбран индекс {index}"})
            return True
        except:
            flag, comment = self.check_block()
            if not flag:
                self.log.log_append({"name": self.tech_name, "action": action, "text": comment})
                return False
            else:
                comment = f"{appointment} / не удалось нати {xpath}"
                self.log.log_append({"name": self.tech_name, "action": action, "text": comment})
                self.error_comment = comment
                return False

    def check_login_or_not(self):
        ar = ["https://www.facebook.com/", "https://www.facebook.com"]
        if self.driver.current_url in ar:
            return True
        elif "www.facebook.com/profile.php" in self.driver.current_url:
            return True
        return False

    def check_xpath(self, xpath, time_wait=60):
        try:
            WebDriverWait(self.driver, time_wait).until(EC.presence_of_element_located((By.XPATH, xpath)))
            return True
        except:
            return False

    def to_start_page(self):

        self.driver.get("https://www.facebook.com/")

        xpath = "//a[@class=' layerButton _4jy0 _4jy4 _4jy1 _51sy selected _42ft']"
        if self.check_xpath(xpath, time_wait=5):
            self.click_to_xpath(xpath, appointment="Клик по непонятной кнопке при входе")

        xpath = "//input[@name='email']"
        text = self.settings["email_f"]

        if self.set_text(xpath=xpath, text=text, appointment="Ввод логина", time_wait=5):
            xpath = "//input[@name='pass']"
            text = self.settings["fb_password"]
            self.set_text(xpath=xpath, text=text, appointment="Ввод пароля", time_wait=5)

            xpath = "//input[@type='submit']"
            if self.click_to_xpath(xpath=xpath, appointment="Кнопка логина"):
                return True

            xpath = "//button[@type='submit']"
            if self.click_to_xpath(xpath=xpath, appointment="Кнопка логина"):
                return True

            xpath = "//button[@id='loginbutton']"
            if self.click_to_xpath(xpath=xpath, appointment="Кнопка логина"):
                return True

        if "facebook.com/confirmemail.php" in self.driver.current_url:
            xpath = "//div[@data-click='profile_icon']"
            if not self.click_to_xpath(xpath, appointment="Акк не подтвержден, нажимем на кнопку"):
                self.answer["status"] = "Ошибка сервера"
                self.answer["comment"] = self.error_comment
                return False

            self.flag_email_not_confirm = True
        return False

    def check(self):
        if self.to_start_page():
            self.log.log_append({"name": self.tech_name, "action": "action", "text": "Логин / Аккаунт залогинелся"})
        else:
            self.log.log_append({"name": self.tech_name, "action": "action", "text": "Логин / Аккаунт не залогинелся"})

        flag, ans = self.check_block()
        if not flag:
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = ans
            return False

        self.click_esc(circle=2, time_wait=1)

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
        else:
            xpath = "//div[@data-tooltip-display='overflow' and text()='Review Setting']"
            if self.find_xpath(xpath=xpath, time_wait=5):
                self.click_to_xpath(xpath)

                xpath = "//div[@data-tooltip-display='overflow' and text()='Keep Off']"
                self.click_to_xpath(xpath)

                xpath = "//div[@data-tooltip-display='overflow' and text()='Close']"
                self.click_to_xpath(xpath)

        return (True)

    def load_img(self, href, img_name=None, appointment=None, action="load_img", circle=3, time_wait=5):
        if img_name == None:
            img_name = f".\\img\\load_img_{random.randint(123456789,999999999)}.jpg"

        try:
            os.remove(img_name)
        except:
            pass

        for i in range(circle):
            try:
                p = requests.get(href)
            except:
                time.sleep(time_wait)
                continue

            out = open(img_name, "wb")
            out.write(p.content)
            out.close()


            self.log.log_append(
                {"name": self.tech_name, "action": action, "text": f"{appointment}/ скачана картинка {href}"})
            return img_name

        self.log.log_append(
            {"name": self.tech_name, "action": action, "text": f"{appointment}/ НЕ скачана картинка {href}"})
        return False





