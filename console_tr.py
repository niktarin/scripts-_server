import random
from threading import Thread


class consol_tr(Thread):

    commands = {"print_log": "Вывод лога в консоль",
                "log_append": "Добавить комментарий в лог",
                "save_to_file":"Запись лога в файл"}

    def __init__(self, main_tr, log):
        Thread.__init__(self)
        self.log = log
        self.main_tr = main_tr

    def check_command(self, command):
        start_command = command

        command = command.replace(" ", "")
        command = command.split("=")




        type_command = command[0]
        if len(command) > 1:
            value_command = command[1]
        else:
            value_command = ""

        if type_command not in self.commands:
            print("Не действительная комманда")
            return

        if type_command == "print_log":
            if value_command != "":
                value_command = value_command.replace("[","")
                value_command = value_command.replace("]","")
                value_command = value_command.split(",")
                print(value_command)
            else:
                value_command = []
            self.log.log_append(start_command)
            self.log.print_log(value_command)

        elif type_command == "log_append":
            if value_command == "":
                print("Не действительная комманда")
                return
            self.log.log_append(value_command)
            print("Комманда принята")

        elif type_command == "save_to_file":
            if value_command != "":
                value_command = value_command.replace("[","")
                value_command = value_command.replace("]","")
                value_command = value_command.split(",")
                print(value_command)
            else:
                value_command = []

            self.log.save_to_file(names=value_command)
            print("Комманда принята")

    def run(self):
        while True:
            command = input()
            self.check_command(command)
