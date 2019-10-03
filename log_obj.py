from datetime import datetime


class log:
    log_arr = []
    v = "v0.1"
    log_file_name = ".\log\log.txt"
    auto_save_flag = False

    def save_auto(self, commands):
        if "flag" in commands:
            self.auto_save_flag = commands["flag"]
            return (f"Установленн флаг {self.auto_save_flag}")
        else:
            return ("Flag а не найден")

    def log_file(self, commands):
        if "log_file_name" in commands:
            self.log_file_name = f"{commands['log_file_name']}"
            return ("Лог файл изменен")
        else:
            return (self.log_file_name)

    def log_append(self, commands):

        if "text" not in commands:
            return ("Значение 'text' не найденно")
        else:
            text = commands["text"]

        if "name" not in commands:
            name = "console"
        else:
            name = commands["name"]

        if "action" not in commands:
            action = 'commant'
        else:
            action = commands["action"]

        now = datetime.now()
        time = now.strftime("%d/%m/%Y %H:%M:%S")

        log_arr = {"name": name, "time": time, "action": action, "text": text}
        self.log_arr.append(log_arr)

        if self.auto_save_flag:
            log_file = open(self.log_file_name, "a")
            file_string = f"{log_arr['name']} {log_arr['time']} {log_arr['action']} {log_arr['text']}\n"
            log_file.write(file_string)
            log_file.close()

        return ("Команда принята")

    def print_log(self, commands):
        if "names" in commands:
            names = commands["names"]
            names = names.split(",")
        else:
            names = []

        if len(names) == 0:
            return self.log_arr
        else:
            ans = []
            for arr in self.log_arr:
                if arr["name"] in names:
                    ans.append(arr)
            return (ans)

    def save_to_file(self, commands):

        if "file_name" not in commands:
            file_name = self.log_file_name
        else:
            file_name = commands["file_name"]

        if "flag" not in commands:
            flag = "a"
        else:
            flag = commands["flag"]
            # TODO проверка флагов

        log_file = open(file_name, flag)
        if "names" in commands:
            names = commands["names"]
            names = names.split(",")
        else:
            names = []

        if len(names) == 0:
            for arr in self.log_arr:
                file_string = f"{arr['name']} {arr['time']} {arr['action']} {arr['text']}\n"
                log_file.write(file_string)
        else:
            for arr in self.log_arr:
                if arr["name"] in names:
                    file_string = f"{arr['name']} {arr['time']} {arr['action']} {arr['text']}\n"
                    log_file.write(file_string)

        log_file.close()
        return ("Команда принята")

    def __repr__(self):
        print(f"def log {self.v}", end="\n")
