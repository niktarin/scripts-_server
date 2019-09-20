from selenium import webdriver
import requests

from scripts.login_email import Login_email_tr
from scripts.simple_update import Simple_update_fb
from scripts.set_posts import Set_posts_tr
from scripts.check_fb import Check_fb
from scripts.сreate_fan_page import Create_fan_page_tr
from scripts.registr_fb import Registr_fb_tr
from scripts.load_img import load_img_tr


class main_obj:

    def __init__(self):
        self.settings = None
        self.driver = None
        self.id_scenarios = ""
        self.type_scenario = ""
        self.output_data = {}
        self.add_driver_comment = ""
        self.add_scenario_comment = ""
        self.comment = ""
        self.tech_name = None
        self.status = "work"
        self.scenario_sattus = None
        self.ml_answear = None
        self.tr_answear = None
        self.log = None
        self.answer = {"id_scenarios": self.id_scenarios,
                       "type_scenario": self.type_scenario,
                       "output_data": {},
                       "comment": "",
                       "status": ""}

    def add_driver(self):
        if self.settings == None:
            self.add_driver_comment = "Не удалось запустить аккаунт"
            return False

        try:
            mla_url = 'http://127.0.0.1:35000/api/v1/profile/start?automation=true&profileId=' + self.settings[
                "ml_token"]
            try:
                resp = requests.get(mla_url)

                self.ml_answear = resp.json()
            except:
                self.add_driver_comment = "Ошибка мультилогина"
                return False

            if self.ml_answear["status"] == "ERROR":
                if "value" in self.ml_answear:
                    index = self.ml_answear["value"].find("active already")
                    if index > -1:
                        self.add_driver_comment = "Аккаунт уже запущен"
                        return False
                self.add_driver_comment = "Не удалось запустить аккаунт"
                return False
            else:
                self.driver = webdriver.Remote(command_executor=self.ml_answear['value'])
                return True
        except:
            self.add_driver_comment = "Ошибка подключения к мультилогину(Возможно он не запущенн)"
            return False

    def set_scenario(self, scenario_settings):
        self.settings = scenario_settings
        self.tech_name = scenario_settings["tech_name"]
        self.id_scenarios = scenario_settings["id_scenarios"]
        self.type_scenario = scenario_settings["type_scenario"]

    def add_scenario_tread(self):
        scenario = self.settings
        type_scenario = scenario["type_scenario"]

        if type_scenario == "mail_login":
            tread = Login_email_tr(scenario)

        elif type_scenario == "empty_update":
            tread = Simple_update_fb(scenario)

        elif type_scenario == "check_fb":
            tread = Check_fb(scenario)

        elif type_scenario == "create_post":
            tread = Set_posts_tr(scenario)

        elif type_scenario == "create_fanpage":
            tread = Create_fan_page_tr(scenario)

        elif type_scenario == "fb_registration":
            tread = Registr_fb_tr(scenario)

        elif type_scenario == "fb_photo_update":
            tread = load_img_tr(scenario)
        else:
            self.add_scenario_comment = "Не удалось определить сценарий"
            return False

        self.tread = tread
        return True

    def start_tread(self):
        if self.tread != None:
            self.tread.driver = self.driver
            self.tread.start()
            return True
        else:
            return False

    def tr_chec_status(self):
        if self.tread.is_alive():
            self.status = "work"
        else:
            self.status = "compleat"

    def answer(self):
        if not self.tread.is_alive():
            output_data = self.tread.answer["output_data"]
            comment = self.tread.answer["comment"]
            status = self.tread.answer["status"]

            self.answer = {"output_data": output_data,
                           "comment": comment,
                           "status": status}
            return self.answer
        else:
            return False

    def start(self):
        if self.driver == None:
            if not self.add_driver():
                self.answer["status"] = "Ошибка"
                self.answer["comment"] = self.add_driver_comment
                return

        if not self.add_scenario_tread():
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = self.add_driver_comment

        if not self.start_tread():
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = "Не удалось запустить поток"
        return True

    def driver_close(self):
        mla_url = "http://localhost.multiloginapp.com:35000/api/v1/profile/stop?profileId=" + self.settings["ml_token"]
        try:
            requests.get(mla_url)
        except:
            pass

        self.driver.quit()
