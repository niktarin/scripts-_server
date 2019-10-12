from .base_tread import Base_tr
import os
import pandas as pd
import base64
class Load_companies_tr(Base_tr):

    def run(self):

        if not self.check():
            try:
                self.driver.quit()
            except:
                pass
            return

        self.driver.get("business.facebook.com/adsmanager/manage/all")
        xpath = "_42d_ _32qq _3n5r layerCancel"
        self.click_to_xpath(xpath)

        for companie_name in self.settings["companies_names"]:
            xpath = f"(//*[text()='{companie_name}']/../../../../../../../../../../div)[1]//input[@class='_7_o0']"
            self.click_to_xpath(xpath)

        xpath = "//button[@data-testid='ads-export-button']"
        if not self.click_to_xpath(xpath):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
            return

        xpath = "//button[@data-testid='export-confirm-button']"
        if not self.click_to_xpath(xpath):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
            return

        time.sleep(5)


        downloads_dir = "C:\\Users\\Administrator\\Downloads"
        files = os.listdir(downloads_dir)
        file = None
        for file_name in files:
        if "export_" in file_name:
            file = file_name
            break

        data = pd.read_csv(f'{downloads_dir}\\{file_name}', sep='	', encoding='utf-16')
        del data["Campaign ID"]
        del data["Ad Set ID"]
        del data["Ad ID"]
        del data["Link"]

        local_file = "test.csv"

        data.to_csv(local_file, sep='	',encoding='utf-16',index=False)
        data = open(local_file, 'rb').read()

        os.remove(f"{downloads_dir}\\{file_name}")
        os.remove(local_file)

        self.answer["output_data"]["csv_in_bytes"] = data
        self.answer["status"] = "Выполнен"
        self.answer["comment"] = "Данные компаний получены"
        self.driver.quit()