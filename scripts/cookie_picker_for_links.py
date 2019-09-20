import requests
import random
from selenium import webdriver
from threading import Thread
import json
import time


class Cookie_picker_for_links_tr(Thread):

    def __init__(self, scenario_settings):
        Thread.__init__(self)
        self.settings = scenario_settings
        self.answear = {"id_scenarios": scenario_settings["id_scenario"],
                        "output_data": {},
                        "comment": "",
                        "status": "",
                        "type": "updata"}

    def run(self):

        try:
            token = self.settings["token"]
            file = self.settings["file_dir"]
            link_min = self.settings["link_min"]
            link_max = self.settings["link_max"]
            link_time = self.settings["link_time"]
        except:
            self.answear["status"] = "Ошибка"
            self.answear["comment"] = f"Не удалось получить данные пользоватея"
            return

        for i in range(20):
            mla_url = 'http://127.0.0.1:35000/api/v1/profile/start?automation=true&profileId=' + token
            resp = requests.get(mla_url)
            json = resp.json()
            if json["status"] == "ERROR":
                time.sleep(2)
            else:
                break

        if json["status"] == "ERROR":
            self.answear["status"] = "Ошибка"
            self.answear["comment"] = f"Не удалось подключиться к мультилогину"
            return

        driver = webdriver.Remote(command_executor=json['value'])

        try:
            handle = open(file, "r")
            handle = list(handle)
        except:
            self.answear["status"] = "Ошибка"
            self.answear["comment"] = f"Не удалось открыть файл"
            driver.quit()
            return

        tyme_arr = []
        summ_links = random.randint(link_min, link_max)
        for i in range(summ_links):
            random.shuffle(handle)
            line = handle[i]
            tyme_arr.append(line)

        self.arr_links = tyme_arr
        for line in tyme_arr:
            try:
                driver.get(line)
            except:
                pass
            time.sleep(link_time)

        self.answear["comment"] = "Сылки пройдены"
        self.answear["status"] = "Выполнен"
        driver.quit()
