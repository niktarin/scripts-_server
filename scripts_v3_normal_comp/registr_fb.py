import json
import random
import time
import os
from selenium.webdriver.common.action_chains import ActionChains
from .base_tread_v3 import Base_tr


class Registr_fb_tr(Base_tr):

    def giv_name(self):
        try:
            self.driver.get("http://ipinfo.io/json")
            el = self.driver.find_element_by_xpath("//pre")
            settings = json.loads(el.text)
            self.country = settings["country"]
            if self.country == "UA":

                last_name = [
                    "Ковалэнко",
                    "Бондарэнко",
                    "Злэнко",
                    "Саенко",
                    "Семеночко",
                    "Шумэйко",
                    "Мацэйко",
                    "Ламэйко",
                    "Бутэйко",
                    "Потебэнько",
                    "Опэнько",
                    "Витребэнько",
                    "Галаенко",
                    "Мотриенко",
                    "Стратиенко",
                    "Петрэнко",
                    "Павлэнко",
                    "Шевчэнко",
                    "Евэнко",
                    "Майстрэнко"]
                random.shuffle(last_name)

                first_name = [
                    "Агрипина",
                    "Ада",
                    "Аделаїда",
                    "Аделіна",
                    "Адріана",
                    "Богдана",
                    "Богуслава",
                    "Болеслава",
                    "Вероніка",
                    "Вікторина",
                    "Вікторія",
                    "Віола",
                    "Віолетта",
                    "Георгіна",
                    "Глафіра",
                    "Гликерія",
                    "Євлалія",
                    "Євлампія",
                    "Євпраксія",
                    "Єлизавета",
                    "Єпистима",
                    "Інга",
                    "Інеса",
                    "Інна",
                    "Іраїда",
                    "Кароліна",
                    "Катерина",
                    "Кіра",
                    "Клавдія",
                    "Клара",
                    "Клементина",
                    "Корнелія",
                    "Ліліана",
                    "Лілія",
                    "Ліна",
                    "Лія",
                    "Лукерія",
                    "Лукія",
                    "Меланія",
                    "Мелетія",
                    "Мелітина",
                    "Милана",
                    "Милослава",
                    "Сільвія",
                    "Сніжана",
                    "Соломія",
                    "Софія",
                    "Станіслава",
                    "Стелла"

                ]
                random.shuffle(first_name)

            elif self.country == "RU":
                first_name = ["Агафья",
                              "Агриппина",
                              "Акулина",
                              "Алевтина",
                              "Александра",
                              "Алина",
                              "Алла",
                              "Анастасия",
                              "Ангелина",
                              "Анжела",
                              "Анжелика",
                              "Анна",
                              "Антонина",
                              "Валентина",
                              "Валерия",
                              "Варвара",
                              "Иоанна",
                              "Ираида",
                              "Ирина",
                              "Зинаида",
                              "Злата",
                              "Зоя",
                              "Маргарита",
                              "Марина",
                              "Мария",
                              "Марфа",
                              "Матрёна",
                              "Мирослава"]

                random.shuffle(first_name)
                last_name = [
                    "Амурская",
                    "Ангельская",
                    "Анненская",
                    "Афанасьева",
                    "Афинская",
                    "Бабочкина",
                    "Багирова",
                    "Баженова",
                    "Белоградская",
                    "Белозёрская",
                    "Березина",
                    "Беркутова",
                    "Благовещенская",
                    "Богословская",
                    "Бриллиантова",
                    "Василькова",
                    "Византийская",
                    "Воскресенская",
                    "Гиацинтова",
                    "Гончарова",
                    "Городецкая",
                    "Залесская",
                    "Елисеева",
                    "Златовласова",
                    "Златопольская",
                    "Знаменская",
                    "Зорина",
                    "Игнатьева",
                    "Истомина",
                    "Каменская",
                    "Колосовская",
                    "Лаврентьева",
                    "Луговая",
                    "Лучинская",
                    "Майская",
                    "Малиновская",
                    "Нагорная",
                    "Никитина",
                    "Озерова",
                    "Островская",
                    "Рассказова",
                    "Родионова",
                    "Рябинина",
                    "Румянцева",
                    "Сапфирова",
                    "Серебрянская",
                    "Солнцева",
                    "Ушанская",
                    "Цветкова",

                ]

                random.shuffle(last_name)

            else:
                first_name = ["Adriana", "Ada", "Abby", "Adrianne", "Aimee", "Beth", "Catherine", "Cathy", "Cheryl",
                              "ringo", "Jamie", "nicky", "Diane", "Donna", "trudie", "Esther", "lauren",
                              "ichabod", "arthur", "ashley", "Fiona", "julio", "lorraine", "floyd", "janet",
                              "lydia", "Irene", "Jasmine", "bradley"]
                random.shuffle(first_name)

                last_name = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller",
                             "Wilson", "Moore", "Wilson", "Taylor", "Anderson", "Thomas", "Jackson", "White"]
                random.shuffle(last_name)

            self.f_name = first_name[0]
            self.l_name = last_name[0]
        except:
            return True

        return False

    def form_filling(self):

        xpath = "//a[@class='_42ft _4jy0 _6lti _4jy6 _4jy2 selected _51sy']"
        if not self.click_to_xpath(xpath, time_wait=3, appointment="кнопка вызова меню регистрации"):
            self.error_comment = None

        xpath = "//input[@name='firstname']"
        if not self.set_text(xpath, self.f_name, appointment="заполнение поля 'имя'", delay=0.2):
            if self.accaunt_block_flag:
                self.answer["status"] = "Ошибка"
            else:
                self.answer["status"] = "Ошибка сервера"
            self.answer["comment"] = self.error_comment
            return False
        time.sleep(2)
        xpath = "//input[@name='lastname']"
        if not self.set_text(xpath, self.l_name, appointment="заполнение поля 'фамилия'", delay=0.2):
            if self.accaunt_block_flag:
                self.answer["status"] = "Ошибка"
            else:
                self.answer["status"] = "Ошибка сервера"
            self.answer["comment"] = self.error_comment
            return False
        time.sleep(2)
        xpath = "//input[@name='reg_email__']"
        if not self.set_text(xpath, self.settings["email_f"], appointment="заполнение поля 'email'", delay=0.2):
            if self.accaunt_block_flag:
                self.answer["status"] = "Ошибка"
            else:
                self.answer["status"] = "Ошибка сервера"
            self.answer["comment"] = self.error_comment
            return False
        time.sleep(2)
        xpath = "//input[@name='reg_email_confirmation__']"
        if not self.set_text(xpath, self.settings["email_f"], appointment="заполнение поля 'email подтвердить'", delay=0.2):
            if self.accaunt_block_flag:
                self.answer["status"] = "Ошибка"
            else:
                self.answer["status"] = "Ошибка сервера"
            self.answer["comment"] = self.error_comment
            return False
        time.sleep(2)
        xpath = "//input[@name='reg_passwd__']"
        if not self.set_text(xpath, self.settings["fb_password"], appointment="заполнение поля 'пароль'", delay=0.2):
            if self.accaunt_block_flag:
                self.answer["status"] = "Ошибка"
            else:
                self.answer["status"] = "Ошибка сервера"
            self.answer["comment"] = self.error_comment
            return False
        time.sleep(2)
        index = random.randint(2, 27)
        xpath = "//select[@name='birthday_day']"
        if not self.set_current_index(xpath, index, appointment="выбор дня рождения"):
            if self.accaunt_block_flag:
                self.answer["status"] = "Ошибка"
            else:
                self.answer["status"] = "Ошибка сервера"
            self.answer["comment"] = self.error_comment
            return False
        time.sleep(2)
        index = random.randint(1, 10)
        xpath = "//select[@name='birthday_month']"
        if not self.set_current_index(xpath, index, appointment="выбор месяца рождения"):
            if self.accaunt_block_flag:
                self.answer["status"] = "Ошибка"
            else:
                self.answer["status"] = "Ошибка сервера"
            self.answer["comment"] = self.error_comment
            return False
        time.sleep(2)
        index = random.randint(20, 30)
        xpath = "//select[@name='birthday_year']"
        if not self.set_current_index(xpath, index, appointment="выбор года рождения"):
            if self.accaunt_block_flag:
                self.answer["status"] = "Ошибка"
            else:
                self.answer["status"] = "Ошибка сервера"
            self.answer["comment"] = self.error_comment
            return False
        time.sleep(2)
        index = 0
        xpath = "//input[@name='sex']"
        if not self.selected_chec_boxs(xpath, index, appointment="выбор пола"):
            if self.accaunt_block_flag:
                self.answer["status"] = "Ошибка"
            else:
                self.answer["status"] = "Ошибка сервера"
            self.answer["comment"] = self.error_comment
            return False
        time.sleep(2)
        xpath = "//button[@name='websubmit']"
        if not self.click_to_xpath(xpath, appointment="кнопка отправки"):
            if self.accaunt_block_flag:
                self.answer["status"] = "Ошибка"
            else:
                self.answer["status"] = "Ошибка сервера"
            self.answer["comment"] = self.error_comment
            return False

        time.sleep(5)
        xpath = "//div[@id='reg_error_inner']"
        element = self.return_el_by_xpath(xpath)
        if element != None:
            height = element.size["height"]
            if height > 0:
                self.answer["status"] = "Ошибка"
                self.answer["comment"] = f"Попытайтесь зарегестрироваться позже"
                return False
        return True

    def load_face(self):
        self.get_link("https://www.facebook.com/profile.php")
        self.click_esc(circle=2)
        self.scroll_page_up(10, time_sleep=0)

        if "face_picture_href" in self.settings:

            href = self.settings["face_picture_href"]
            pictur_name = self.load_img(href=href)
            if not pictur_name:
                self.answer["status"] = "Ошибка"
                self.answer["comment"] = "Не удалось загрузить картинку(битая ссылка/проблеммы со связью)"
                return False

            xpath = "//div[contains(concat(' ',@class,' '),' fbTimelineProfilePicSelector')]"
            if not self.click_to_xpath(xpath, appointment="нажать на меню для заливки фото"):
                self.log.log_append({"name": self.tech_name, "action": "action", "text": "клик "})
                return False

            xpath = "//a[@class='_3cia']/div[@class='_3jk']/input[@type='file']"
            elem = self.return_el_by_xpath(xpath)
            if elem != None:
                elem.send_keys(pictur_name)
                self.log.log_append({"name": self.tech_name, "action": "action", "text": "фото залито"})
            else:
                self.log.log_append({"name": self.tech_name, "action": "action", "text": "не удалось залить фото"})
                return False

            try:
                os.remove(pictur_name)
            except:
                pass

            xpath = "//button[@data-testid='profilePicSaveButton']"
            if not self.click_to_xpath(xpath, time_wait=120, appointment="кнопка сохранения изменений"):
                return False
            else:
                return True

        else:
            return False

    def load_caver(self):
        self.get_link("https://www.facebook.com/profile.php")
        self.click_esc(circle=2)
        self.scroll_page_up(10, time_sleep=0)
        if "cover_picture_href" in self.settings:

            href = self.settings["cover_picture_href"]
            pictur_name = self.load_img(href=href)
            if not pictur_name:
                self.answer["status"] = "Ошибка"
                self.answer["comment"] = "Не удалось загрузить картинку(битая ссылка/проблеммы со связью)"
                return False

            xpath = "//div[@id='fbProfileCoverPhotoSelector']"
            element_to_hover_over = self.return_el_by_xpath(xpath)
            if element_to_hover_over != None:
                hover = ActionChains(self.driver).move_to_element(element_to_hover_over)
                hover.perform()
                if not self.click_to_element(element_to_hover_over):
                    return False
            else:
                return False

            xpath = "//label//div[@class='_3jk']//input"
            element = self.return_el_by_xpath(xpath)
            if element != None:
                element.send_keys(pictur_name)

            try:
                os.remove(pictur_name)
            except:
                pass

            xpath = "//button[@name='save']"
            if not self.click_to_xpath(xpath, time_wait=120, appointment="кнопка сохранения изменений"):
                return False
            else:
                self.log.log_append({"name": self.tech_name, "action": "action", "text": "кавер залито"})
                return True
        else:
            return False

    def login_mail(self, flag=True):
        type_mail = self.settings["email_f"].split("@")[1]

        if type_mail == "yahoo.com":

            self.get_link(
                "https://login.yahoo.com/config/login?.src=fpctx&.intl=us&.lang=en-US&.done=https%3A%2F%2Fwww.yahoo.com")

            xpath = "//input[@id='login-username']"
            if not self.set_text(xpath, self.settings["email_f"], time_wait=5,
                                 appointment="заполнение поля 'email' входа в почту"):
                if self.accaunt_block_flag:
                    self.answer["status"] = "Ошибка"
                else:
                    self.answer["status"] = "Ошибка сервера"
                self.answer["comment"] = self.error_comment
                return False
            else:
                self.enter_click(xpath)

            xpath = "//input[@id='login-passwd']"
            if not self.set_text(xpath, self.settings["email_password"],
                                 appointment="заполнение поля 'password' входа в почту"):
                if self.accaunt_block_flag:
                    self.answer["status"] = "Ошибка"
                else:
                    self.answer["status"] = "Ошибка сервера"
                self.answer["comment"] = self.error_comment
                return False
            else:
                self.enter_click(xpath)
            time.sleep(2)
            self.driver.get("https://mail.yahoo.com")
            text = "mail.yahoo.com/d/folders/1"
            if not self.check_text_in_link(text=text):
                return False
            else:
                return True

        elif type_mail == "gmail.com":

            self.get_link(
                "https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")

            u = ["https://policies.google.com/privacy?gl=TM&hl=en",
                 "https://mail.google.com/mail/u/0/#inbox",
                 "https://mail.google.com/mail/#inbox",
                 "https://policies.google.com/privacy?gl=US&hl=ru",
                 "https://mail.google.com/mail/u/0/",
                 "https://mail.google.com/mail/u/0/?pli=1#inbox"]

            if not self.driver.current_url in u:

                xpath = "//div[@id='profileIdentifier']"
                if self.check_xpath(xpath, time_wait=3):
                    xpath = "//input[@name='password']"
                    if not self.set_text(xpath, self.settings["email_password"],
                                         appointment="заполнение поля 'password' входа в почту"):
                        if self.accaunt_block_flag:
                            self.answer["status"] = "Ошибка"
                        else:
                            self.answer["status"] = "Ошибка сервера"
                        self.answer["comment"] = self.error_comment
                        return False
                    else:
                        self.enter_click(xpath)
                time.sleep(2)

                xpath = "//input[@id='identifierId']"
                if not self.set_text(xpath, self.settings["email_f"], time_wait=150,
                                     appointment="заполнение поля 'email' входа в почту"):
                    if self.accaunt_block_flag:
                        self.answer["status"] = "Ошибка"
                    else:
                        self.answer["status"] = "Ошибка сервера"
                    self.answer["comment"] = self.error_comment
                    return False
                else:
                    self.enter_click(xpath)

                time.sleep(2)
                xpath = "//input[@name='password']"
                if not self.set_text(xpath, self.settings["email_password"], time_wait=150,
                                     appointment="заполнение поля 'password' входа в почту"):
                    if self.accaunt_block_flag:
                        self.answer["status"] = "Ошибка"
                    else:
                        self.answer["status"] = "Ошибка сервера"
                    self.answer["comment"] = self.error_comment
                    return False
                else:
                    self.enter_click(xpath)

            time.sleep(2)

            if self.find_xpath("""//span[text()="Couldn't sign you in"]""") and flag:
                xpath = "//li[last()-1]"
                self.click_to_xpath(xpath, time_wait=5)
                time.sleep(10)
                self.login_mail(flag = False)

            xpath = "//li[last()-1]"
            if self.click_to_xpath(xpath, time_wait=5, appointment="кнопка подверждение рекавери почты"):
                time.sleep(2)
                xpath = "//input[@id='knowledge-preregistered-email-response']"
                if not self.set_text(xpath, self.settings["email_s"], appointment="введение рекавери почты"):
                    if self.accaunt_block_flag:
                        self.answer["status"] = "Ошибка"
                    else:
                        self.answer["status"] = "Ошибка сервера"
                    self.answer["comment"] = self.error_comment
                    return False
                else:
                    self.enter_click(xpath)

            xpath = "(//span[@class='RveJvd snByac']/../..)[2]"
            self.click_to_xpath(xpath,time_wait=5)


            time.sleep(2)
            text = "myaccount.google.com/signinoptions/recovery-options-collection"
            if self.check_text_in_link(text=text, circle=5):
                xpath = "//span[text()='Done']"
                if not self.click_to_xpath(xpath):
                    xpath = "//span[text()='Confirm']"
                    self.click_to_xpath(xpath)

            time.sleep(2)
            text = "accounts.google.com/signin/newfeatures"
            if self.check_text_in_link(text=text):
                url = "accounts.google.com/signin/newfeatures"
                if url in self.driver.current_url:
                    xpath = "//div[@class='U26fgb XHsn7e dURtfb Tk2jV']"
                    self.click_to_xpath(xpath)
                    xpath = "//div[@class='U26fgb XHsn7e dURtfb Tk2jV M9Bg4d']"
                    for i in range(2):
                        self.click_to_xpath(xpath)
                    xpath = "//div[@class='U26fgb O0WRkf zZhnYe e3Duub C0oVfc WVqvne ioikHf TMcGbb']"
                    self.click_to_xpath(xpath)

            time.sleep(2)



            # text = "policies.google.com"
            # if self.check_text_in_link(text=text) and flag:
            #     self.login_mail(flag=False)

            time.sleep(2)

            self.click_to_xpath(xpath="(//a[@class='gb4'])[1]",time_wait=3)

            if not self.driver.current_url in u:
                return False

        else:
            return False

        return True

    def confirm_email(self):

        type_mail = self.settings["email_f"].split("@")[1]

        if type_mail == "yahoo.com":

            self.get_link("https://mail.yahoo.com")

            xpath = "//button[@data-test-id='themes-cue-close']"
            if not self.click_to_xpath(xpath, time_wait=5, appointment="закрыть какоето сообщение на почте"):
                if self.accaunt_block_flag:
                    self.answer["status"] = "Ошибка"
                else:
                    self.answer["status"] = "Ошибка сервера"
                self.answer["comment"] = self.error_comment
                return False

            xpath = """(//a[@aria-label="Facebook's email"])[position() = last()]"""
            if self.click_to_xpath(xpath, appointment="поиск песьма"):

                xpath = "//table/tbody/tr[3]/td[2]/table/tbody/tr[2]/td[3]/a"
                if self.click_to_xpath(xpath, appointment="переход оп ссылке в письме"):
                    return True
                else:
                    return False
            else:
                return False

        elif type_mail == "gmail.com":

            self.driver.get("https://mail.google.com")
            time.sleep(10)
            xpath = "//button[@name='welcome_dialog_next']"
            self.click_to_xpath(xpath, time_wait=5)

            xpath = "//button[@name='ok']"
            self.click_to_xpath(xpath, time_wait=5)

            xpath = "(//span[@email='registration@facebookmail.com'])[position() = last()]/../../.."
            if self.click_to_xpath(xpath, appointment="поиск песьма"):
                xpath = "//span[@style='font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;white-space:nowrap;font-weight:bold;vertical-align:middle;color:#ffffff;font-size:14px;line-height:14px']"
                if self.click_to_xpath(xpath, appointment="клик по ссылке"):
                    self.window_handles_go(handles=1)

                    time.sleep(3)
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def answers_questions(self):
        # where did you go to university?
        self.click_esc()
        ua_ans = {"which city do you live in?": ["Kiev", "Dnipro", "Kharkov", "Odessa"],
                  "what city are you from?": ["Kiev", "Dnipro", "Kharkov", "Odessa"],
                  "where did you go to high school?": ["киев школа 54",
                                                       "киев школа 79",
                                                       "киев школа 313",
                                                       "киев школа 252",
                                                       "киев школа 88",
                                                       "киев школа 302",
                                                       "киев школа 3",
                                                       "киев школа 235",
                                                       "киев школа 204",
                                                       "киев школа 207"],
                  "where did you go to college?": ["Львовский национальный университет им. Ивана Франка",
                                                   "Национальный технический университет «Харьковский политехнический институт»",
                                                   "Сумской государственный университет",
                                                   "Киевский национальный университет им. Шевченко",
                                                   "Харьковский национальный университет им. Каразина."],
                  "where do you work?": ["Self-employed",
                                         "student",
                                         "retired"],
                  "где вы живете?": ["Kiev", "Dnipro", "Kharkov", "Odessa"],
                  "из какого вы города?": ["Kiev", "Dnipro", "Kharkov", "Odessa"],
                  "в какой школе вы учились?": ["киев школа 54",
                                                "киев школа 79",
                                                "киев школа 313",
                                                "киев школа 252",
                                                "киев школа 88",
                                                "киев школа 302",
                                                "киев школа 3",
                                                "киев школа 235",
                                                "киев школа 204",
                                                "киев школа 207"],
                  "в каком вузе вы учились?": ["Львовский национальный университет им. Ивана Франка",
                                               "Национальный технический университет «Харьковский политехнический институт»",
                                               "Сумской государственный университет",
                                               "Киевский национальный университет им. Шевченко",
                                               "Харьковский национальный университет им. Каразина."],
                  "где вы работаете?": ["Self-employed",
                                        "student",
                                        "retired"],
                  "У якому місті ви живете?": ["Kiev", "Dnipro", "Kharkov", "Odessa"],
                  "в якому місті Ви мешкаєте?": ["Kiev", "Dnipro", "Kharkov", "Odessa"],
                  "У якій школі ви вчилися?": ["киев школа 54",
                                               "киев школа 79",
                                               "киев школа 313",
                                               "киев школа 252",
                                               "киев школа 88",
                                               "киев школа 302",
                                               "киев школа 3",
                                               "киев школа 235",
                                               "киев школа 204",
                                               "киев школа 207"],
                  "Який коледж ви відвідували?": ["Львовский национальный университет им. Ивана Франка",
                                                  "Национальный технический университет «Харьковский политехнический институт»",
                                                  "Сумской государственный университет",
                                                  "Киевский национальный университет им. Шевченко",
                                                  "Харьковский национальный университет им. Каразина."],
                  "Де ви працюєте?": ["Self-employed",
                                      "student",
                                      "retired"]}

        ru_ans = {
            "which city do you live in?": ["Moscow Russia Moscow"],
            "what city are you from?": ["Moscow Russia Moscow"],
            "where did you go to high school?": ["москва школа 303",
                                                 "москва школа 124",
                                                 "москва школа 252",
                                                 "москва школа 2025",
                                                 "москва школа 54",
                                                 "москва школа 42",
                                                 "москва школа 12"],
            "where did you go to college?": ["Львовский национальный университет им. Ивана Франка",
                                             "Национальный технический университет «Харьковский политехнический институт»",
                                             "Сумской государственный университет",
                                             "Киевский национальный университет им. Шевченко",
                                             "Харьковский национальный университет им. Каразина."],
            "where do you work?": ["Self-employed", "student", "retired"],
            "what is your position at retired": ["retiree"],
            "где вы живете?": ["Moscow", "Saint-Peterburg", "Omsk"],
            "из какого вы города?": ["Moscow", "Saint-Peterburg", "Omsk"],
            "в какой школе вы учились?": ["москва школа 303",
                                          "москва школа 124",
                                          "москва школа 252",
                                          "москва школа 2025",
                                          "москва школа 54",
                                          "москва школа 42",
                                          "москва школа 12"],
            "в каком вузе вы учились?": ["Львовский национальный университет им. Ивана Франка",
                                         "Национальный технический университет «Харьковский политехнический институт»",
                                         "Сумской государственный университет",
                                         "Киевский национальный университет им. Шевченко",
                                         "Харьковский национальный университет им. Каразина."],
            "где вы работаете?": ["Self-employed", "student", "retired"],
            "У якому місті ви живете?": ["Moscow Russia Moscow"],
            "в якому місті Ви мешкаєте?": ["Moscow Russia Moscow"],
            "У якій школі ви вчилися?": ["москва школа 303",
                                         "москва школа 124",
                                         "москва школа 252",
                                         "москва школа 2025",
                                         "москва школа 54",
                                         "москва школа 42",
                                         "москва школа 12"],
            "Який коледж ви відвідували?": ["Львовский национальный университет им. Ивана Франка",
                                            "Национальный технический университет «Харьковский политехнический институт»",
                                            "Сумской государственный университет",
                                            "Киевский национальный университет им. Шевченко",
                                            "Харьковский национальный университет им. Каразина."],
            "Де ви працюєте?": ["Self-employed", "student", "retired"]}

        if self.country == "UA":
            ans = ua_ans
        else:
            ans = ru_ans

        for i in range(5):
            self.click_esc()

            self.scroll_page_up(10, time_sleep=0)
            xpath = "((//div[@id='profile_timeline_info_review']/li/div/div/div/div)[2]/div)[1]"
            try:
                element = self.driver.find_element_by_xpath(xpath)
                question = element.text
                question = question.split(', ')
            except:
                continue

            if len(question) > 1:
                question = question[1]
            else:
                question = question[0]

            question = question.lower()

            if question not in ans:
                self.log.log_append(
                    {"name":"question", "action": "load_file", "text": f"Не определено {question}"})
                xpath = "//button[@value='deny']"
                self.click_to_xpath(xpath)

            else:
                self.click_esc()
                answears = ans[question]
                random.shuffle(answears)
                my_answer = answears[0]

                xpath = "//input[@data-testid='searchable-text-input']"
                self.set_text(xpath, my_answer,delay=0)

                xpath = "//li[@data-testid='choose_contact_button']"
                self.click_to_xpath(xpath)

                xpath = "//input[@data-testid='searchable-text-input']"
                self.enter_click(xpath)

                xpath = "//button[@value='confirm']"
                self.click_to_xpath(xpath)

    def add_groups(self):
        time.sleep(2)
        if self.country == "RU":
            file_groups = ".\\data\\RU group.txt"

        elif self.country == "UA":
            file_groups = ".\\data\\UA group.txt"

        else:
            file_groups = ".\\data\\general.txt"

        links = []
        try:
            f = open(file_groups, "r")
        except:
            self.log.log_append(
                {"name": self.tech_name, "action": "load_file", "text": "не удалось загрузить файл с группами"})
            return False

        for link in f:
            if link == "\n":
                continue
            links.append(link.replace("\n", ""))

        random.shuffle(links)

        for i in range(2):
            link = links[i]
            self.driver.get(link)
            self.click_esc()
            xpath = "//button[@data-testid='page_profile_like_button_test_id']"
            self.click_to_xpath(xpath)

    def run(self):
        try:
            confirm_email_flag = False
            email_comment = ""

            if not self.login_mail():
                self.answer["status"] = "Ошибка"
                self.answer["comment"] = f"Не удалось зайти на почту"
                return

            self.giv_name()

            link = 'https://www.facebook.com'
            if not self.get_link(link):
                self.answer["status"] = "Ошибка"
                self.answer["comment"] = f"Не удалось зайти на https://www.facebook.com"
                return

            flag, ans = self.check_block()
            if not flag:
                self.answer["status"] = "Ошибка"
                self.answer["comment"] = ans
                return

            self.click_esc()
            xpath = "//span[@class='_2md']"
            if self.find_xpath(xpath, time_wait=5):
                if not "www.facebook.com/confirmemail.php" in self.driver.current_url:
                    self.answer["status"] = "Ошибка"
                    self.answer["comment"] = f"Аккаунт уже зарегистрированн"
                    return
            else:
                self.log.log_append(
                    {"name": self.tech_name, "action": "check", "text": "аккаун не залогинен/зарегистрированн"})
                if not self.form_filling():
                    return

            self.click_esc()
            xpath = "//*[@id='bluebar_profile_and_home']/div/div/a"
            if not self.click_to_xpath(xpath, time_wait=10):
                flag, ans = self.check_block()
                if not flag:
                    self.answer["status"] = "Ошибка"
                    self.answer["comment"] = ans
                    return

                if self.confirm_email():
                    confirm_email_flag = True
                    email_comment = "почта подтверждена"
                else:
                    email_comment = "почта не подтверждена"

            if not self.load_caver():
                cover_picture = "caver не залит"
            else:
                cover_picture = "caver залит"

            if not self.load_face():
                face_picture = " face не залит"
            else:
                face_picture = "face залит"

            self.answers_questions()

            if not confirm_email_flag:

                if not self.confirm_email():
                    email_comment = "почта не подтверждена"
                else:
                    email_comment = "почта подтверждена"
                    self.add_groups()
            else:
                self.add_groups()

            if not self.accaunt_block_flag:
                self.answer["status"] = "Выполнен"
                self.answer["comment"] = f"Аккаунт зарегистрирован в фб {email_comment, face_picture, cover_picture}"
            else:
                self.answer["comment"] = self.error_comment
                self.answer["status"] = "Ошибка"
        except:
            self.log.log_append(
                {"name": self.tech_name, "action": "error", "text": "Не предвиденная ошибка потока сценария"})
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = "Не предвиденная ошибка потока сценария"
