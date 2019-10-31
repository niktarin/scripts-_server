from .base_tread import Base_tr
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import base64
import time
import os
import requests

class Set_posts_tr(Base_tr):

    def get_files(self):
        try:

            if "text" in self.settings:
                self.text = self.settings["text"]
            else:
                self.text = None

            if "link" in self.settings:
                self.link = self.settings["link"]
            else:
                self.link = None

            if "img" in self.settings:
                self.img_href = self.settings["img"]

                try:
                    os.remove("img_for_post.jpg")
                except :
                    pass

                p = requests.get(self.img_href)
                out = open("img_for_post.jpg", "wb")
                out.write(p.content)
                out.close()
                self.img_name = "img_for_post.jpg"
            else:
                self.img_name = None


            return (True)
        except:
            return(False)

    def set_post(self):
    	
        xpath = "//div[@aria-label='Create a post'] "
        if not self.click_to_xpath(xpath, circle=60, time_sleep=1):
            self.answer["comment"] = f"Время исчерпано не удалось найти {xpath}"
            self.answer["status"] = "Ошибка"
            return (False)


        circle = 0
        while True:
            elem = self.driver.find_element_by_xpath("//div[@class='_3u15']")
            size = elem.size
            circle +=1

            if circle >= 20:
                self.answer["comment"] = f"Время исчерпано не удалось отобразить //div[@class='_3u15']"
                self.answer["status"] = "Ошибка"
                return (False)

            if size["width"] == 0 or size["height"] == 0:
                time.sleep(1)
                continue
            else:
                break


        try:

            if self.text != None:
                data = self.text.replace("\n", " ")
                if data.replace(" ", "") != "":
                    webdriver.ActionChains(self.driver).send_keys(data).perform()
                webdriver.ActionChains(self.driver).send_keys(Keys.ENTER).perform()


            if self.link != None:
                link = self.link.replace("\n", "")
                if link.replace(" ","") != "":
                    webdriver.ActionChains(self.driver).send_keys(link).perform()
                    webdriver.ActionChains(self.driver).send_keys(Keys.ENTER).perform()
                    for i in range(len(link)+1):
                        webdriver.ActionChains(self.driver).send_keys(Keys.BACK_SPACE).perform()



            time.sleep(3)
            if self.img_name != None:
                elemets = self.driver.find_elements_by_xpath("//input[@data-testid='media-sprout']")
                if len(elemets)>0:
                    elemets[0].send_keys(self.img_name)
                    time.sleep(15)
                else:
                    xpath = "(//ul[@data-testid='collapsed_sprouts']//li)[1]"
                    self.click_to_xpath(xpath)
                    time.sleep(3)
                    xpath = "//div[@data-testid='photo-video-button']"
                    self.click_to_xpath(xpath)
                    time.sleep(3)

                    try:
                        elem = self.driver.find_element_by_xpath("//input[@data-testid='media-attachment-add-photo']")
                        elem.send_keys(self.img_name)
                        time.sleep(15)
                    except:
                        pass

            try:
                elem = self.driver.find_element_by_xpath("//button[@data-testid='react-composer-post-button']")
                elem.click()
            except:
                pass

        except:
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = f"Ошибка при попытки сделать комментарий"
            return (False)
        time.sleep(10)
        return (True)

    def to_fan_pages(self):

        if "fan_pages" not in self.settings:
            return (True)

        for fan_page in self.settings["fan_pages"]:
            fan_page.replace(" ", "")
            if fan_page == "":
                continue
            if self.settings["biznes"] == "True" :
                fan_page = "business." + fan_page

            try:
                self.driver.get(fan_page)
                if not self.set_post():
                    return (False)
            except:
                self.answer["comment"] = f"Не удалось перейти на файн пейдж {fan_page}"
                self.answer["status"] = "Ошибка"
                return (False)

        return (True)

    def to_standart_page(self):
        xpath = "//span[@class='_2md']"
        if not self.click_to_xpath(xpath):
            self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
            self.answer["status"] = "Ошибка"
            return (False)

        time.sleep(1)
        xpath = "//div[@data-click='profile_icon']//a"
        if not self.click_to_xpath(xpath):
            self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
            self.answer["status"] = "Ошибка"
            return (False)
        time.sleep(1)
        return (self.set_post())

    def run(self):
        if not self.check():
            return

        if not self.get_files():
            self.answer["comment"] = "Не удалось получить данные для поста"
            self.answer["status"] = "Ошибка"
            self.driver.quit()
            return

        for i in range(4):
            webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()

        if "start_page" in  self.settings:
            if self.settings["start_page"]:
                if not self.to_standart_page():
                    self.driver.quit()
                    return

        if not self.to_fan_pages():

            self.driver.quit()
            return

        self.answer["comment"] = "Пост сделан"
        self.answer["status"] = "Выполнен"

