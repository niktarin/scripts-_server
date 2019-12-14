from scripts_v2.base_tread_v2 import Base_tr
import random


class Likes(Base_tr):

    def stop(self):
        self.flag_work = False

    def likes(self):

        self.scroll_page_down(100)
        self.scroll_page_up(100)

        xpath = "//span[@class='_1mto']/div[@class='_khz _4sz1 _4rw5 _3wv2']/a"
        elements_1 = self.driver.find_elements_by_xpath(xpath)

        xpath = "//div[@data-testid='UFI2ReactionLink/actionLink']/div/a"
        elements_2 = self.driver.find_elements_by_xpath(xpath)

        lenght_1 = len(elements_1)
        lenght_2 = len(elements_2)

        elements = elements_1 if lenght_1 >= lenght_2 else elements_2
        lenght = lenght_1 if lenght_1 >= lenght_2 else lenght_2

        if lenght == 0:
            return True

        maximum = int(self.settings["likes_max"])
        minimum = int(self.settings["likes_min"])

        maximum = maximum if maximum < lenght else lenght
        minimum = minimum if minimum < lenght else lenght

        if maximum < minimum:
            minimum, maximum = maximum, minimum

        likes = random.randint(minimum, maximum)
        likes = likes if likes < len(elements) else len(elements)

        for index in range(likes):
            element = elements[index]
            self.click_to_element(element)
        return True

    def pages_V1(self):

        if "fan_pages_scroll" not in self.settings:
            return True

        for link in self.settings["fan_pages_scroll"]:
            link.replace(" ", "")
            if link == "":
                continue
            try:
                self.get_link(link)
                self.click_esc()
                self.scroll_page_down(100)
                self.scroll_page_up(100)
                self.likes()
            except:
                pass
        return True

    def page_v2(self):
        file_groups = ".\\data\\listGroup.txt"
        file_account = ".\\data\\listAccount.txt"

        links = []
        try:
            f = open(file_groups, "r")
        except:
            self.log.log_append(
                {"name": self.tech_name, "action": "load_file", "text": "не удалось загрузить файл с группами"})
            return False

        for link in f:
            if link == "\n":
                continue
            links.append(link.replace("\n", ""))

        random.shuffle(links)

        for i in range(2):
            link = links[i]
            self.get_link(link)
            self.likes()

        links = []
        try:
            f = open(file_account, "r")
        except:
            self.log.log_append(
                {"name": self.tech_name, "action": "load_file", "text": "не удалось загрузить файл с группами"})
            return False

        for link in f:
            if link == "\n":
                continue
            links.append(link.replace("\n", ""))

        random.shuffle(links)

        for i in range(2):
            link = links[i]
            self.get_link(link)
            self.likes()

    def run(self):
        try:
            if not self.check():
                return
            self.page_v2()
            self.answer["comment"] = ""
            self.answer["status"] = "Выполнен"
        except:
            self.log.log_append(
                {"name": self.tech_name, "action": "error", "text": "Не предвиденная ошибка потока сценария"})
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = "Не предвиденная ошибка потока сценария"
