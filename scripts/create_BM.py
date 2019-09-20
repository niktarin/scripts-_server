import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from base_tread import Base_tr


class Create_fan_page_tr(Base_tr):

    def run(self):

        if not self.check():
            try:
                self.driver.quit()
            except:
                pass
            return
        self.driver.get("business.facebook.com")

        xpath = "//a[@data-testid='business-create-account-button']"
        if not self.click_to_xpath(xpath):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
            return


        xpath = "(//input[@class='_4b7k _4b7k_big _53rs'])[1]"
        if not self.set_text(xpath, self.settings["company_name"]):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
            return (False)

        xpath = "(//input[@class='_4b7k _4b7k_big _53rs'])[2]"
        if not self.set_text(xpath, self.settings["my_name"]):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
            return (False)

        xpath = "(//input[@class='_4b7k _4b7k_big _53rs'])[3]"
        if not self.set_text(xpath, self.settings["email"]):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
            return (False)

        xpath = "//button[@class='_271k _271m _1qjd _7tvm _7tv2 _7tv4']"
        if not self.click_to_xpath(xpath):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
            return


        xpath = "//button[@data-testid='SUISearchableSelector/button']"
        if not self.click_to_xpath(xpath):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
            return


        xpath = "//input[@class='_58al']"
        if not self.set_text(xpath, self.settings["country"]):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
            return (False)

        webdriver.ActionChains(self.driver).send_keys(Keys.ENTER).perform()

        xpath = "(//input[@class='_4b7k _4b7k_big _53rs'])[1]"
        if not self.set_text(xpath, self.settings["house"]):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
            return (False)

        xpath = "(//input[@class='_4b7k _4b7k_big _53rs'])[1]"
        if not self.set_text(xpath, self.settings["address_f"]):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
            return (False)

        xpath = "(//input[@class='_4b7k _4b7k_big _53rs'])[2]"
        if not self.set_text(xpath, self.settings["address_s"]):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
            return (False)

        xpath = "(//input[@class='_4b7k _4b7k_big _53rs'])[3]"
        if not self.set_text(xpath, self.settings["city"]):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
            return (False)

        xpath = "(//input[@class='_4b7k _4b7k_big _53rs'])[4]"
        if not self.set_text(xpath, self.settings["region"]):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
            return (False)

        xpath = "(//input[@class='_4b7k _4b7k_big _53rs'])[5]"
        if not self.set_text(xpath, self.settings["postcode"]):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
            return (False)

        xpath = "(//input[@class='_4b7k _4b7k_big _53rs'])[6]"
        if not self.set_text(xpath, self.settings["phone_number"]):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
            return (False)

        xpath = "(//input[@class='_4b7k _4b7k_big _53rs'])[7]"
        if not self.set_text(xpath, self.settings["site"]):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
            return (False)

        xpath = "//button[@class='_271k _271m _1qjd _7tvm _7tv2 _7tv4']"
        if not self.click_to_xpath(xpath):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
            return

        time.sleep(3)

        xpath = "//button[@class='_271k _271m _1qjd _7tvm _7tv2 _7tv4']"
        if not self.click_to_xpath(xpath):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
            return

        self.answer["status"] = "Выполнен"
        self.answer["comment"] = "BM сдоздан"
        self.driver.quit()
