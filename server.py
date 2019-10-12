from console_tr import consol_tr
from log_obj import log
from data_exchange_tr import data_exchange_tr
from timer_tr import timer
import time
from ml_control_obj import ml_control

class main_hab():
    main_objects = []
    max_tread = 2

    def __init__(self):
        self.log = log()
        self.console = consol_tr(self)
        self.data_exchange = data_exchange_tr(self)
        self.timer = timer(self)
        self.ml_control = ml_control()

    def start(self):
        self.console.start()
        self.timer.start()
        self.data_exchange.start()
        # t = time.time()+100
        t = time.time() + 3
        # print(time.time())
        # print(t)
        # print(t+100)
        # self.timer.add_action(time=t,command = self.console.check_command, commands = "command:treads max:0")
        # self.timer.add_action(time=t+20,command = self.ml_control.restart_ml)
        # self.timer.add_action(time=t+30,command = self.ml_control.close_ml)

def start():
    main_hab = main_hab()
    main_hab.start()

main_hab = main_hab()
main_hab.start()

# command:print_log
