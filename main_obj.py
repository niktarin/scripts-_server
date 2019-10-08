from selenium import webdriver
import requests
import time
from selenium.webdriver.remote.command import Command
from scripts_v2.simple_update import Simple_update_fb


# from scripts_v2.set_posts import Set_posts_tr
# from scripts_v2.check_fb import Check_fb
# from scripts_v2.сreate_fan_page import Create_fan_page_tr
# from scripts_v2.registr_fb import Registr_fb_tr
# from scripts_v2.load_img import load_img_tr

class answer:
    id_scenarios = None
    type_scenario = None
    output_data = {}
    comment = None
    status = None

    def set_scenario(self, scenario):
        self.id_scenarios = scenario["id_scenarios"]
        self.type_scenario = scenario["type_scenario"]

    def get_answer(self):
        answer = {"id_scenarios": self.id_scenarios,
                  "type_scenario": self.type_scenario,
                  "output_data": {},
                  "comment": self.comment,
                  "status": self.status}
        return answer


class main_obj:

    def __init__(self, log):
        self.settings = None
        self.driver = None
        self.id_scenarios = None
        self.type_scenario = None
        self.add_driver_comment = None
        self.add_scenario_comment = None
        self.comment = None
        self.tech_name = None
        self.scenario_status = None
        self.ml_answear = None
        self.tr_answear = None
        self.obj_live = True
        self.log = log
        self.status = "work"
        self.output_data = {}
        self.ans_obj = answer()

    def create_driver(self):
        pass

    def add_driver(self):
        if self.settings == None:
            self.add_driver_comment = "Не удалось запустить аккаунт (настройки пустые)"
            return False

        mla_url = 'http://127.0.0.1:35000/api/v1/profile/start?automation=true&profileId=' + self.settings["ml_token"]
        try:
            resp = requests.get(mla_url)
            self.ml_answear = resp.json()
        except:
            self.add_driver_comment = "Ошибка мультилогина (возможноон не запущен или работает не правильно)"
            return False

        if self.ml_answear["status"] == "ERROR":
            if "value" in self.ml_answear:
                index = self.ml_answear["value"].find("active already")
                if index > -1:
                    self.add_driver_comment = "Аккаунт уже запущен"
                    return False
            self.add_driver_comment = f"Не удалось запустить аккаунт ({self.ml_answear})"
            return False

        else:
            self.driver = webdriver.Remote(command_executor=self.ml_answear['value'])
            time.sleep(5)
            self.add_driver_comment = "Аккаунт запущен"
            return True

    def set_scenario(self, scenario_settings):
        self.settings = scenario_settings
        self.tech_name = scenario_settings["tech_name"]
        self.id_scenarios = scenario_settings["id_scenarios"]
        self.type_scenario = scenario_settings["type_scenario"]
        self.ans_obj.set_scenario(scenario_settings)
        self.log.log_append({"name":self.tech_name, "action": "set_scenario", "text": scenario_settings})

    def add_scenario_tread(self):
        scenario = self.settings
        type_scenario = scenario["type_scenario"]

        # if type_scenario == "mail_login":
        #     tread = Login_email_tr(scenario)

        if type_scenario == "empty_update":
            tread = Simple_update_fb(scenario, self.log)


        # elif type_scenario == "check_fb":
        #     tread = Check_fb(scenario)
        #
        # elif type_scenario == "create_post":
        #     tread = Set_posts_tr(scenario)
        #
        # elif type_scenario == "create_fanpage":
        #     tread = Create_fan_page_tr(scenario)
        #
        # elif type_scenario == "fb_registration":
        #     tread = Registr_fb_tr(scenario)
        #
        # elif type_scenario == "fb_photo_update":
        #     tread = load_img_tr(scenario)
        else:
            self.add_scenario_comment = "Не удалось определить сценарий"
            return False

        self.tread = tread
        self.log.log_append({"name": self.tech_name, "action": "add_tread", "text": type_scenario})
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
            self.log.log_append({"name": self.tech_name, "action": "status", "text": f"Сценарий {self.tech_name} (id {self.id_scenarios}) завершон"})
            self.status = "compleat"
            
    def driver_check(self):
        try:
            self.driver.execute(Command.STATUS)
            return False
        except:
            return True
            
    def get_answer(self):
        if self.obj_live:
            if not self.tread.is_alive():
                self.ans_obj.output_data = self.tread.answer["output_data"]
                self.ans_obj.comment = self.tread.answer["comment"]
                self.ans_obj.status = self.tread.answer["status"]
                return self.ans_obj.get_answer()
            return None
        else:
            return self.ans_obj.get_answer()

    def start(self):
        if self.driver == None:            
            for i in range(3):
                if self.add_driver():
                    break
                else:
                    time.sleep(5)

            if self.driver == None:
                self.ans_obj.status = "Ошибка сервера"
                self.ans_obj.comment = self.add_driver_comment
                self.log.log_append({"name": self.tech_name, "action": "obj", "text": self.add_driver_comment})
                self.obj_live = False
                self.status = "compleat"
                return

        if not self.add_scenario_tread():
            self.ans_obj.status = "Ошибка сервера"
            self.ans_obj.status = self.add_scenario_comment
            self.log.log_append({"name": self.tech_name, "action": "obj", "text": self.add_scenario_comment})
            self.obj_live = False
            self.status = "compleat"
            return

        if not self.start_tread():
            self.ans_obj.status = "Ошибка сервера"
            self.ans_obj.status = "Не удалось запустить поток"
            self.log.log_append({"name": self.tech_name, "action": "obj", "text": "Не удалось запустить поток"})
            self.obj_live = False
            self.status = "compleat"

    def driver_close(self):
        mla_url = "http://localhost.multiloginapp.com:35000/api/v1/profile/stop?profileId=" + self.settings["ml_token"]
        try:
            requests.get(mla_url)
        except:
            pass
        try:
            self.driver.quit()
        except:
            pass
        self.log.log_append({"name": self.tech_name, "action": "driver_close", "text": f"Драйвер {self.tech_name} закрыт"})
