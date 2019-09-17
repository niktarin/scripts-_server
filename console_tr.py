import random
import re
from threading import Thread


class consol_tr(Thread):
    commands = {"print_log": "Вывод лога в консоль",
                "log_append": "Добавить комментарий в лог",
                "save_to_file": "Запись лога в файл"}

    flags = ["-u", "-w", "-a", "-f"]

    def __init__(self, main_tr, log):
        Thread.__init__(self)
        self.log = log
        self.main_tr = main_tr

    def check_command(self, command):
        regex = re.compile(r"\b(\w+)\s*:\s*([^:]*)(?=\s+\w+\s*:|$)")
        commands = dict(regex.findall(command))
        for i in commands:
            commands[i] = commands[i].replace(" ","")


        if "command" not in commands:
            print("Команда не опознана")
            return

        elif  commands["command"] not in self.commands:

            print(commands["command"])
            print(self.commands[commands["command"]])

            print("Команда не йдена")
            return

        type_command = commands["command"]

        if type_command not in self.commands:
            print("Не действительная комманда")
            return

        if type_command == "print_log":
            self.log.print_log(commands)
            print("Комманда принята")

        elif type_command == "log_append":
            self.log.log_append(commands)
            print("Комманда принята")

        elif type_command == "save_to_file":
            self.log.save_to_file(commands)
            print("Комманда принята")

    def run(self):
        while True:
            command = input()
            self.check_command(command)
