import re
from threading import Thread


class consol_tr(Thread):
    commands = {"print_log": "Вывод лога в консоль (names) ",
                "log_append": "Добавить комментарий в лог (text name action)",
                "save_to_file": "Запись лога в файл (file_name flag names)",
                "help": "Вывод информации",
                "log_file": " log_file_name название ",
                "save_auto": "Автоматомсохранятьв файл (flag True\False)",
                "treads": "количество потоков (max)"}

    def __init__(self, main_hab):
        Thread.__init__(self)
        self.main_hab = main_hab

    def check_command(self, command):
        regex = re.compile(r"\b(\w+)\s*:\s*([^:]*)(?=\s+\w+\s*:|$)")
        commands = dict(regex.findall(command))
        for i in commands:
            commands[i] = commands[i].replace(" ", "")

        if "command" not in commands:
            print("Ключевое слово 'command' не найдено")
            return

        type_command = commands["command"]

        if type_command not in self.commands:
            print(f"Команда {type_command} не найдена")
            return

        if type_command == "print_log":
            answer = self.main_hab.log.print_log(commands)
            for arr in answer:
                an = f"{arr['name']} {arr['time']} {arr['action']} {arr['text']}"
                print(an)
            leng = len(answer)
            if leng > 0:
                print(f"Запсей:{leng}\nКонец")
            else:
                print("Не найденно записей")

        elif type_command == "log_append":
            answer = self.main_hab.log.log_append(commands)
            print(answer)

        elif type_command == "save_to_file":
            answer = self.main_hab.log.save_to_file(commands)
            print(answer)

        elif type_command == "help":
            for i in self.commands:
                print(i, "-", self.commands[i])

        elif type_command == "log_file":
            answer = self.main_hab.log.log_file(commands)
            print(answer)

        elif type_command == "save_auto":
            answer = self.main_hab.log.save_auto(commands)
            print(answer)

        elif type_command == "treads":
            if "max" not in commands:
                answer = self.main_hab.max_tread
                print(f"Потоков:{answer}")
            else:
                try:
                    val = int(commands["max"])
                    self.main_hab.max_tread = val
                    print(f"Потоков:{self.main_hab.max_tread}")
                except:
                    print("Ошибка")
                    return

    def run(self):
        while True:
            command = input()
            self.check_command(command)
# command:treads max:4
# command:log_append text:trololo2 name:console
# command:print_log names:console
# command:save_to_file names:console,console2 file_name:trololo.txt
# command:log_file log_file_name:trololo2.txt
