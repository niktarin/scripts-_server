import requests
from selenium import webdriver
from .base_tread import Base_tr
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import os

class load_img___fp(Base_tr):

    def load_img(self):

        if "face_picture_fp_href" in self.settings:
            self.face_picture = "face_picture_fp.jpg"
            self.face_picture_href = self.settings["face_picture_href"]
            try:
                os.remove(self.face_picture)
            except:
                pass

            p = requests.get(self.face_picture_href)
            out = open(self.face_picture, "wb")
            out.write(p.content)
            out.close()



            element_to_hover_over = self.driver.find_element_by_id("//a[@aria-label='Profile picture']")
            hover = ActionChains(self.driver).move_to_element(element_to_hover_over)
            hover.perform()


            xpath = "//a[@aria-label='Update menu']"
            if not self.click_to_xpath(xpath):
                self.answer["status"] = "Ошибка"
                self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
                return (False)


            for i in range(40):
                try:
                    elem = self.driver.find_element_by_xpath("//input[@data-testid='profile_picture_upload_menu_item']")
                    elem.send_keys(self.face_picture)
                    break
                except:
                    time.sleep(1)

            time.sleep(10)

            xpath = "//button[@data-testid='profilePicSaveButton']"
            if not self.click_to_xpath(xpath):
                self.answer["status"] = "Ошибка"
                self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
                return (False)



        time.sleep(5)
        for i in range(3):
            webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
            time.sleep(1)
        self.driver.refresh()

        if "cover_picture_fp_href" in self.settings:
            self.cover_picture = "cover_picture_fp.jpg"
            self.cover_picture_href = self.settings["cover_picture_href"]
            try:
                os.remove(self.cover_picture)
            except:
                pass

            p = requests.get(self.cover_picture_href)
            out = open(self.cover_picture, "wb")
            out.write(p.content)
            out.close()

            xpath = "//a[@data-testid='cover_photo_edit_menu']"
            if not self.click_to_xpath(xpath):
                self.answer["status"] = "Ошибка"
                self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
                return (False)


            time.sleep(3)
            elem = self.driver.find_element_by_xpath("//input[@name='simple_video_uploader']")
            elem.send_keys(self.cover_picture)
            time.sleep(10)

            xpath = "//button[@data-testid='cover_photo_save_button']"
            if not self.click_to_xpath(xpath):
                self.answer["status"] = "Ошибка"
                self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
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

        self.driver.get(self.settings["fan_page_href"])

        if not self.load_img():
            self.driver.quit()
            return

        self.answer["status"] = "Выполнен"
        self.answer["comment"] = "Изображения обновленны"
        self.driver.quit()
