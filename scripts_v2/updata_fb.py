from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from .base_tread_v2 import Base_tr
import random
import time


class Updata_fb_tr(Base_tr):

    def my_page_scroll(self):
        xpath = "//span[@class='_2md']"
        if not self.click_to_xpath(xpath, appointment="переход на личную страницу"):
            if self.accaunt_block_flag:
                self.answer["status"] = "Ошибка"
            else:
                self.answer["status"] = "Ошибка сервера"
            self.answer["comment"] = self.error_comment
            return False

        if self.flag_email_not_confirm:
            xpath = "//div[@data-click='profile_icon']"
            if not self.click_to_xpath(xpath, appointment="переход на личную страницу"):
                if self.accaunt_block_flag:
                    self.answer["status"] = "Ошибка"
                else:
                    self.answer["status"] = "Ошибка сервера"
                self.answer["comment"] = self.error_comment
                return False
        else:
            xpath = "(//div[@class='linkWrap noCount'])[1]"
            if not self.click_to_xpath(xpath, appointment="Переход на личную страницу"):
                if self.accaunt_block_flag:
                    self.answer["status"] = "Ошибка"
                else:
                    self.answer["status"] = "Ошибка сервера"
                self.answer["comment"] = self.error_comment
                return False
        if not self.flag_work:
            return True
        down = random.randint(100, 400)
        self.scroll_page_down(down, appointment="Скролл вних")
        time.sleep(5)
        if not self.flag_work:
            return True
        self.scroll_page_up(down, appointment="Скролл вверх")
        return True

    def start_page_scroll(self):
        xpath = "//span[@class='_2md']"
        if not self.click_to_xpath(xpath, appointment="переход на стартовую страницу"):
            if self.accaunt_block_flag:
                self.answer["status"] = "Ошибка"
            else:
                self.answer["status"] = "Ошибка сервера"
            self.answer["comment"] = self.error_comment
            return False

        if self.flag_email_not_confirm:
            xpath = "//div[@data-click='profile_icon']"
            if not self.click_to_xpath(xpath, appointment="переход на стартовую страницу"):
                if self.accaunt_block_flag:
                    self.answer["status"] = "Ошибка"
                else:
                    self.answer["status"] = "Ошибка сервера"
                self.answer["comment"] = self.error_comment
                return False


        if not self.flag_work:
            return True
        down = random.randint(100, 400)
        self.scroll_page_down(down, appointment="Скролл вних")
        time.sleep(5)
        if not self.flag_work:
            return True
        self.scroll_page_up(down, appointment="Скролл вверх")
        return True

    def fan_page_scroll(self):
        self.click_esc()

        if "fan_pages_scroll" not in self.settings:
            return (True)

        for link in self.settings["fan_pages_scroll"]:
            if not self.flag_work:
                return True
            link.replace(" ", "")
            if link == "":
                return (True)
            try:
                self.driver.get(link)
                self.click_esc()
                down = random.randint(50, 300)
                self.scroll_page_down(down)
                time.sleep(5)
                self.scroll_page_up(down)
            except:
                pass
        return True

    def friends_list_scroll(self):
        self.driver.get("https://www.facebook.com/find-friends/browser/")
        self.click_esc()
        if not self.flag_work:
            return True
        down = random.randint(15, 200)
        self.scroll_page_down(down, appointment="Скролл вних")
        if not self.flag_work:
            return True
        self.scroll_page_up(down, appointment="Скролл вверх")
        return True

    def friends_page_scroll(self):
        xpath = "//span[@class='_2md']"
        if not self.click_to_xpath(xpath, appointment="переход на личную страницу"):
            if self.accaunt_block_flag:
                self.answer["status"] = "Ошибка"
            else:
                self.answer["status"] = "Ошибка сервера"
            self.answer["comment"] = self.error_comment
            return False

        xpath = "(//div[@class='linkWrap noCount'])[1]"
        if not self.click_to_xpath(xpath, appointment="Переход на личную страницу"):
            if self.accaunt_block_flag:
                self.answer["status"] = "Ошибка"
            else:
                self.answer["status"] = "Ошибка сервера"
            self.answer["comment"] = self.error_comment
            return False

        xpath = "//div[@id='fbTimelineHeadline']/div/ul/li[3]/a"
        if not self.click_to_xpath(xpath, appointment="Переход на страничку друзей"):
            if self.accaunt_block_flag:
                self.answer["status"] = "Ошибка"
            else:
                self.answer["status"] = "Ошибка сервера"
            self.answer["comment"] = self.error_comment
            return False
        if not self.flag_work:
            return True
        time.sleep(3)
        self.scroll_page_down(15)
        xpath = "//div[@class='uiProfileBlockContent']/div/div/div"
        arr_el = self.driver.find_elements_by_xpath(xpath)
        random.shuffle(arr_el)
        el = arr_el[0]
        el.click()
        time.sleep(5)
        if not self.flag_work:
            return True
        down = random.randint(15, 200)
        self.scroll_page_down(down, appointment="Скролл вних")
        self.scroll_page_up(down, appointment="Скролл вверх")
        return True

    def group_page_scroll(self):
        link = "https://www.facebook.com/groups/"
        self.get_link(link)

        if not self.flag_work:
            return True

        time.sleep(3)
        self.scroll_page_down(15)
        xpath = "//div[@class='mfclru0v _4ik4 _4ik5']"
        arr_el = self.driver.find_elements_by_xpath(xpath)
        random.shuffle(arr_el)
        el = arr_el[0]
        el.click()
        time.sleep(5)

        if not self.flag_work:
            return True
        down = random.randint(15, 200)
        self.scroll_page_down(down, appointment="Скролл вних")
        if not self.flag_work:
            return True

        self.scroll_page_up(down, appointment="Скролл вверх")
        return True

    def likes(self):
        xpath = "//span[@class='_2md']"
        if not self.click_to_xpath(xpath, appointment="переход на личную страницу"):
            if self.accaunt_block_flag:
                self.answer["status"] = "Ошибка"
            else:
                self.answer["status"] = "Ошибка сервера"
            self.answer["comment"] = self.error_comment
            return False

        self.scroll_page_down(100)

        xpath = "//span[@class='_1mto']/div[@class='_khz _4sz1 _4rw5 _3wv2']/a"
        elements_1 = self.driver.find_elements_by_xpath(xpath)

        xpath = "//div[@data-testid='UFI2ReactionLink/actionLink']/div/a"
        elements_2 = self.driver.find_elements_by_xpath(xpath)

        lenght_1 = len(elements_1)
        lenght_2 = len(elements_2)

        elements = elements_1 if lenght_1 >= lenght_2 else elements_2
        lenght = lenght_1 if lenght_1 >= lenght_2 else lenght_2

        maximum = int(self.settings["likes_max"])
        minimum = int(self.settings["likes_min"])

        maximum = maximum if maximum < lenght else lenght
        minimum = minimum if minimum < lenght else lenght

        if maximum < minimum:
            minimum, maximum = maximum, minimum

        likes = random.randint(minimum, maximum)
        likes = likes if likes < len(elements) else len(elements)
        random.shuffle(elements)

        for index in range(likes):
            element = elements[index]
            self.click_to_element(element)
        return True

    def set_reposts(self):

        xpath = "//span[@class='_2md']"
        if not self.click_to_xpath(xpath, appointment="переход на личную страницу"):
            if self.accaunt_block_flag:
                self.answer["status"] = "Ошибка"
            else:
                self.answer["status"] = "Ошибка сервера"
            self.answer["comment"] = self.error_comment
            return False

        self.scroll_page_down(100)
        # try:
        xpath = "//span[@class='_1mto']/span[@class='_27de _4noj']/.."
        elements_1 = self.driver.find_elements_by_xpath(xpath)

        xpath = "//a[@class=' _2nj7  _18vj _18vk']"
        elements_2 = self.driver.find_elements_by_xpath(xpath)

        lenght_1 = len(elements_1)
        lenght_2 = len(elements_2)

        elements = elements_1 if lenght_1 > lenght_2 else elements_2
        # random.shuffle(elements)

        lenght = lenght_1 if lenght_1 >= lenght_2 else lenght_2

        maximum = int(self.settings["repost_max"])
        minimum = int(self.settings["repost_min"])

        maximum = maximum if maximum < lenght else lenght
        minimum = minimum if minimum < lenght else lenght

        reposts = random.randint(minimum, maximum)
        # except:
        #     return False

        for index in range(reposts):

            el = elements[index]
            hover = ActionChains(self.driver).move_to_element(el)
            hover.perform()

            xpath = f"(//div[@class='_6800 uiPopover _6a'])[{index+1}]"
            self.click_to_xpath(xpath)
            # element = elements[index]
            # self.driver.execute_script("arguments[0].click();", element)

            time.sleep(1)
            xpath = "//button[@data-testid='react_share_dialog_post_button']"
            if not self.click_to_xpath(xpath):
                time.sleep(1)
                xpath = f"(//li[@class='_54ni _2al8 __MenuItem']/a/span/span[@class='_54nh'])[last()]"
                self.click_to_xpath(xpath)
                time.sleep(1)
                xpath = "//button[@data-testid='react_share_dialog_post_button'] "
                self.click_to_xpath(xpath)

        return True
        # except:
        #
        #     return False

    def stop(self):
        self.flag_work = False
        
    def run(self):

        if not self.check():
            return

        self.likes()
        # print( self.lik)
        # self.set_reposts()
        # print( self.reposts)

        arr_action = [
            self.start_page_scroll,
            self.fan_page_scroll,
            self.friends_list_scroll,
            self.friends_page_scroll,
            self.group_page_scroll]


        while self.flag_work:
            print(self.flag_work)
            random.shuffle(arr_action)
            act = arr_action[0]
            if not act():
                self.answer["comment"] = "Где то ошибка"
                self.answer["status"] = "Ошибка"
                return

        # self.answer["output_data"]["reposts"] = self.reposts
        # self.answer["output_data"]["friends"] = self.friends
        # self.answer["output_data"]["groups"] = 0
        # self.answer["output_data"]["likes"]= self.lik

        self.answer["comment"] = "Обновление прошло успешно"
        self.answer["status"] = "Выполнен"
