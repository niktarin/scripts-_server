from datetime import datetime


class log:
    log_arr = []
    v = "v0.1"

    def __init__(self, ftp_ip=None):
        self.ftp_ip = ftp_ip

    def log_append(self, log_str, tech_name="console"):
        now = datetime.now()
        d = now.strftime("%d/%m/%Y %H:%M:%S")
        log_arr = [d, tech_name, log_str]
        self.log_arr.append(log_arr)

    def print_log(self, names):

        if len(names) == 0:
            for arr in self.log_arr:
                print(f"{arr[0]} {arr[1]} {arr[2]}")
        else:
            for arr in self.log_arr:
                if arr[1] in names:
                    print(f"{arr[0]} {arr[1]} {arr[2]}")

    def save_to_file(self, names, file_add_text = True, file_name="log.txt"):
        if file_add_text:
            flag = "a"
        else:
            flag = "w"

        log_file = open(file_name, flag)

        if len(names) == 0:
            for arr in self.log_arr:
                file_string = f"{arr[0]} {arr[1]} {arr[2]}"
                log_file.write(file_string)
        else:
            for arr in self.log_arr:
                if arr[1] in names:
                    file_string = f"{arr[0]} {arr[1]} {arr[2]}"
                    log_file.write(file_string)

        log_file.close()

    def __repr__(self):
        print(f"def log {self.v}", end="\n")
