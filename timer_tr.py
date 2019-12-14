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
            for float_time in actions:
                if float_time < time.time():
                    action = actions[float_time][0]
                    try:
                        action(actions[float_time][1])
                    except:
                        pass
                    del self.actions[float_time]
            time.sleep(10)

    def add_action(self, time, command, commands):

        self.actions[time] = [command,commands]
        print(self.actions)