import requests
from selenium import webdriver
import json
from scripts.base_tread import Base_tr
import random
import time
from selenium.webdriver.common.keys import Keys
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
            return (None, None)

        return (self.f_name, self.l_name)

    def form_filling(self):

        xpath = "//input[@name='firstname']"
        if not self.set_text(xpath, self.f_name):
            return (False)
        time.sleep(4)

        xpath = "//input[@name='lastname']"
        if not self.set_text(xpath, self.l_name):
            return (False)

        time.sleep(4)
        xpath = "//input[@name='reg_email__']"
        if not self.set_text(xpath, self.settings["email_f"]):
            return (False)

        time.sleep(4)
        xpath = "//input[@name='reg_email_confirmation__']"
        if not self.set_text(xpath, self.settings["email_f"]):
            return (False)

        time.sleep(4)
        xpath = "//input[@name='reg_passwd__']"
        if not self.set_text(xpath, self.settings["fb_password"]):
            return (False)

        time.sleep(4)
        index = random.randint(2, 27)
        xpath = "//select[@name='birthday_day']"
        if not self.set_current_index(xpath, index):
            self.answer = {"answer": False, "comment": "Не удалось выбрать день рождения"}
            return (False)

        time.sleep(2)
        index = random.randint(1, 10)
        xpath = "//select[@name='birthday_month']"
        if not self.set_current_index(xpath, index):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = f"Не удалось выбрать месяц рождения"
            return (False)

        time.sleep(2)
        index = random.randint(20, 30)
        xpath = "//select[@name='birthday_year']"
        if not self.set_current_index(xpath, index):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = f"Не удалось выбрать год рождения"
            return (False)

        time.sleep(2)
        index = 0
        xpath = "//input[@name='sex']"
        if not self.selected_chec_boxs(xpath, index):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = f"Не удалось выбрать пол"
            return (False)

        time.sleep(2)
        xpath = "//button[@name='websubmit']"
        if not self.click_to_xpath(xpath):
            return (False)

        time.sleep(3)
        xpath = "//div[@id='reg_error_inner']"
        try:
            element = self.driver.find_element_by_xpath(xpath)
            height = element.size["height"]
            if height > 0:
                self.click_to_xpath(xpath)
        except:
            pass
        time.sleep(3)

        # elements = self.driver.find_elements_by_xpath(xpath)
        # if len(elements) > 0:
        #     self.click_to_xpath(xpath)

        # time.sleep(3)
        # elements = self.driver.find_elements_by_xpath(xpath)
        # if len(elements) > 0:

        xpath = "//div[@id='reg_error_inner']"
        try:
            element = self.driver.find_element_by_xpath(xpath)
            height = element.size["height"]
            if height > 0:
                self.answer["status"] = "Ошибка"
                self.answer["comment"] = f"Попытайтесь зарегестрироваться позже"
                return False
        except:
            pass

        return True

    def google_form_filling(self):
        xpath = "//button[@class='_42ft _4jy0 _4jy4 _4jy1 selected _51sy']"
        if self.click_to_xpath(xpath):
            time.sleep(10)
            window_after = self.driver.window_handles[1]
            self.driver.switch_to.window(window_after)

            if not self.click_to_xpath("//li[@class='M8HEDc ibdqA cd29Sd bxPAYd W7Aapd SmR8 znIWoc']"):

                xpath = "//input[@type='email']"
                if not self.set_text(xpath, self.settings["email_f"]):
                    self.answer["status"] = "Ошибка"
                    self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
                    return

                xpath = "//div[@id='identifierNext']"
                if not self.click_to_xpath(xpath):
                    return

                xpath = "//input[@type='password']"
                if not self.set_text(xpath, self.settings["email_password"]):
                    self.answer["status"] = "Ошибка"
                    self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
                    return

                xpath = "//div[@id='passwordNext']"
                if not self.click_to_xpath(xpath):
                    return

                xpath = "(//li[last()-1])[1]"
                if not self.click_to_xpath(xpath):
                    return

                elements = self.driver.find_elements_by_xpath("//button[@id='checkpointSubmitButton']")
                if len(elements) > 0:
                    self.answer["status"] = "Ошибка"
                    self.answer["comment"] = f"Аккаунт заблокированн"
                    return
                xpath = "//input[@id='identifierId']"
                if not self.set_text(xpath, self.settings["email_s"]):
                    self.answer["status"] = "Ошибка"
                    self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
                    return

                elements = self.driver.find_elements_by_xpath("//button[@id='checkpointSubmitButton']")
                if len(elements) > 0:
                    self.answer["status"] = "Ошибка"
                    self.answer["comment"] = f"Аккаунт заблокированн"
                    return
                xpath = "//input[@id='identifierId']"
                element = self.driver.find_element_by_xpath(xpath)
                element.send_keys(Keys.ENTER)

                elements = self.driver.find_elements_by_xpath("//button[@id='checkpointSubmitButton']")
                if len(elements) > 0:
                    self.answer["status"] = "Ошибка"
                    self.answer["comment"] = f"Аккаунт заблокированн"
                    return

            time.sleep(3)
            if len(self.driver.window_handles) > 1:
                window_after = self.driver.window_handles[1]
                self.driver.switch_to.window(window_after)
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[0])

            for i in range(3):
                webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
                time.sleep(1)

            try:
                xpath = "//input[@name='ok']"
                self.click_to_xpath(xpath)
            except:
                pass

            xpath = "(//div[@id='bluebar_profile_and_home']//div//div)[1]"
            self.click_to_xpath(xpath)
        return True

    def load_img(self):
        # xpath = "(//div[@class='linkWrap noCount'])[1]"
        # if not self.click_to_xpath(xpath):
        #     self.answer["status"] = "Ошибка"
        #     self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
        #     return (False)

        if "face_picture_href" in self.settings and self.settings["face_picture_href"] != False:
            self.scroll_page_up(10)
            self.face_picture = "face_picture.jpg"
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
                    elem = self.driver.find_element_by_xpath(
                        "//a[@class='_3cia']/div[@class='_3jk']/input[@type='file']")
                    elem.send_keys(self.face_picture)
                    break
                except:
                    time.sleep(1)

            time.sleep(10)

            xpath = "//button[@data-testid='profilePicSaveButton']"
            if not self.click_to_xpath(xpath):
                return (False)

            try:
                os.remove(self.face_picture)
            except:
                pass

            time.sleep(5)
            for i in range(3):
                webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
                time.sleep(1)

            self.scroll_page_up(15)
        else:
            self.face_picture = None

        if "cover_picture_href" in self.settings and self.settings["cover_picture_href"] != False:
            self.cover_picture = "cover_picture.jpg"
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

            try:
                os.remove(self.cover_picture)
            except:
                pass

        else:
            self.cover_picture = None

        return

    def login_mail(self):
        type_mail = self.settings["email_f"].split("@")[1]

        if type_mail == "yahoo.com":

            self.driver.get(
                "https://login.yahoo.com/config/login?.src=fpctx&.intl=us&.lang=en-US&.done=https%3A%2F%2Fwww.yahoo.com")

            time.sleep(4)

            xpath = "//input[@id='login-username']"
            if not self.set_text(xpath, self.settings["email_f"]):
                return False
            else:
                self.enter_click(xpath)

            time.sleep(4)

            xpath = "//input[@id='login-passwd']"
            if not self.set_text(xpath, self.settings["email_password"]):
                return False

            else:
                self.enter_click(xpath)

            self.driver.get("https://mail.yahoo.com")

            time.sleep(5)
            if "mail.yahoo.com/d/folders/1" not in self.driver.current_url:
                return False

        elif type_mail == "gmail.com":

            self.driver.get(
                "https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")

            u = ["https://policies.google.com/privacy?gl=TM&hl=en",
                 "https://mail.google.com/mail/u/0/#inbox",
                 "https://mail.google.com/mail/#inbox",
                 "https://policies.google.com/privacy?gl=US&hl=ru",
                 "https://mail.google.com/mail/u/0/"]

            if not self.driver.current_url in u:

                xpath = "//div[@id='profileIdentifier']"
                if self.check_xpath(xpath):
                    xpath = "//input[@name='password']"
                    self.set_text(xpath, self.settings["email_password"])
                    self.enter_click(xpath)

                time.sleep(3)
                xpath = "//input[@id='identifierId']"
                if not self.set_text(xpath, self.settings["email_f"]):
                    return False
                else:
                    self.enter_click(xpath)

                time.sleep(4)
                xpath = "//input[@name='password']"
                if not self.set_text(xpath, self.settings["email_password"]):
                    return False
                else:
                    self.enter_click(xpath)

            time.sleep(5)

            self.driver.switch_to_window(self.driver.window_handles[0])

            xpath = "//li[last()-1]"
            if self.click_to_xpath(xpath, circle=5, time_sleep=1):
                xpath = "//input[@id='identifierId']"
                self.set_text(xpath, self.settings["email_s"])
                self.enter_click(xpath)

            time.sleep(5)

            if not self.driver.current_url in u:
                return False

        else:
            return False

        return True

    def confirm_email(self):

        type_mail = self.settings["email_f"].split("@")[1]

        if type_mail == "yahoo.com":

            self.driver.get("https://mail.yahoo.com")

            xpath = "//button[@data-test-id='themes-cue-close']"
            self.click_to_xpath(xpath, circle=10, time_sleep=1)

            xpath = """(//a[@aria-label="Facebook's email"])[position() = last()]"""
            if self.click_to_xpath(xpath, circle=10, time_sleep=1):
                xpath = "//table/tbody/tr[3]/td[2]/table/tbody/tr[2]/td[3]/a"
                self.click_to_xpath(xpath, circle=10, time_sleep=1)
                return True

        elif type_mail == "gmail.com":

            self.driver.get("https://mail.google.com")

            xpath = "//button[@name='welcome_dialog_next']"
            self.click_to_xpath(xpath, circle=5, time_sleep=1)

            xpath = "//button[@name='ok']"
            self.click_to_xpath(xpath, circle=5, time_sleep=1)

            xpath = "(//span[@email='registration@facebookmail.com'])[position() = last()]/../../.."
            try:
                WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath)))
                self.click_to_xpath(xpath)
                xpath = "//span[@style='font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;white-space:nowrap;font-weight:bold;vertical-align:middle;color:#ffffff;font-size:14px;line-height:14px']"
                self.click_to_xpath(xpath)
                return True
            except:
                return False
        else:
            return False

        return False

    def answers_questions(self):

        ans = {
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

        for i in range(6):

            xpath = "((//div[@id='profile_timeline_info_review']/li/div/div/div/div)[2]/div)[1]"
            element = self.driver.find_element_by_xpath(xpath)
            question = element.text
            question = question.split(', ')

            if len(question) > 1:
                question = question[1]
            else:
                question = question[0]

            question.lower()

            if question not in ans:
                print(f"Не определено {question}")
                # xpath = "//button[@value='deny']"
                # self.click_to_xpath(xpath)

            else:
                answears = ans[question]
                random.shuffle(answears)
                my_answer = answears[0]
                xpath = "//input[@data-testid='searchable-text-input']"
                self.set_text(xpath, my_answer)

                xpath = "//li[@data-testid='choose_contact_button']"
                self.click_to_xpath(xpath)

                xpath = "//input[@data-testid='searchable-text-input']"
                self.enter_click(xpath)

                xpath = "//button[@value='confirm']"
                self.click_to_xpath(xpath)

            time.sleep(3)

    def add_groups(self):
        if self.country == "RU":
            file_groups = "RU group.txt"

        elif self.country == "UA":
            file_groups = "UA group.txt"

        else:
            file_groups = "general.txt"

        links = []
        f = open(file_groups, "r")

        for link in f:
            if link == "\n":
                continue

            links.append(link.replace("\n", ""))

        random.shuffle(links)

        for i in range(2):
            link = links[i]
            self.driver.get(link)

            xpath = "//button[@data-testid='page_profile_like_button_test_id']"
            self.click_to_xpath(xpath)

    def run(self):

        if not self.login_mail():
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = f"Не удалось зайти на почту"
            self.driver.quit()
            return

        self.giv_name()

        link = 'https://www.facebook.com'
        if not self.get_tu_link(link):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = f"Не удалось зайти на https://www.facebook.com"
            self.driver.quit()
            return

        time.sleep(3)

        if not self.check_block():
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = f"Аккаунт заблокирован"
            self.driver.quit()
            return

        if not self.form_filling():
            self.driver.quit()
            return

        for i in range(5):
            webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
            time.sleep(1)

        if not self.check_block():
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = f"Аккаунт заблокирован аосле заполнения формы"
            self.driver.quit()
            return

        xpath = "//*[@id='bluebar_profile_and_home']/div/div/a"
        self.click_to_xpath(xpath)

        for i in range(4):
            webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
            time.sleep(1)

        self.load_img()

        self.answers_questions()

        self.add_groups()

        if self.cover_picture == None:
            cover_picture = "caver не залит"
        else:
            cover_picture = "caver залит"

        if self.face_picture == None:
            face_picture = " face не залит"
        else:
            face_picture = "face залит"

        if not self.confirm_email():
            email_comment = "почта не подтверждена"
        else:
            email_comment = "почта подтверждена"

        self.answer["status"] = "Выполнен"
        self.answer["comment"] = f"Аккаунт зарегистрирован в фб {email_comment, face_picture, cover_picture}"
