from console_tr import consol_tr
from log_obj import log
from data_exchange_tr import data_exchange_tr
from timer_tr import timer
import time
from ml_control_obj import ml_control

class main_hab():
    main_objects = []
    max_tread = 0
    max_err = 3
    errors = 0

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
        t = 3600
        self.timer.add_action(time=t,command = self.console.check_command, commands = "command:treads max:2")


main_hab = main_hab()
main_hab.start()

# command:print_log
# command:treads max:2
