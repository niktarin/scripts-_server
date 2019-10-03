from scripts_v2.base_tread_v2 import Base_tr
import random
import time

class Simple_update_fb(Base_tr):

    def start_page_scroll(self):
        self.click_esc()
        down = random.randint(50, 300)
        self.scroll_page_down(down)
        self.scroll_page_up(down)
        return True

    def fan_page_scroll(self):
        self.click_esc()

        if "fan_pages_scroll" not in self.settings:
            return (True)

        for link in self.settings["fan_pages_scroll"]:
            link.replace(" ", "")
            if link == "":
                return (True)
            try:
                self.driver.get(link)
                self.click_esc()
                down = random.randint(50, 300)
                self.scroll_page_down(down)
                self.scroll_page_up(down)
            except:
                pass

        return (True)

    def friends_page_scroll(self):
        self.driver.get("https://www.facebook.com/find-friends/browser/")
        self.click_esc()
        down = random.randint(15, 200)
        self.scroll_page_down(down)
        self.scroll_page_up(down)
        return True

    def refresh(self):
        ran = random.randint(1, 2)
        t = random.randint(10, 20)
        for i in range(ran):
            self.driver.refresh()
            time.sleep(t)

    def run(self):

        if not self.check():
            return

        arr_action = [self.start_page_scroll,
                      self.fan_page_scroll,
                      self.friends_page_scroll]

        random.shuffle(arr_action)

        for act in arr_action:
            if not act():
                return
            self.refresh()

        self.answer["comment"] = "Пустое обновление прошло успешно"
        self.answer["status"] = "Выполнен"
        self.driver.quit()


        # xpath = "//span[@class='_2md']"
        # if not self.click_to_xpath(xpath):
        #     self.answer["status"] = "Ошибка"
        #     self.answer["comment"] = self.error_comment
        #     return False