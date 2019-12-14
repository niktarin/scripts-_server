import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from langdetect import detect
from .base_tread_v2 import Base_tr
import random


class Create_bm_tr(Base_tr):
    kiev_ru_streat = ["1-го Мая ул.",
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
    kiev_us_streat = ["Academician Tupolev Str.",
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

    dushanbe_us_streat = [
        "st.January ", "st.Razin", "st.Abay", "st.Rahimiul.Abdulahad Kakhorov", "st.Rahimi", "St.Abdurayhon Beruni",
        "st.Rakhmona Nabiev", " st.Abulkasima Firdousi", " st.Rumi", " st.Avasto",
        "st.Saida Nosiraul.Azizbekovaul.Samad",
        "Ganiul.Aznob", " st.Sahbo", " st.Aini", " St.Sulaimoniul.Academician Akobir Adhamov",
        " st.Sukhrobul.Academician",
        "Dzhabar Rasulov", " st.Temur Malikul.Academician M.Nazarshoev", " st.Tehran", " st.Alisher Navoi",
        " st.Titova",
        "st.Ahmad Donish", " st.Tunisia", " st.Fazlidina Muhammadieva", " st.Barbada",
        " St.Faridaddina Attoraul.Baumana",
        "Foteh Niyoshi", " St.Bach", "St.Khabibullo Nazarova", "st.Behzod"]
    ashgabat_us_streat = ["st.Williams", "St.Tellia", " St.Gagarina", " st.Uspensky", "st.Geologists",
                          " st.Ushakova",
                          "st.Gurban Soltan Ece", " st.Frunze", " st.Gurbannazar Ezizowaul Khudaiberdyeva",
                          "st.Dokuchaev", "st.Chapaevaul Friendship of Peoples",
                          " st.Chekhov", "st.Zelyli", "st.Shevchenko", "st.Karbysheva", "st.Shevchenko",
                          "st.Kurban Durdy",
                          "st.Yunnatovul.Keshi", "st.Yunusa Emreul.Lenin", " Aitakova St.", " St.Leo Tolstoy",
                          "st.Tselinnaya", "st.Mechnikov""Tselinnaya ",
                          "st.Mechnikov", " Tselinnaya", " st.Mira Tselinnaya St.", " st.MRZ Central Street",
                          "st.N.HalmamedovSchorsa",
                          " st.Nakhimova", "Andalyp st.Negina"]
    minsk_us_streat = ["st.Kuhlman", " St.Liberation", " st.Kuntsevschina", " st.Founders", " st.Kupriyanova",
                       "st.Ostrog", " st.Kurchatov", " st.Pavel Shpilevsky", " st.Lazarevaul.Peacocks Myadyalki",
                       "st.Lazo", " st.Pavlovaul.Landera", "st.Pavlovsky", "st.Levkova", " st.Panfilova",
                       "st.Lieutenant",
                       "Kizhevatova", " st.Papanin", " st.Lenin", " st.Parkhomenko", "st.Leonardo da Vinci"]


def run(self):
    try:
        if not self.check_ip_data():
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = "не удалось получить данные об IP"
            return
        self.get_link("https://business.facebook.com/")

        xpath = "//a[@data-testid='business-create-account-button']"
        if not self.click_to_xpath(xpath, appointment="переход на страниу создания bm"):
            if self.accaunt_block_flag:
                self.answer["status"] = "Ошибка"
            else:
                self.answer["status"] = "Ошибка сервера"
            self.answer["comment"] = self.error_comment
            return False

        xpath = "(//input[@class='_4b7k _4b7k_big _53rs'])[2]"
        elem = self.return_el_by_xpath(xpath)
        if elem != None:
            name = elem.get_attribute("value")
            company_name = self.settings["tech_name"] + " " + name
        else:
            company_name = self.settings["tech_name"] + " ----"

        xpath = "(//input[@class='_4b7k _4b7k_big _53rs'])[1]"
        if not self.set_text(xpath, company_name, appointment="название компании"):
            if self.accaunt_block_flag:
                self.answer["status"] = "Ошибка"
            else:
                self.answer["status"] = "Ошибка сервера"
            self.answer["comment"] = self.error_comment
            return

        email_f = self.settings["email_f"]
        email_f = email_f.replace("+", "")
        email_f = email_f.replace(" ", "")

        if email_f.isnumeric():
            email = ["na", "mu", "si", "su", "jo", "ji", "ju", "go", "me", "lo", "we", "ty", "pi", "po", "pa", "li",
                     "lo", "ly"]
            random.shuffle(email)
            email = email[0:5]
            email = "".join(email) + "@gmail.com"
            email_f = email

        xpath = "(//input[@class='_4b7k _4b7k_big _53rs'])[3]"
        if not self.set_text(xpath, email_f, appointment="email"):
            if self.accaunt_block_flag:
                self.answer["status"] = "Ошибка"
            else:
                self.answer["status"] = "Ошибка сервера"
            self.answer["comment"] = self.error_comment
            return

        xpath = "//button[@class='_271k _271m _1qjd _7tvm _7tv2 _7tv4']"
        if not self.click_to_xpath(xpath, appointment="кнопка создания бм"):
            if self.accaunt_block_flag:
                self.answer["status"] = "Ошибка"
            else:
                self.answer["status"] = "Ошибка сервера"
            self.answer["comment"] = self.error_comment
            return False

        time.sleep(10)
        xpath = "//div[@class='_43rm']"
        elem = self.return_el_by_xpath(xpath)
        if elem != None:
            text = elem.text
            qwes = detect(text)
        else:
            if self.accaunt_block_flag:
                self.answer["status"] = "Ошибка"
            else:
                self.answer["status"] = "Ошибка сервера"
            self.answer["comment"] = "Возможо поля формы зполнены не верно"
            return False

        if self.ip_settings["country"] == "RU":

            # if qwes == "ru":
            #     streat = self.moskou_ru_streat
            #     country = "Росси"
            #     city = "Москва"
            #     reg = "Московская область"
            #
            # elif qwes == "uk":
            #     streat = self.moskou_ru_streat
            #     country = "Росі"
            #     city = "Москва"
            #     reg = "Московська область"d
            # else:

            data = [["Tajikistan", "Dushanbe region", "Dushanbe", self.dushanbe_us_streat],
                    ["Turkmenistan", "Ashgabat region", "Ashgabat", self.ashgabat_us_streat],
                    ["Belarus", "Minsk region", "Minsk", self.minsk_us_streat]]
            random.shuffle(data)
            data = data[0]

            country = data[0]
            reg = data[1]
            city = data[2]
            random.shuffle(data[3])
            streat = data[3][0]


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
        else:
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = "Страна прокси не RU/UA"
            return False


        xpath = "//button[@data-testid='SUISearchableSelector/button']"
        if not self.click_to_xpath(xpath, appointment="еще одна кнопка"):
            if self.accaunt_block_flag:
                self.answer["status"] = "Ошибка"
            else:
                self.answer["status"] = "Ошибка сервера"
            self.answer["comment"] = self.error_comment
            return False

        xpath = "//input[@class='_58al']"
        if not self.set_text(xpath, country, appointment="страна"):
            if self.accaunt_block_flag:
                self.answer["status"] = "Ошибка"
            else:
                self.answer["status"] = "Ошибка сервера"
            self.answer["comment"] = self.error_comment
        else:
            self.enter_click(xpath)

        # if self.ip_settings["country"] == "RU":
        #     country = "Russia"
        # elif self.ip_settings["country"] == "UA":
        #     country = "Ukraine"
        # else:
        #     country = "USA"

        random.shuffle(streat)

        street = streat[0]
        xpath = "(//input[@class='_4b7k _4b7k_big _53rs'])[1]"
        if not self.set_text(xpath, street, appointment="улица"):
            if self.accaunt_block_flag:
                self.answer["status"] = "Ошибка"
            else:
                self.answer["status"] = "Ошибка сервера"
            self.answer["comment"] = self.error_comment
            return

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
        if not self.set_text(xpath, city, appointment="город"):
            if self.accaunt_block_flag:
                self.answer["status"] = "Ошибка"
            else:
                self.answer["status"] = "Ошибка сервера"
            self.answer["comment"] = self.error_comment
            return

        xpath = "(//input[@class='_4b7k _4b7k_big _53rs'])[4]"
        if not self.set_text(xpath, reg, appointment="регион"):
            if self.accaunt_block_flag:
                self.answer["status"] = "Ошибка"
            else:
                self.answer["status"] = "Ошибка сервера"
            self.answer["comment"] = self.error_comment
            return

        postcode = f"0{random.randint(7000, 9000)}"
        xpath = "(//input[@class='_4b7k _4b7k_big _53rs'])[5]"
        if not self.set_text(xpath, postcode, appointment="postcode"):
            if self.accaunt_block_flag:
                self.answer["status"] = "Ошибка"
            else:
                self.answer["status"] = "Ошибка сервера"
            self.answer["comment"] = self.error_comment
            return

        ind = ["067", "068", "095", "093", "091", "099"]
        random.shuffle(ind)
        ind = ind[0]
        phone_number = f"+38{ind}{random.randint(1234567, 9999999)}"
        xpath = "(//input[@class='_4b7k _4b7k_big _53rs'])[6]"

        if not self.set_text(xpath, phone_number, appointment="Номер телефона"):
            if self.accaunt_block_flag:
                self.answer["status"] = "Ошибка"
            else:
                self.answer["status"] = "Ошибка сервера"
            self.answer["comment"] = self.error_comment
            return

        site = ["na", "mu", "si", "go", "me", "lo", "we", "ty", "pi", "po", "pa", "li", "lo", "ly"]
        random.shuffle(site)
        site = site[0:3]
        site = "".join(site) + ".com"

        xpath = "(//input[@class='_4b7k _4b7k_big _53rs'])[7]"
        if not self.set_text(xpath, site, appointment="Название сайта"):
            if self.accaunt_block_flag:
                self.answer["status"] = "Ошибка"
            else:
                self.answer["status"] = "Ошибка сервера"
            self.answer["comment"] = self.error_comment
            return False

        xpath = "//button[@class='_271k _271m _1qjd _7tvm _7tv2 _7tv4']"
        if not self.click_to_xpath(xpath, appointment="еще одна кнопка"):
            if self.accaunt_block_flag:
                self.answer["status"] = "Ошибка"
            else:
                self.answer["status"] = "Ошибка сервера"
            self.answer["comment"] = self.error_comment
            return False

        time.sleep(3)

        xpath = "//button[@class='_271k _271m _1qjd _7tvm _7tv2 _7tv4']"
        if not self.click_to_xpath(xpath, appointment="еще одна кнопка"):
            if self.accaunt_block_flag:
                self.answer["status"] = "Ошибка"
            else:
                self.answer["status"] = "Ошибка сервера"
            self.answer["comment"] = self.error_comment
            return False
        time.sleep(60)

        link = "https://www.facebook.com/"
        self.get_link(link)

        xpath = "//div[@id='userNavigationLabel']"
        if not self.click_to_xpath(xpath, appointment="еще одна кнопка"):
            if self.accaunt_block_flag:
                self.answer["status"] = "Ошибка"
            else:
                self.answer["status"] = "Ошибка сервера"
            self.answer["comment"] = self.error_comment
            return False

        xpath = f"//div[@class='navSubmenuName ellipsis' and text()='{company_name}']"
        if self.find_xpath(xpath, time_wait=60):
            self.answer["status"] = "Выполнен"
            self.answer["comment"] = "БМ сдоздан"
        else:
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = "БМ не создан, аккаунт жив!"
    except:
        self.log.log_append(
            {"name": self.tech_name, "action": "error", "text": "Не предвиденная ошибка потока сценария"})
        self.answer["status"] = "Ошибка"
        self.answer["comment"] = "Не предвиденная ошибка потока сценария"
