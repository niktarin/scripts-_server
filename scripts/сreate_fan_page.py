import requests
import time
import os
from .base_tread import Base_tr
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Create_fan_page_tr(Base_tr):

    def run(self):

        if not self.check():
            try:
                self.driver.quit()
            except:
                pass
            return

        xpath = "//a[@id='creation_hub_entrypoint']"
        if not self.click_to_xpath(xpath):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
            return

        xpath = "//li[@class='_54ni _14-r layerHide __MenuItem'][1]"
        if not self.click_to_xpath(xpath):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
            return

        xpath = "//button[@data-testid='NON_BUSINESS_SUPERCATEGORYSelectButton']"
        if not self.click_to_xpath(xpath):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
            return

        xpath = "//input[@id='NON_BUSINESS_SUPERCATEGORYPageNameInput']"
        if not self.set_text(xpath, self.settings["name"]):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
            return (False)

        xpath = "//span[@data-testid='NON_BUSINESS_SUPERCATEGORYCategoryTypeahead']/label/input"
        if not self.set_text(xpath, self.settings["category"]):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
            return (False)

        time.sleep(2)

        xpath = "(//div[@class='_1ith']/button[@class='_271k _271m _1qjd _7tvm _7tv2 _7tv4'])[2]"
        if not self.click_to_xpath(xpath):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
            return

        time.sleep(10)

        
        try:
            xpath = "//div[@class='_29dy']"
            element = self.driver.find_element_by_xpath(xpath)
            if element.is_displayed():
                self.answer["status"] = "Ошибка"
                self.answer["comment"] = "Поля заполнены не правильно"
                self.driver.quit()
                return
        except:
            pass


        if "profile_picture_href" in self.settings:
            self.profile_picture = f"profile_picture_{self.settings['id_scenarios']}.jpg"
            self.profile_picture_href = self.settings["profile_picture_href"]

            try:
                os.remove(self.profile_picture)
            except:
                pass

            p = requests.get(self.profile_picture_href)
            out = open(self.profile_picture, "wb")
            out.write(p.content)
            out.close()


            xpath = "//input[@name='admin_to_do_profile_pic']"
            if self.find_xpath(xpath):
                elem = self.driver.find_element_by_xpath(xpath)
                elem.send_keys(self.profile_picture)
            else:
                pass

            xpath = "//a[text()='Close']"
            if self.find_xpath(xpath, circle=5, time_sleep=1):
                self.click_to_xpath(xpath)
                xpath = "//a[@class='_42ft _4jy0 _4jy3 _517h _51sy']"
                self.click_to_xpath(xpath)


            else:
                pass

        else:
            xpath = "//a[@class='_42ft _4jy0 _4jy3 _517h _51sy']"
            self.click_to_xpath(xpath)

        time.sleep(5)

        if "cover_photo_href" in self.settings:
            self.cover_photo = f"cover_photo_{self.settings['id_scenarios']}.jpg"
            self.cover_photo_href = self.settings["cover_photo_href"]

            try:
                os.remove(self.cover_photo)
            except:
                pass

            p = requests.get(self.cover_photo_href)
            out = open(self.cover_photo, "wb")
            out.write(p.content)
            out.close()

            xpath = "//input[@name='admin_to_do_cover_photo']"
            if self.find_xpath(xpath):
                elem = self.driver.find_element_by_xpath(xpath)
                elem.send_keys(self.cover_photo)
            else:
                pass

            xpath = "//a[text()='Close']"
            if self.find_xpath(xpath, circle=5, time_sleep=1):
                self.click_to_xpath(xpath)
                xpath = "//a[@class='_42ft _4jy0 _4jy3 _517h _51sy']"
                self.click_to_xpath(xpath)
            else:
                pass


            xpath = "(//div[@class='_ohf rfloat'])[last()]"
            if self.find_xpath(xpath, circle=5, time_sleep=1):
                self.click_to_xpath(xpath)
                xpath = "//a[@class='_42ft _4jy0 _4jy3 _517h _51sy']"
                self.click_to_xpath(xpath)
            else:
                pass

        else:
            xpath = "//a[@class='_42ft _4jy0 _4jy3 _517h _51sy']"
            self.click_to_xpath(xpath, circle=5, time_sleep=1)

        step = 0
        while True:
            url = self.driver.current_url.replace("www.","")
            if "modal=admin_todo_tour" in url:
                break
            else:
                step+=1
                time.sleep(1)
            if step >= 30:
                break

        self.driver.refresh()
        self.answer["output_data"]["URL"] = self.driver.current_url.replace("www.","")
        self.answer["output_data"]["name"] = self.settings["name"]
        self.answer["status"] = "Выполнен"
        self.answer["comment"] = f"FP {self.settings['name']} создана"


        self.driver.quit()
