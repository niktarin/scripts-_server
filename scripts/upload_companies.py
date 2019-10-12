import base64
import time
from .base_tread import Base_tr
import os

class Create_fan_page_tr(Base_tr):

    def run(self):

        if not self.check():
            try:
                self.driver.quit()
            except:
                pass
            return

        self.driver.get("business.facebook.com/adsmanager/manage/all")
        xpath = "_42d_ _32qq _3n5r layerCancel"
        self.click_to_xpath(xpath)

        xpath = "//button[@data-tooltip-content='Export & Import'] "
        if not self.click_to_xpath(xpath):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
            return

        xpath = "//span[text()='Ads']"
        if not self.click_to_xpath(xpath):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
            return


        file_b = self.settings["file_bytes"]
        file_name = "companies_setttings.csv"
        f = open(file_name, 'wb')
        f.write(file_b)
        f.close()
        xpath = "//input[@data-testid='import-paste-text-link']"
        elem = self.driver.find_element_by_xpath(xpath)
        elem.send_keys(file_name)

        time.sleep(3)

        xpath = "//button[@data-testid='import-button'] "
        if not self.click_to_xpath(xpath):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
            return

        self.answer["status"] = "Выполнен"
        self.answer["comment"] = "Компании загруженны"
        self.driver.quit()