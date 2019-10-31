from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from .base_tread import Base_tr
import random
import time

class Updata_fb_tr(Base_tr):

    def start_page_scroll(self):

        xpath = "//span[@class='_2md']"
        if not self.click_to_xpath(xpath):
            self.answear["status"] = "Ошибка"
            self.answear["comment"] = f"Время исчерпано, не удалось найти {xpath}"
            return (False)

        if not self.scroll_page_down():
            self.answear["status"] = "Ошибка"
            self.answear["comment"] = f"Время исчерпано, не удалось прокрутить стартовую страницу"
            return (False)
        return (True)

    def likes(self):

        if not self.start_page_scroll():
            return (False)

        try:
            xpath = "//span[@class='_1mto']/div[@class='_khz _4sz1 _4rw5 _3wv2']/a"
            elements_1 = self.driver.find_elements_by_xpath(xpath)

            xpath = "//div[@data-testid='UFI2ReactionLink/actionLink']/div/a"
            elements_2 = self.driver.find_elements_by_xpath(xpath)

            lenght_1 = len(elements_1)
            lenght_2 = len(elements_2)

            elements = elements_1 if lenght_1 >= lenght_2 else elements_2
            lenght = lenght_1 if lenght_1 >= lenght_2 else lenght_2

            maximum = self.settings["likes_max"]
            minimum = self.settings["likes_min"]

            maximum = maximum if maximum < lenght else lenght
            minimum = minimum if minimum < lenght else lenght

            if maximum < minimum:
                minimum, maximum = maximum, minimum

            likes = random.randint(minimum, maximum)
            likes = likes if likes < len(elements) else len(elements)
            random.shuffle(elements)

            self.lik = 0

            while self.lik <= likes and len(elements) > 0:
                element = elements[0]
                if self.click_to_element(element):
                    del elements[0]
                    self.lik += 1
                else:
                    del elements[0]
                    continue

            return True

        except:
            self.answear["status"] = "Ошибка"
            self.answear["comment"] = "Не удалось поставить лайки"
            return (False)

    def set_reposts(self):

        xpath = "//span[@class='_2md']"
        if not self.click_to_xpath(xpath):
            self.answear["status"] = "Ошибка"
            self.answear["comment"] = f"Время исчерпано, не удалось найти {xpath}"
            return (False)

        if not self.scroll_page_down():
            self.answear["status"] = "Ошибка"
            self.answear["comment"] = f"Время исчерпано, не удалось найти {xpath}"
            return (False)

        time.sleep(2)
        try:
            xpath = "//span[@class='_1mto']/span[@class='_27de _4noj']/.."
            elements_1 = self.driver.find_elements_by_xpath(xpath)

            xpath = "//span[@class='_18vi']/span[@class='_1j6m']"
            elements_2 = self.driver.find_elements_by_xpath(xpath)

            lenght_1 = len(elements_1)
            lenght_2 = len(elements_2)

            elements = elements_1 if lenght_1 >= lenght_2 else elements_2
            random.shuffle(elements)

            lenght = lenght_1 if lenght_1 >= lenght_2 else lenght_2

            maximum = self.settings["repost_max"]
            minimum = self.settings["repost_min"]

            maximum = maximum if maximum < lenght else lenght
            minimum = minimum if minimum < lenght else lenght

            reposts = random.randint(minimum, maximum)
            self.reposts = 0
        except:
            self.answear["status"] = "Ошибка"
            self.answear["comment"] = f"Ошибка repost_settings"
            return (False)
        try:
            while self.reposts <= reposts and len(elements) > 0:
                element_rep = elements[0]
                del elements[0]

                summ = 0
                while summ < 10:
                    try:
                        element_rep.click()
                        break
                    except:
                        summ += 1
                        time.sleep(1)

                xpath = "//button[@data-testid='react_share_dialog_post_button']"
                if not self.click_to_xpath(xpath):
                    xpath = f"(//li[@class='_54ni _2al8 __MenuItem']/a/span/span[@class='_54nh'])[last()]"
                    self.click_to_xpath(xpath)

                    xpath = "//button[@data-testid='react_share_dialog_post_button'] "
                    self.click_to_xpath(xpath)

            return (True)
        except:
            self.answear["status"] = "Ошибка"
            self.answear["comment"] = f"Ошибка при репостах"
            return (False)

    def add_friends(self):
        xpath = "//span[@class='_2md']"
        if not self.click_to_xpath(xpath):
            self.answear["status"] = "Ошибка"
            self.answear["comment"] = f"Время исчерпано, не удалось найти {xpath}"
            return (False)

        xpath = "(//div[@class='linkWrap noCount'])[1]"
        if not self.click_to_xpath(xpath):
            self.answear["status"] = "Ошибка"
            self.answear["comment"] = f"Время исчерпано, не удалось найти {xpath}"
            return (False)

        xpath = "//div[@id='fbTimelineHeadline']/div/ul/li[3]/a"
        if not self.click_to_xpath(xpath):
            self.answear["status"] = "Ошибка"
            self.answear["comment"] = f"Время исчерпано, не удалось найти {xpath}"
            return (False)

        xpath = "//a[@href='/find-friends/browser/']"
        if not self.click_to_xpath(xpath):
            self.answear["status"] = "Ошибка"
            self.answear["comment"] = f"Время исчерпано, не удалось найти {xpath}"
            return (False)

        try:
            time.sleep(10)
            xpath = "(//button[@class='_42ft _4jy0 FriendRequestAdd addButton _4jy3 _4jy1 selected _51sy'])[position()>13]"
            elements_1 = self.driver.find_elements_by_xpath(xpath)

            xpath = "(//button[@class='_42ft _4jy0 _4jy3 _4jy1 selected _51sy'])[position()>13]"
            elements_2 = self.driver.find_elements_by_xpath(xpath)

            lenght_1 = len(elements_1)
            lenght_2 = len(elements_2)

            elements = elements_1 if lenght_1 >= lenght_2 else elements_2
            random.shuffle(elements)

            lenght = lenght_1 if lenght_1 >= lenght_2 else lenght_2

            maximum = self.settings["friends_add_max"]
            minimum = self.settings["friends_add_min"]

            maximum = lenght if maximum > lenght else maximum
            minimum = lenght if minimum > lenght else minimum

            f_r = random.randint(minimum, maximum)
            self.friends = 0
            while self.friends < f_r and len(elements) > 0:
                element = elements[0]
                del elements[0]

                if self.click_to_element(element):
                    self.friends += 1

            return (True)
        except:
            self.answear["status"] = "Ошибка"
            self.answear["comment"] = f"Ошибка при добавлении друзей"
            return (False)

    def add_groups(self):
        xpath = "//span[@class='_2md']"
        if not self.click_to_xpath(xpath):
            self.answear["status"] = "Ошибка"
            self.answear["comment"] = f"Время исчерпано, не удалось найти {xpath}"
            return (False)

        xpath = "//a[@href='/groups/?ref=bookmarks']"
        if not self.click_to_xpath(xpath):
            xpath = "//div[@class='linkWrap noCount' and text()='Groups']"
            if not self.click_to_xpath(xpath):
                self.answear["status"] = "Ошибка"
                self.answear["comment"] = f"Время исчерпано, не удалось найти {xpath}"
                return (False)

        time.sleep(3)


        xpath = "//div[@class='_43rm']"
        elements = self.driver.find_elements_by_xpath(xpath)
        random.shuffle(elements)
        maximum = self.settings["groups_max"]
        minimum = self.settings["groups_min"]

        g_r = random.randint(minimum, maximum)
        self.groups = 0

        circl_max = 0

        while self.groups < g_r and circl_max <20:

            element = elements[0]
            flag = self.click_to_element(element)
            del elements[0]
            time.sleep(3)
            xp = "//div[@class='_4t2a']"
            ele = self.driver.find_elements_by_xpath(xp)
            if ele != []:
                flag = False
                self.driver.refresh()

            t = "//div[@data-testid='exception_dialog']"
            p = self.driver.find_elements_by_xpath(t)
            if p != []:
                flag = False
                webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
                self.driver.refresh()


            circl_max += 1
            if flag:
                self.groups += 1
            else:
                self.scroll_page_down(down=30)
                xpath = "//div[@class='_43rm']"
                elements = self.driver.find_elements_by_xpath(xpath)
                random.shuffle(elements)

    def fan_page_scroll(self):
        for link in self.settings["fan_pages"]:
            link.replace(" ","")
            if link == "":
                continue

            self.driver.get(link)
            down = random.randint(50, 300)
            self.scroll_page_down(down)
            self.scroll_page_up(down)

        return (True)

    def run(self):

        if not self.check():
            try:
                self.driver.quit()
            except:
                pass
            return

        arr_action = [
            self.start_page_scroll,
            self.likes,
            self.set_reposts,
            self.add_friends,
            self.fan_page_scroll,
            self.add_groups
        ]

        random.shuffle(arr_action)

        for act in arr_action:
            if not act():
                self.driver.quit()
                return

        self.answear["output_data"]["reposts"] = self.reposts
        self.answear["output_data"]["friends"] = self.friends
        self.answear["output_data"]["groups"] = 0
        self.answear["output_data"]["likes"]= self.lik

        self.answear["comment"] = "Обновление прошло успешно"
        self.answear["status"] = "Выполнен"
        self.driver.quit()
