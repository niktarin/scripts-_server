import time

from base_tread import Base_tr


class Create_fan_page_tr(Base_tr):

    def run(self):

        if not self.check():
            try:
                self.driver.quit()
            except:
                pass
            return

        self.driver.get("https://business.facebook.com/settings/pages")

        xpath = "//button[@data-testid='AddAssetButton-brands/menuRoot']"
        if not self.click_to_xpath(xpath):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
            return

        xpath = "//li[@class='_54ni _3jgh __MenuItem'][3]"
        if not self.click_to_xpath(xpath):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
            return

        xpath = f"(//div[@class='_4_uj'])[{self.settings['page_category']}]"
        if not self.click_to_xpath(xpath):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
            return

        if self.settings["page_category"] == 1:
            pass
            # xpath = "//input[@name='page_name']"
            # if not self.set_text(xpath, self.settings["page_name"]):
            #     self.answer["status"] = "Ошибка"
            #     self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
            #     return (False)
            #
            # xpath = "//div[@id='u_4r_4']"
            # if not self.click_to_xpath(xpath):
            #     self.answer["status"] = "Ошибка"
            #     self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
            #     return
            #
            # xpath = f"//span[text()='{self.settings['company_topic']}']"
            # if not self.click_to_xpath(xpath):
            #     self.answer["status"] = "Ошибка"
            #     self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
            #     return
            #
            #
            # xpath = "//input[@name='address']"
            # if not self.set_text(xpath, self.settings["address"]):
            #     self.answer["status"] = "Ошибка"
            #     self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
            #     return (False)
            #
            # xpath = "//input[@name='city']"
            # if not self.set_text(xpath, self.settings["city"]):
            #     self.answer["status"] = "Ошибка"
            #     self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
            #     return (False)
            #
            # xpath = "//input[@name='zip']"
            # if not self.set_text(xpath, self.settings["zip"]):
            #     self.answer["status"] = "Ошибка"
            #     self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
            #     return (False)


        else:
            xpath = "//input[@name='page_name']"
            if not self.set_text(xpath, self.settings["page_name"]):
                self.answer["status"] = "Ошибка"
                self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
                return (False)

            xpath = "//div[@class='_6a _6b uiPopover']"
            if not self.click_to_xpath(xpath):
                self.answer["status"] = "Ошибка"
                self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
                return

            xpath = f"//span[text()='{self.settings['company_topic']}']"
            if not self.click_to_xpath(xpath):
                self.answer["status"] = "Ошибка"
                self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
                return

        xpath = "//button[@class='_42ft _42fu layerConfirm uiOverlayButton selected _42g- _42gy']"
        if not self.click_to_xpath(xpath):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
            return

        xpath = f"(//div[text()='{self.settings['page_name']}']/..)[1]"
        if not self.click_to_xpath(xpath, circle=100, time_sleep=2):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
            return

        xpath = "//button[@class='_271k _271m _1qjd _7tvm _7tv2 _7tv4']"
        if not self.click_to_xpath(xpath):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
            return

        step = 0
        while True:
            url = self.driver.current_url
            if "business_id" in url:
                break
            else:
                step += 1
                time.sleep(1)
            if step >= 30:
                break

        url = self.driver.current_url
        url = url.replace("business.", "")
        index = url.find("/?")
        if index >= 0:
            url = url[:index]

        self.answer["fan_page_href"] = url
        self.answer["status"] = "Выполнен"
        self.answer["comment"] = "Фан пейдж через БМ создана"
        self.driver.quit()
