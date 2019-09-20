from datetime import datetime


class log:
    log_arr = []
    v = "v0.1"

    def __init__(self, ftp_ip=None):
        self.ftp_ip = ftp_ip

    def log_append(self, commands):
        if "text" not in commands:
            return False
        else:
            text = commands["text"]

        if "name" not in commands:
            return False
        else:
            name = commands["name"]

        now = datetime.now()
        d = now.strftime("%d/%m/%Y %H:%M:%S")

        log_arr = [d, name, text]
        self.log_arr.append(log_arr)

    def print_log(self, commands):
        if "names" in commands:
            names = commands["names"]
            names = names.split(",")
        else:
            names = []

        if len(names) == 0:
            for arr in self.log_arr:
                print(f"{arr[0]} {arr[1]} {arr[2]}")
        else:
            for arr in self.log_arr:
                if arr[1] in names:
                    print(f"{arr[0]} {arr[1]} {arr[2]}")

    def save_to_file(self, commands):

        if "file_name" not in commands:
            file_name = f"{self.ftp_ip}_log.txt"
        else:
            file_name = commands["file_name"]

        if "flag"not in commands:
            flag = "a"
        else:
            flag = commands["flag"]

        log_file = open(file_name, flag)
        if "names" in commands:
            names = commands["names"]
            names = names.split(",")
        else:
            names = []

        if len(names) == 0:
            for arr in self.log_arr:
                file_string = f"{arr[0]} {arr[1]} {arr[2]} \n"
                log_file.write(file_string)
        else:
            for arr in self.log_arr:
                if arr[1] in names:
                    file_string = f"{arr[0]} {arr[1]} {arr[2]}"
                    log_file.write(file_string)

        log_file.close()

    def __repr__(self):
        print(f"def log {self.v}", end="\n")

