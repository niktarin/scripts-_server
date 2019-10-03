from scripts.base_tread import Base_tr


class Create_advertising(Base_tr):

    def standart_start(self):
        self.driver.get("https://business.facebook.com/adsmanager/")

        for i in range(2):
            xpath = "//button[@class='_42d_ _32qq _3n5r layerCancel']"
            self.driver.find_element_by_xpath(xpath).click()

        xpath = "(//button[@class='_271k _271m _1qjd _7tvm _7tv3 _7tv4'])[2]"
        if not self.click_to_xpath(xpath):
            self.answer["comment"] = f"Время исчерпано не удалось найти {xpath}"
            self.answer["status"] = "Ошибка"
            return (False)

        xpath = "//button[@data-testid='select-guided-creation-button']"
        if not self.click_to_xpath(xpath):
            self.answer["comment"] = f"Время исчерпано не удалось найти {xpath}"
            self.answer["status"] = "Ошибка"
            return (False)

        xpath = f"//div[@id='AdsCFObjectiveSelectorItemContainer-{self.settings['company_type']}]"
        if not self.click_to_xpath(xpath):
            self.answer["comment"] = f"Время исчерпано не удалось найти {xpath}"
            self.answer["status"] = "Ошибка"
            return (False)

        xpath = "//input[@data-testid='edit-name-field']"
        if not self.set_text(xpath, self.settings['company_name']):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
            return (False)

        xpath = f"//li[@id='CAMPAIGN_AUCTION_PROMOTED_OBJECT_SECTION']"
        if not self.click_to_xpath(xpath):
            self.answer["comment"] = f"Время исчерпано не удалось найти {xpath}"
            self.answer["status"] = "Ошибка"
            return (False)

        xpath = "//input[@data-testid='edit-name-field']"
        if not self.set_text(xpath, self.settings['ad_group_name']):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
            return (False)
        return (True)

    def traffic_settings(self):
        xpath = f"//div[@data-value='WEBSITE']"
        if not self.click_to_xpath(xpath):
            self.answer["comment"] = f"Время исчерпано не удалось найти {xpath}"
            self.answer["status"] = "Ошибка"
            return (False)

    def audience_settings(self):

        xpath = "(//label[@class='_58ak _3ct8']/input[@class='_58al'])[1]"
        if not self.set_text(xpath, self.settings['custom_audience']):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
            return (False)

        # TODO полные настройни локации
        xpath = "(//label[@class='_58ak _3ct8']/input[@class='_58al'])[2]"
        if not self.set_text(xpath, self.settings['country_name']):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = f"Время исчерпано, не удалось найти {xpath}"
            return (False)

        #########################################################
        if self.settings['pol'] == "male":
            xpath = f"(//div[@data-testid='gender_selector']/div[@class='_7ztw _1-qs']/button)[2]"
            if not self.click_to_xpath(xpath):
                self.answer["comment"] = f"Время исчерпано не удалось найти {xpath}"
                self.answer["status"] = "Ошибка"
                return (False)


        elif self.settings['pol'] == "female":
            xpath = f"(//div[@data-testid='gender_selector']/div[@class='_7ztw _1-qs']/button)[1]"
            if not self.click_to_xpath(xpath):
                self.answer["comment"] = f"Время исчерпано не удалось найти {xpath}"
                self.answer["status"] = "Ошибка"
                return (False)

        else:
            xpath = f"(//div[@data-testid='gender_selector']/div[@class='_7ztw _1-qs']/button)[1]"
            if not self.click_to_xpath(xpath):
                self.answer["comment"] = f"Время исчерпано не удалось найти {xpath}"
                self.answer["status"] = "Ошибка"
                return (False)
        return True

    def placements(self):
        xpath = f"//div[@data-value='manual']"
        if not self.click_to_xpath(xpath):
            self.answer["comment"] = f"Время исчерпано не удалось найти {xpath}"
            self.answer["status"] = "Ошибка"
            return (False)

        check_array = [
            "//div[@id='placement-facebook']",
            "//div[@id='placement-instagram']",
            "//div[@id='placement-audience_network']",
            "//div[@id='placement-checkbox-messenger']"]

        for xpath in check_array:
            if not self.click_to_xpath(xpath):
                self.answer["comment"] = f"Время исчерпано не удалось найти {xpath}"
                self.answer["status"] = "Ошибка"
                return (False)

        if "placement-facebook" in self.settings['platforms']:
            xpath = f"//div[@data-value='manual']"
            if not self.click_to_xpath(xpath):
                self.answer["comment"] = f"Время исчерпано не удалось найти {xpath}"
                self.answer["status"] = "Ошибка"
                return (False)

        if "placement-instagram" in self.settings['platforms']:
            xpath = f"//div[@id='placement-instagram']"
            if not self.click_to_xpath(xpath):
                self.answer["comment"] = f"Время исчерпано не удалось найти {xpath}"
                self.answer["status"] = "Ошибка"
                return (False)

        if "placement-audience_network" in self.settings['platforms']:
            xpath = f"//div[@id='placement-audience_network']"
            if not self.click_to_xpath(xpath):
                self.answer["comment"] = f"Время исчерпано не удалось найти {xpath}"
                self.answer["status"] = "Ошибка"
                return (False)

        if "placement-checkbox-messenger" in self.settings['platforms']:
            xpath = f"//div[@id='placement-checkbox-messenger']"
            if not self.click_to_xpath(xpath):
                self.answer["comment"] = f"Время исчерпано не удалось найти {xpath}"
                self.answer["status"] = "Ошибка"
                return (False)

        #Места размещения
        if "feed" not in self.settings["Placements"]:
            xpath = f"//div[@id='placement-feed']"
            if not self.click_to_xpath(xpath):
                self.answer["comment"] = f"Время исчерпано не удалось найти {xpath}"
                self.answer["status"] = "Ошибка"
                return (False)

        if "story" not in self.settings["Placements"]:
            xpath = f"//div[@id='placement-story']"
            if not self.click_to_xpath(xpath):
                self.answer["comment"] = f"Время исчерпано не удалось найти {xpath}"
                self.answer["status"] = "Ошибка"
                return (False)

        if "context" not in self.settings["Placements"]:
            xpath = f"//div[@id='placement-context']"
            if not self.click_to_xpath(xpath):
                self.answer["comment"] = f"Время исчерпано не удалось найти {xpath}"
                self.answer["status"] = "Ошибка"
                return (False)

        if "external" not in self.settings["Placements"]:
            xpath = f"//div[@id='placement-external']"
            if not self.click_to_xpath(xpath):
                self.answer["comment"] = f"Время исчерпано не удалось найти {xpath}"
                self.answer["status"] = "Ошибка"
                return (False)
        return True

    def budget_and_schedule(self):
        xpath = f"//li[@id='CAMPAIGN_AUCTION_PRICING_SECTION']"
        if not self.click_to_xpath(xpath):
            self.answer["comment"] = f"Время исчерпано не удалось найти {xpath}"
            self.answer["status"] = "Ошибка"
            return (False)

        xpath = f"//div[@data-testid='optimization-goal-nested-selector']/button"
        if not self.click_to_xpath(xpath):
            self.answer["comment"] = f"Время исчерпано не удалось найти {xpath}"
            self.answer["status"] = "Ошибка"
            return (False)

    def run(self):
        if not self.check():
            try:
                self.driver.quit()
            except:
                pass
            return

        if not self.standart_start():
            self.driver.quit()
            return

        flag = False
        if self.settings['company_type'] == "traffic":
            flag = self.traffic_settings()

        if not flag:
            self.driver.quit()
            return

        if not self.audience_settings():
            self.driver.quit()
            return

        if not self.placements():
            self.driver.quit()
            return

        if not self.budget_and_schedule():
            self.driver.quit()
            return


