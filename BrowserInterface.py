from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

class Interface:
    def __init__(self, url: str) -> None:
        self.browser = webdriver.Firefox()
        self.browser.get(url)
        self.input = self.browser.find_element_by_class_name("container")
    
    def move(self, direction: str) -> None:
        keymap = {
            "up": "w",
            "down": "s",
            "left": "a",
            "right": "d"
        }

        actions = ActionChains(self.browser)
        actions.send_keys(keymap[direction])
        actions.perform()