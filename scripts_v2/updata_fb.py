from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from .base_tread_v2 import Base_tr
import random
import time


class Updata_fb_tr(Base_tr):

    def run(self):

        arr_action = [
            self.start_page_scroll,
            self.likes,
            self.set_reposts,
            self.add_friends,
            self.fan_page_scroll,
            self.add_groups
        ]

        random.shuffle(arr_action)

        for act in arr_action:
            if not act():
                self.driver.quit()
                return

        self.answear["output_data"]["reposts"] = self.reposts
        self.answear["output_data"]["friends"] = self.friends
        self.answear["output_data"]["groups"] = 0
        self.answear["output_data"]["likes"]= self.lik

        self.answear["comment"] = "Обновление прошло успешно"
        self.answear["status"] = "Выполнен"
        self.driver.quit()
