from scripts.base_tread import Base_tr
import time

class Login_email_tr(Base_tr):


    def login_mail(self):
        type_mail = self.settings["email_f"].split("@")[1]

        if type_mail == "yahoo.com":

            self.driver.get("https://login.yahoo.com/config/login?.src=fpctx&.intl=us&.lang=en-US&.done=https%3A%2F%2Fwww.yahoo.com")

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
            if "mail.yahoo.com/d/folders/1" not in  self.driver.current_url:
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
            if self.click_to_xpath(xpath,circle=5, time_sleep=1):
                xpath = "//input[@id='identifierId']"
                self.set_text(xpath, self.settings["email_s"])
                self.enter_click(xpath)

            time.sleep(5)

            if not self.driver.current_url in u:
                return False

        else:
            return False

        return True


    def run(self):

        if not self.connect_to_multilogin():
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = "Проблемы с подключением к мультилогину"
            try:
                self.driver.quit()
            except:
                pass
            return

        if not self.login_mail():
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = f"Не удалось зайти на почту"
            self.driver.quit()
            return 

        self.answer["status"] = "Выполнен"
        self.answer["comment"] = "Аккаунт залогинен на почту"
        self.driver.quit()
