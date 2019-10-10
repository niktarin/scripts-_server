from console_tr import consol_tr
from log_obj import log
from data_exchange_tr import data_exchange_tr
from timer_tr import timer
import time
from ml_control_obj import ml_control

class main_hab():
    main_objects = []
    max_tread = 0

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
        t = time.time() + 30
        # print(time.time())
        # print(t)
        # print(t+100)
        # self.timer.add_action(time=t,command = self.console.check_command, commands = "command:treads max:0")
        # self.timer.add_action(time=t+20,command = self.ml_control.restart_ml)
        # self.timer.add_action(time=t+30,command = self.ml_control.close_ml)

main_hab = main_hab()
main_hab.start()



# consol_tr = consol_tr(main_hab)
# data_exchange_tr = data_exchange_tr(main_hab)

# consol_tr.start()
# data_exchange_tr.start()
