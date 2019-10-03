from scripts.base_tread import Base_tr
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import random
import time

class Simple_update_fb(Base_tr):

    def start_page_scroll(self):
        for i in range(5):
            webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
            time.sleep(1)

        xpath = "//span[@class='_2md']"
        if not self.click_to_xpath(xpath):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
            return (False)

        down = random.randint(50, 300)
        if not self.scroll_page_down(down):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
            return (False)

        if not self.scroll_page_up(down):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
            return (False)

        return (True)

    def fan_page_scroll(self):
        for i in range(5):
            webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
            time.sleep(1)

        if "fan_pages_scroll" not in self.settings:
            return (True)

        for link in self.settings["fan_pages_scroll"]:
            link.replace(" ","")
            if link == "":
                return (True)
            try:
                self.driver.get(link)
                down = random.randint(50, 300)
                self.scroll_page_down(down)
                self.scroll_page_up(down)

            except:
                pass
        return (True)

    def friends_page_scroll(self):

        for i in range(5):
            webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
            time.sleep(1)

        xpath = "//span[@class='_2md']"
        if not self.click_to_xpath(xpath):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
            return (False)

        for i in range(4):
            webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
            time.sleep(1)

        xpath = "(//div[@class='linkWrap noCount'])[1]"
        if not self.click_to_xpath(xpath):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
            return (False)





        # xpath = "//button[@class='_42ft _5upp _50zy layerCancel _36gl _50-0 _50z_']"
        # self.click_to_xpath(xpath = xpath, circle=30, time_sleep=1)

        # xpath = "//div[@id='fbTimelineHeadline']/div/ul/li[3]/a"
        # if not self.click_to_xpath(xpath):

        #     xpath = "//button[@class='_42ft _5upp _50zy layerCancel _36gl _50-0 _50z_']"
        #     self.click_to_xpath(xpath = xpath, circle=30, time_sleep=1)

        #     xpath = "//div[@id='fbTimelineHeadline']/div/ul/li[3]/a"
        #     if not self.click_to_xpath(xpath):
        #         self.answer["status"] = "Ошибка"
        #         self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
        #         return (False)


        # xpath = "//a[@href='/find-friends/browser/']"
        # if not self.click_to_xpath(xpath):
        #     self.answer["status"] = "Ошибка"
        #     self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
        #     return (False)
        self.driver.get("https://www.facebook.com/find-friends/browser/")
        for i in range(4):
            webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
            time.sleep(1)


        down = random.randint(15, 200)
        if not self.scroll_page_down(down):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = f"Не удалось пролистать страницу"
            return (False)

        if not self.scroll_page_up(down):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = f"Не удалось пролистать страницу"
            return (False)

        return(True)

    def refresh(self):
        ran = random.randint(1, 2)
        t = random.randint(10, 20)
        for i in range(ran):
            self.driver.refresh()
            time.sleep(t)

    def run(self):

        if not self.check():
            return

        arr_action = [  self.start_page_scroll,
                        self.fan_page_scroll,
                        self.friends_page_scroll]

        random.shuffle(arr_action)

        for act in arr_action:
            if not act():
                self.live = False
                return
            self.refresh()

        self.answer["comment"] = "Пустое обновление прошло успешно"
        self.answer["status"] = "Выполнен"
        self.driver.quit()