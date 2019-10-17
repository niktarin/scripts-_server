from scripts_v2.base_tread_v2 import Base_tr
import random
import time


class static_bot(Base_tr):

    def check_data(self):
        self.login = self.settings["login"]
        self.password = self.settings["password"]
        self.phone_number = self.settings["phone_number"]
        self.data = {"balance": None,
                     "history": {}}

    def login(self):
        if not self.get_link(
                "https://passport.yandex.ru/auth?origin=money&retpath=https%3A%2F%2Fmoney.yandex.ru%2F%3Ffrom%3Dauth"):
            return

        xpath = "//span[@class='passp-account-list__sign-in-button-text']"
        if self.find_xpath(xpath):
            if not self.click_to_xpath(xpath):
                if self.accaunt_block_flag:
                    self.answer["status"] = "Ошибка"
                else:
                    self.answer["status"] = "Ошибка сервера"
                self.answer["comment"] = self.error_comment

        xpath = "//a[@class='control link link_theme_normal passp-current-account passp-current-account_has-display-name']"
        if self.find_xpath(xpath):
            xpath = "//a[@class='control link control_hovered_yes link_hovered_yes link_theme_normal passp-auth-header-link passp-auth-header-link_visible']  "
            if not self.click_to_xpath(xpath):
                if self.accaunt_block_flag:
                    self.answer["status"] = "Ошибка"
                else:
                    self.answer["status"] = "Ошибка сервера"
                self.answer["comment"] = self.error_comment

        xpath = "//div[@class='passp-add-account-page_has-social-block']"
        if not self.set_text(xpath, self.login, appointment="заполнение поля 'логин'"):
            if self.accaunt_block_flag:
                self.answer["status"] = "Ошибка"
            else:
                self.answer["status"] = "Ошибка сервера"
            self.answer["comment"] = self.error_comment
            return False
        else:
            self.enter_click(xpath)

        xpath = "//input[@id='passp-field-passwd']"
        if not self.set_text(xpath, self.password, appointment="заполнение поля 'пароль'"):
            if self.accaunt_block_flag:
                self.answer["status"] = "Ошибка"
            else:
                self.answer["status"] = "Ошибка сервера"
            self.answer["comment"] = self.error_comment
            return False
        else:
            self.enter_click(xpath)

        xpath = "//input[@class='p-control__input_name_challenge p-control_challenge-phone']"
        if self.find_xpath(xpath, time_wait=10):
            if not self.set_text(xpath, self.phone_number, appointment="заполнение поля 'номер телефона'"):
                if self.accaunt_block_flag:
                    self.answer["status"] = "Ошибка"
                else:
                    self.answer["status"] = "Ошибка сервера"
                self.answer["comment"] = self.error_comment
                return False
            else:
                self.enter_click(xpath)

        xpath = "//a[@class='control button2 button2_view_classic button2_size_l button2_theme_normal button2_type_link registration__avatar-btn']  "
        if self.find_xpath(xpath):
            if not self.click_to_xpath(xpath, appointment="скипнуть заливку картинки"):
                if self.accaunt_block_flag:
                    self.answer["status"] = "Ошибка"
                else:
                    self.answer["status"] = "Ошибка сервера"
                self.answer["comment"] = self.error_comment

        xpath = "//button[@class='control button2 button2_view_classic button2_size_l button2_theme_action button2_width_max button2_type_submit passp-form-button']"
        if self.find_xpath(xpath):
            if not self.click_to_xpath(xpath, appointment="скипнуть заливку картинки"):
                if self.accaunt_block_flag:
                    self.answer["status"] = "Ошибка"
                else:
                    self.answer["status"] = "Ошибка сервера"
                self.answer["comment"] = self.error_comment

        self.get_link("https://money.yandex.ru/actions?_openstat=template%3Bimenu%3Bactions")

    def get_data(self):

        xpath = "//div[@class='get-more visibility visibility_hidden_yes history-item-list__get-more i-bem get-more_js_inited]"
        while True:
            if self.find_xpath(xpath):
                self.click_to_xpath(xpath)
                time.sleep(2)
            else:
                break

        xpath = "(//span[@class='price__whole-amount text text_size_xxxxl text_view_primary text_weight_regular'])[1]"
        elem = self.return_el_by_xpath(xpath)
        if elem != None:
            whole = elem.text
        else:
            whole = "--"

        xpath = "//span[@class='price__decimal-separator text text_size_xxxxl text_view_primary text_weight_regular']"
        elem = self.return_el_by_xpath(xpath)
        if elem != None:
            separator = elem.text
        else:
            separator = ","

        xpath = "//span[@class='price__label text text_size_xxxxl text_view_primary text_weight_light']"
        elem = self.return_el_by_xpath(xpath)
        if elem != None:
            decimal = elem.text
        else:
            decimal = "--"

        xpath = "//span[@class='price__label text text_size_xxxxl text_view_primary text_weight_light'] "
        elem = self.return_el_by_xpath(xpath)
        if elem != None:
            valut = elem.text
        else:
            valut = "-"

        self.data["balance"] = whole + separator + decimal + valut

        xpath = "//div[@class='payment-history-item__wrap-border']"
        elements = self.driver.find_elements_by_xpath(xpath)
        lenght = len(elements)
        for i in range(lenght):
            arr_data = {}
            index = i + 1
            xpath = f"(//p[@class='payment-history-item__text'])[{index}]"
            elem = self.return_el_by_xpath(xpath)
            arr_data["name"] = elem.text

            xpath = f"(//p[@class='payment-history-item__text'])[{index}]/../../div/span[@class='price price_absolute_yes']/.."
            elem = self.return_el_by_xpath(xpath)
            znak = elem.text

            xpath = f"(//p[@class='payment-history-item__text'])[{index}]/../../div/span[@class='price price_absolute_yes']/span/span[@class='price__whole-amount']"
            elem = self.return_el_by_xpath(xpath)
            whole = elem.text

            xpath = f"(//p[@class='payment-history-item__text'])[{index}]/../../div/span[@class='price price_absolute_yes']/span/span[@class='price__decimal-separator']"
            el = self.return_el_by_xpath(xpath)
            if el != None:
                separator = elem.text
            else:
                separator = ""

            xpath = f"(//p[@class='payment-history-item__text'])[{index}]/../../div/span[@class='price price_absolute_yes']/span/span[@class='price__decimal-amount']"
            el = self.return_el_by_xpath(xpath)
            if el != None:
                decimal = elem.text
            else:
                decimal = ""

            arr_data["value"] = znak + whole + separator + decimal

            xpath = f"(//p[@class='payment-history-item__text'])[{index}]/../../div/span[@class='payment-render payment-render_type_date']"
            elem = self.return_el_by_xpath(xpath)
            arr_data["date"] = elem.text

            xpath = "(//p[@class='payment-history-item__text'])[1]/../../div/span[@class='payment-render payment-render_type_date']/span[@class='payment-render__comment']"
            elem = self.return_el_by_xpath(xpath)
            arr_data["time"] = elem.text

            self.data["history"][index] = arr_data.copy()
            del arr_data

    def run(self):
        try:
            self.check_data()
            self.login()
            self.get_data()

            print(self.data)

            self.answer["comment"] = "Данные об кошельке получены"
            self.answer["status"] = "Выполнен"
        except:
            self.log.log_append(
                {"name": self.tech_name, "action": "error", "text": "Не предвиденная ошибка потока сценария"})
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = "Не предвиденная ошибка потока сценария"
