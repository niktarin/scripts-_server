import requests
from base_tread import Base_tr

class Create_accaunts_in_ml(Base_tr):
    token = "57e44d8f5a5b87b653a0801353fbe54706e92575"
    ml_accaunts = {}
    def run(self):
        for accaunt in self.settings["accaunts"]:
            name = accaunt["name"]
            host = accaunt["host"]
            port = accaunt["port"]
            username = accaunt["username"]
            password = accaunt["password"]

            post_data = {
                "name": name,
                "browser": "mimic",
                "os": "win",
                "network": {
                    "proxy": {
                        "type": "HTTP",
                        "host": host,
                        "port": port,
                        "username": username,
                        "password":password}}}
            answear = requests.post(
                f"https://api.multiloginapp.com/v2/profile?token={self.token}&defaultMode=FAKE",
                json=post_data)
            code = answear.status_code
            if code == 200:
                ml_token = answear.json()["uuid"]
                self.ml_accaunts["name"] = ml_token
            else:
                self.ml_accaunts["name"] = "token error"

        self.answer["accaunts"] = self.ml_accaunts
        self.answer["status"] = "Выполнен"
        self.answer["comment"] = "Аккаунты добавленны в Мультилогин"
        self.driver.quit()


