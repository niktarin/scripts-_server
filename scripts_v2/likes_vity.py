from scripts_v2.base_tread_v2 import Base_tr
import random


class Likes_vity(Base_tr):

    def likes(self, minimum=1, maximum=2):

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

    def account_serf(self):
        links = []
        for link in self.file_account:
            if link == "\n":
                continue
            links.append(link.replace("\n", ""))

        random.shuffle(links)
        link = links[0]
        self.get_link(link)
        scroll = random.randint(50, 150)
        self.scroll_page_down(scroll)
        self.scroll_page_up(scroll)
        self.likes()

    def self_serf(self):
        xpath = "//span[@class='_2md']"
        if not self.click_to_xpath(xpath, appointment="переход на личную страницу"):
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = self.error_comment
            return False

        scroll = random.randint(50, 150)
        self.scroll_page_down(scroll)
        self.scroll_page_up(scroll)

    def fp_serf(self):
        links = []
        for link in self.file_fp:
            if link == "\n":
                continue
            links.append(link.replace("\n", ""))
        random.shuffle(links)
        link = links[0]
        self.get_link(link)

        xpath = "//button[@data-testid='page_profile_follow_button_test_id']"
        self.click_to_xpath(xpath)

        scroll = random.randint(50, 150)
        self.scroll_page_down(scroll)
        self.scroll_page_up(scroll)
        self.likes(maximum=1)

    def load_data(self):
        self.file_account_path = ".\\data\\listAccount.txt"
        self.file_fp_path = ".\\data\\listFP.txt"

        try:
            self.file_account = open(self.file_account_path, "r")
            self.file_fp = open(self.file_fp_path, "r")
        except:
            self.log.log_append(
                {"name": self.tech_name, "action": "load_file", "text": "не удалось загрузить файл с группами"})
            return False

    def run(self):
        try:
            if not self.check():
                return

            self.load_data()
            choice = random.choice([True, False])
            if choice:
                self.account_serf()
            self.self_serf()
            self.fp_serf()
            self.self_serf()

            self.answer["comment"] = ""
            self.answer["status"] = "Выполнен"
        except:
            self.log.log_append(
                {"name": self.tech_name, "action": "error", "text": "Не предвиденная ошибка потока сценария"})
            self.answer["status"] = "Ошибка"
            self.answer["comment"] = "Не предвиденная ошибка потока сценария"
