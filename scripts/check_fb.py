from scripts.base_tread import Base_tr

class Check_fb(Base_tr):

        
    def run(self):

        if not self.check():
            try:
                self.driver.quit()
            except :
                pass
            return


        self.answer["comment"] = "Аккаунт не забанен"
        self.answer["status"] = "Выполнен"
        self.driver.quit()
