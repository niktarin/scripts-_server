from threading import Thread
import time
import requests
from main_obj import main_obj

class data_exchange_tr(Thread):

    def __init__(self, main_hab):
        Thread.__init__(self)
        self.main_hab = main_hab
        self.flag_work = True
        self.wait_time = 10
        self.scenario = None

    def set_answear(self):
        for my_object in self.main_hab.main_objects:
            if my_object.status == "compleat":
                answer = my_object.answear()

                try:
                    respons = requests.post('http://arbcapsule.club/api/scenarios/script-result', json=answer)
                except:
                    continue

                code = respons.status_code
                if code == 200:
                    serv_requests = respons.json()

                    if "error_message" in serv_requests:
                        my_object.driver_close()
                        my_object.status = "del"
                    else:
                        my_object.set_scenaroi(serv_requests)
                        my_object.status = "work"
                        my_object.start()

    def del_obj(self):
        for my_object in self.main_hab.main_objects:
            my_object.cheack_status()

    def get_scenaroi(self):
        answer = requests.get('http://arbcapsule.club/api/scenarios/get-one')
        scenario = answer.json()

        if "error_message" in scenario:
            return
        else:
            obj = main_obj()
            obj.log = self.main_hab.log
            obj.set_scenario(scenario)
            obj.start()

    def check_status_treads(self):
        for my_object in self.main_hab.main_objects:
            my_object.cheack_status()

    def check_len(self):
        len_treads = len(self.main_hab.main_objects)
        max_treads = self.main_hab.max_tread

        if len_treads >= max_treads:
            return True
        else:
            return False

    def run(self):
        while self.flag_work:

            self.check_status_treads()
            self.set_answear()
            self.del_obj()

            if not self.check_len():
                time.sleep(self.wait_time)
                continue

            self.get_scenaroi()



