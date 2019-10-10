from threading import Thread
import time

class timer(Thread):

    def __init__(self, main_hab):
        Thread.__init__(self)
        self.main_hab = main_hab
        self.log = main_hab.log
        self.actions = {}

    def run(self):
        while True:
            actions = self.actions.copy()
            for int_time in actions:
                if int_time < time.time():
                    action = actions[int_time][0]
                    action(actions[int_time][1])
                    del self.actions[int_time]
            time.sleep(10)

    def add_action(self, time, command, commands):
        self.actions[time] = [command,commands]
