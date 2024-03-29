import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from langdetect import detect
from .base_tread import Base_tr
import random

class Create_bm_tr(Base_tr):
    kiev_ru_streat =["1-го Мая ул.",
                        "1-й Полевой переулок",
                        "1-я Софиевская улица ныне часть Валерия Лобановского проспект",
                        "2-й Казарменный переулок см. Бакинская улица",
                        "2-я Тростянецкая улица (1989-90) см. Анны Ахматовой улица",
                        "3-го Интернационала площадь см. Европейская площадь",
                        "8 Марта ул.",
                        "6-я линия см. Архитектора Кобелева улица",
                        "7-я линия см. Архитектора Кобелева улица",
                        "9 января улица (1925-44) см. Багговутовская улица",
                        "9 Мая ул.",
                        "40-летия Октября проспект см. Голосеевский проспект",
                        "50-летия Октября проспект см. Леся Курбаса проспект",
                        "40-я Новая улица см. Армейская улица",
                        "63-я Новая улица см. Эстонский переулок"]

    kiev_us_streat =[ "Academician Tupolev Str.",    
                        "Academician Zabolotny Str.",   
                        "Adam Mickiewicz Street.",
                        "Admiral Ushakov Str.",  
                        "Aerodrome Street.",  
                        "Aggregate street. ", 
                        "Aistova street. ", 
                        "Aivazovsky pen.",  
                        "Akhtyrskaya street. ",    
                        "Alder Street."]

    moskou_ru_streat = [
                            "Библиотечная улица",
                            "Библиотечный проезд",
                            "Биржевая площадь",
                            "Бирюлёвская улица",
                            "Бирюсинка, улица",
                            "Благовещенский переулок",
                            "Благуша, улица",
                            "Бобров переулок",
                            "Бобруйская улица",
                            "Богатырская 3-я, улица",
                            "Богатырский 2-й, переулок",
                            "Богатырский Мост, улица"] 

    moskou_us_streat = [
                            "1st khodinskiy fare",
                            "1st line Horoshёvskogo Serebryany Bor",
                            "1st Northern Line",
                            "1st Smolensky Pereulok",
                            "1st Street Park",
                            "2nd khodinskiy fare",
                            "2nd line Horoshёvskogo Serebryany Bor",
                            "2nd Northern Line",
                            "2nd Paveletsky passage",
                            "2nd Street Park",
                            "3rd khodinskiy fare",
                            "3rd line Horoshёvskogo Serebryany Bor",
                            "3rd Northern Line",
                            "3rd Street Park",
                            "4th khodinskiy fare",
                            "4th line Horoshёvskogo Serebryany Bor",
                            "4th Northern Line",
                            "4th Street Park",
                            "5th Northern Line",
                            "5th Street Park"] 


    def run(self):

        
        if not self.check():
            try:
                self.driver.quit()
            except:
                pass
            return

        self.check_ip_data()
        # xpath = "//div[@data-click='profile_icon']//a/span/span"
        # elem = self.driver.find_element_by_xpath(xpath)
        # name = elem.text

        self.driver.get("https://business.facebook.com/")


        xpath = "//a[@data-testid='business-create-account-button']"
        if not self.click_to_xpath(xpath):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
            return

        xpath = "(//input[@class='_4b7k _4b7k_big _53rs'])[2]"
        elem = self.driver.find_element_by_xpath(xpath)
        name = elem.get_attribute("value")
        company_name = self.settings["tech_name"]+ " "+ name

        xpath = "(//input[@class='_4b7k _4b7k_big _53rs'])[1]"
        if not self.set_text(xpath, company_name):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
            return (False)

        # xpath = "(//input[@class='_4b7k _4b7k_big _53rs'])[2]"
        # if not self.set_text(xpath, name):
        #     self.answer["status"] = "Ошибка"
        #     self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
        #     return (False)

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

        # xpath = "//button[@data-testid='SUISearchableSelector/button']"
        # if not self.click_to_xpath(xpath):
        #     self.answer["status"] = "Ошибка"
        #     self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
        #     return


        xpath = "//div[@class='_43rm']"
        elem = self.driver.find_element_by_xpath(xpath)
        text = elem.text
        qwes = detect(text)

        if self.ip_settings["country"] == "RU":

            if qwes == "ru":
                streat = self.moskou_ru_streat
                country = "Росси"
                city = "Москва"
                reg = "Московская область"

            elif qwes == "uk":
                streat = self.moskou_ru_streat
                country = "Росі"
                city = "Москва"
                reg = "Московська область"
            else:
                streat = self.moskou_us_streat
                country = "Russia"
                city = "Moscow"
                reg = "Moscow region"

        elif self.ip_settings["country"] == "UA":

            if qwes == "ru":
                streat = self.kiev_ru_streat
                country = "Украина"
                city = "Киев"
                reg = "Киевская ообласть"

            elif qwes == "uk":
                streat = self.kiev_ru_streat
                country = "Україн"
                city = "Київ"
                reg = "Київська область"
            else:
                streat = self.kiev_us_streat
                country = "Ukrain"
                city = "Kiev"
                reg = "Kiev region"

        xpath = "//button[@data-testid='SUISearchableSelector/button']"
        if not self.click_to_xpath(xpath):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
            return

        xpath = "//input[@class='_58al']"
        if not self.set_text(xpath, country):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
            return (False)

        webdriver.ActionChains(self.driver).send_keys(Keys.ENTER).perform()

        # if self.ip_settings["country"] == "RU":
        #     country = "Russia"
        # elif self.ip_settings["country"] == "UA":
        #     country = "Ukraine"
        # else:
        #     country = "USA"
      
        random.shuffle(streat)

        street = streat[0]
        xpath = "(//input[@class='_4b7k _4b7k_big _53rs'])[1]"
        if not self.set_text(xpath, street):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
            return (False)

        # xpath = "(//input[@class='_4b7k _4b7k_big _53rs'])[1]"
        # if not self.set_text(xpath, self.settings["address_f"]):
        #     self.answer["status"] = "Ошибка"
        #     self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
        #     return (False)

        # xpath = "(//input[@class='_4b7k _4b7k_big _53rs'])[2]"
        # if not self.set_text(xpath, self.settings["address_s"]):
        #     self.answer["status"] = "Ошибка"
        #     self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
        #     return (False)

        xpath = "(//input[@class='_4b7k _4b7k_big _53rs'])[3]"
        if not self.set_text(xpath, city):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
            return (False)

        xpath = "(//input[@class='_4b7k _4b7k_big _53rs'])[4]"
        if not self.set_text(xpath, reg):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
            return (False)

        postcode = f"0{random.randint(7000,9000)}"
        xpath = "(//input[@class='_4b7k _4b7k_big _53rs'])[5]"
        if not self.set_text(xpath, postcode):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
            return (False)

        ind = ["067","068","095","093","091","099"]
        random.shuffle(ind)
        ind = ind[0]
        phone_number =  f"+38{ind}{random.randint(1234567,9999999)}"
        xpath = "(//input[@class='_4b7k _4b7k_big _53rs'])[6]"
        if not self.set_text(xpath, phone_number):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
            return (False)

        site = ["na","mu","si","go","me","lo","we","ty","pi","po","pa","li","lo","ly"]
        random.shuffle(site)
        site = site[0:3]
        site = "".join(site)+".com"


        xpath = "(//input[@class='_4b7k _4b7k_big _53rs'])[7]"
        if not self.set_text(xpath, site):
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
