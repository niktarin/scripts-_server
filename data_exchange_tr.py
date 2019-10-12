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
                    self.log.log_append({"name": "server", "action": "return_answer", "text": answer})
                except:
                    self.log.log_append({"name": "server", "action": "return_answer", "text": "Не удалось вернуть ответ на сервер"})
                    continue

                code = respons.status_code
                # my_object.driver_close()
                # my_object.status = "del"
                if code == 200:
                    serv_requests = respons.json()

                    if "message" in serv_requests:
                        my_object.driver_close()
                        my_object.status = "del"
                    else:
                        my_object.set_scenario(serv_requests)
                        my_object.status = "work"
                        my_object.start()

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

        scenario = answer.json()
        if "error_message" in scenario:
            return False
        else:
            self.log.log_append({"name":"server", "action":"get_scenaroi", "text": scenario})
            obj = main_obj(self.main_hab.log)
            obj.log = self.main_hab.log
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

            if not self.get_scenaroi():
                time.sleep(self.wait_time)



