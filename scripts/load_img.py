import requests
from selenium import webdriver
from scripts.base_tread import Base_tr
import time
from selenium.webdriver.common.keys import Keys
import os
from selenium.webdriver.common.action_chains import ActionChains

class load_img_tr(Base_tr):

    def load_img(self):
        xpath = "(//div[@class='linkWrap noCount'])[1]"
        if not self.click_to_xpath(xpath):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
            return (False)


        time.sleep(5)
        for i in range(3):
            webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
            time.sleep(1)
        self.scroll_page_up(15)
        if "cover_picture_href" in self.settings:
            self.cover_picture = f"cover_picture_{self.settings['tech_name']}.jpg"
            self.cover_picture_href = self.settings["cover_picture_href"]
            try:
                os.remove(self.cover_picture)
            except:
                pass

            p = requests.get(self.cover_picture_href)
            out = open(self.cover_picture, "wb")
            out.write(p.content)
            out.close()


            xpath = "//div[@id='fbProfileCoverPhotoSelector']"
            element_to_hover_over = self.driver.find_element_by_xpath(xpath)
            hover = ActionChains(self.driver).move_to_element(element_to_hover_over)
            hover.perform()

            if not self.click_to_xpath(xpath):
                return (False)


            time.sleep(3)
            elem = self.driver.find_element_by_xpath("//label//div[@class='_3jk']//input")
            elem.send_keys(self.cover_picture)
            time.sleep(10)

            xpath = "//button[@name='save']"
            if not self.click_to_xpath(xpath):
                return (False)

        self.scroll_page_up(15)
        if "face_picture_href" in self.settings:
            self.face_picture = f"face_picture_{self.settings['tech_name']}.jpg"
            self.face_picture_href = self.settings["face_picture_href"]
            try:
                os.remove(self.face_picture)
            except:
                pass

            p = requests.get(self.face_picture_href)
            out = open(self.face_picture, "wb")
            out.write(p.content)
            out.close()

            xpath = "//div[contains(@class, 'fbTimelineProfilePicSelector')]"
            if not self.click_to_xpath(xpath):
                return (False)

            for i in range(40):
                try:
                    elem = self.driver.find_element_by_xpath("//a[@class='_3cia']/div[@class='_3jk']/input[@type='file']")
                    elem.send_keys(self.face_picture)
                    break
                except:
                    time.sleep(1)

            time.sleep(10)

            xpath = "//button[@data-testid='profilePicSaveButton']"
            if not self.click_to_xpath(xpath):
                return (False)


     
        return True

    def run(self):

        if not self.check():
            try:
                self.driver.quit()
            except:
                pass
            return

        for i in range(4):
            webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()

        if not self.load_img():
            self.driver.quit()
            return

        self.answer["status"] = "Выполнен"
        self.answer["comment"] = "Изображения обновленны"
        self.driver.quit()
