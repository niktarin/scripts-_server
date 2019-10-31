from threading import Thread
import time
import requests
from main_obj import main_obj

class data_exchange_tr(Thread):

    def __init__(self, main_hab):
        Thread.__init__(self)
        self.main_hab = main_hab
        self.log = main_hab.log
        self.flag_work = True
        self.wait_time = 10
        self.scenario = None


    def set_answer(self):
        for my_object in self.main_hab.main_objects:
            if my_object.status == "compleat":
                answer = my_object.get_answer()
                if answer["status"] == "Ошибка сервера":
                    self.log.log_append({"name": "server", "action": "return_answer", "text": answer})
                    my_object.driver_close()
                    my_object.status = "del"

                if answer["status"] == "Ошибка":
                    self.log.log_append({"name": "server", "action": "return_answer", "text": answer})
                    my_object.driver_close()
                    my_object.status = "del"

                # else:
                try:
                    respons = requests.post('http://arbcapsule.club/api/scenarios/script-result', json=answer)
                    code = respons.status_code
                    # code = 200
                    self.log.log_append({"name": "server", "action": "return_answer", "text": answer})
                    self.log.log_append({"name": "server", "action": "respons_code", "text": code})

                except:
                    self.log.log_append({"name": "server", "action": "return_answer", "text": "Не удалось вернуть ответ на сервер"})
                    continue

                if code == 200:
                    serv_requests = respons.json()

                    if "message" in serv_requests:
                        my_object.driver_close()
                        my_object.status = "del"
                    else:
                        self.log.log_append({"name": "server", "action": "get_scenaroi_prod", "text": serv_requests})
                        my_object.set_scenario(serv_requests)
                        my_object.status = "work"
                        my_object.start()
                else:
                    self.log.log_append({"name": "server", "action": "get_scenaroi_prod", "text": serv_requests})

    def del_obj(self):
        for index, my_object in enumerate(self.main_hab.main_objects):
            if my_object.status == "del":
                del self.main_hab.main_objects[index]

    def get_scenaroi(self):
        try:
            answer = requests.get('http://arbcapsule.club/api/scenarios/get-one')
        except:
            self.log.log_append({"name":"server", "action":"get_scenaroi", "text": "Ошибка при обращении к серверу"})
            return False
        try:
            scenario = answer.json()
        except:
            self.log.log_append({"name": "server", "action": "get_scenaroi_error", "text": "Ошибка при попыке получить answer.json()"})
            return False
        # scenario = {'id_scenarios': 9980, 'type_scenario': 'fb_surfing', 'tech_name': '800', 'ml_token': 'b18024d0-2bb1-47f6-8397-4e349b189ec8', 'email_f': 'inessavelikanova873@gmail.com', 'fb_password': 'p52Hm8i9SdLY56Yd', 'likes_min': '2', 'likes_max': '3', 'repost_min': '1', 'repost_max': '2', 'time': '5'}
        if "error_message" in scenario:
            return
        else:
            self.log.log_append({"name":"server", "action":"get_scenaroi", "text": scenario})
            obj = main_obj(main_hab = self.main_hab)
            obj.set_scenario(scenario)
            obj.start()
            self.main_hab.main_objects.append(obj)
            return True

    def check_status_treads(self):
        for my_object in self.main_hab.main_objects:
            if my_object.status == "work":
                my_object.tr_chec_status()

    def check_len(self):
        len_treads = len(self.main_hab.main_objects)
        max_treads = self.main_hab.max_tread
        if len_treads < max_treads:
            return False
        else:
            return True

    def run(self):
        while self.flag_work:
            self.check_status_treads()
            self.set_answer()
            self.del_obj()

            if self.check_len():
                time.sleep(self.wait_time)
                continue

            self.get_scenaroi()
            time.sleep(self.wait_time)



