from scripts_v2.base_tread_v2 import Base_tr
import re
import time

class First_ad_card_BM(Base_tr):

    def add_fp(self):

        self.get_link("https://business.facebook.com")

        xpath = "//div[text()='Add Page']/../.."
        if not self.click_to_xpath(xpath, appointment="кнопка cоздания страницы #1"):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = self.error_comment
            return False

        xpath = "(//div[text()='Add Page']/../..)[2]"
        if not self.click_to_xpath(xpath, appointment="кнопка cоздания страницы #2"):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = self.error_comment
            return False

        xpath = "//input[@data-testid='searchable-text-input']"
        if not self.set_text(xpath, self.settings["fp_link"], appointment="заполнение поля 'fp link'"):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = self.error_comment
            return False
        time.sleep(2)
        xpath = "//ul[@role='listbox']/li"
        if not self.click_to_xpath(xpath, appointment="иконка выпадающего меню"):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = self.error_comment
            return False
        time.sleep(2)
        xpath = "(//div[text()='Add Page']/../..)[2]"
        if not self.click_to_xpath(xpath, appointment="кнопка cоздания страницы #2"):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = self.error_comment
            return False

    def add_card(self):
        self.get_link("https://business.facebook.com/settings/payment-methods")

        xpath = "//div[text()='Add']/../.."
        if not self.click_to_xpath(xpath, appointment="кнопка cоздания страницы #2"):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = self.error_comment
            return False

        time.sleep(2)
        xpath = "(//div[@id='AdsPaymentsInlineCreditCard']/div/div/div)[2]/div/label/input"
        if not self.set_text(xpath, self.settings["name_on_card"], appointment="name_on_card"):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = self.error_comment
            return False
        time.sleep(2)
        xpath = "((//div[@id='AdsPaymentsInlineCreditCard']/div/div/div)[4]/div)[1]/label/input"
        if not self.set_text(xpath, self.settings["card_number"], appointment="card_number"):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = self.error_comment
            return False
        time.sleep(2)
        xpath = "((//div[@id='AdsPaymentsInlineCreditCard']/div/div/div)[4]/div)[2]/label/input"
        if not self.set_text(xpath, self.settings["expiration_mm"], appointment="expiration_mm"):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = self.error_comment
            return False
        time.sleep(2)
        xpath = "((//div[@id='AdsPaymentsInlineCreditCard']/div/div/div)[4]/div)[3]/label/input"
        if not self.set_text(xpath, self.settings["expiration_yy"], appointment="expiration_yy"):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = self.error_comment
            return False
        time.sleep(2)
        xpath = "(//div[@id='AdsPaymentsInlineCreditCard']/div/div/div)[6]/div/label/input "
        if not self.set_text(xpath, self.settings["security_code"], appointment="security_code"):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = self.error_comment
            return False

        xpath = "//button[text()='Continue']"
        if not self.click_to_xpath(xpath, appointment="Continue"):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = self.error_comment
            return False

    def add_account(self):
        self.get_link("https://business.facebook.com/settings/ad-accounts")

        xpath = "(//div[@data-testid='persona-selector']/div)[1]"
        name = self.return_el_by_xpath(xpath).text

        xpath = "//*[text()='Add']/../.."
        if not self.click_to_xpath(xpath, appointment="кнопка cоздания account"):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = self.error_comment
            return False

        xpath = "//div[text()='Create a New Ad Account']"
        if not self.click_to_xpath(xpath, appointment="Create a New Ad Account"):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = self.error_comment
            return False

        xpath = "//input[@data-testid='AdAccountDialogs-brands/createTextInput']"
        if not self.set_text(xpath, name, appointment="name"):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = self.error_comment
            return False


        xpath = "//*[text()='Select payment method']/../../.."
        if not self.click_to_xpath(xpath, appointment="Next"):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = self.error_comment
            return False

        xpath = f"//span[text()='MASTERCARD *{ self.settings['card_number'][-4:]}']"
        if not self.click_to_xpath(xpath, appointment="Выпадающее меню оплаты"):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = self.error_comment
            return False

        xpath = "//div[text()='Next']"
        if not self.click_to_xpath(xpath, appointment="Next"):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = self.error_comment
            return False

        xpath = f"//*[text()='My business ({name})']"
        if not self.click_to_xpath(xpath, appointment="Next"):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = self.error_comment
            return False

        xpath = "//*[text()='Create']"
        if not self.click_to_xpath(xpath, appointment="Create"):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = self.error_comment
            return False

        xpath ="(//*[text()='Name']/../span)[2]/div"
        if not self.click_to_xpath(xpath, appointment=""):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = self.error_comment
            return False

        xpath ="//*[text()='Manage Ad Account']/../..//div[@role='checkbox']"
        if not self.click_to_xpath(xpath, appointment=""):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = self.error_comment
            return False

        xpath ="//*[text()='Assign']/../.."
        if not self.click_to_xpath(xpath, appointment=""):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = self.error_comment
            return False

    def compain(self):
        self.get_link("https://www.facebook.com/adsmanager/manage/campaigns")

        xpath = "(//*[text()='I Accept'])[2]/../.."
        self.click_to_xpath(xpath,time_wait=10, appointment="")

        self.driver.refresh()

        html = self.driver.page_source
        rt = re.findall(r"""access_token:"\w+""", html)
        rt = rt[0]
        rt = rt.replace('access_token:"', "").replace('"', "")

        self.answer["output_data"]["access_token"] = rt

    def run(self):
        try:
            if not self.check():
                return
            #
            # self.add_fp()
            # self.add_card()
            # self.add_account()
            self.compain()

            # if :
            #     status = "Выполнен"
            # else:
            #     status = "Ошибка"

            # self.answer["comment"] = f" "
            # self.answer["status"] = status
        except:
            self.log.log_append({"name": self.tech_name, "action": "error", "text": "Не предвиденная ошибка потока сценария"})
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = "Не предвиденная ошибка потока сценария"