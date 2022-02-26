from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options

import json

class Interface:
    def __init__(self, url: str, size: int) -> None:
        self.size = size
        # Setting prefs for log reading
        cap = DesiredCapabilities.FIREFOX
        cap['loggingPrefs'] = {'browser':'ALL'}

        opts = Options()
        opts.log.level = "trace"

        self.browser = webdriver.Firefox(capabilities = cap, options = opts)
        self.browser.get(url)

        # Setting up keyboard input
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
    
    def restart(self) -> None:
        actions = ActionChains(self.browser)
        actions.send_keys("r")
        actions.perform()

    
    def grid(self) -> dict:
        tiles = []
        data = json.loads(self.browser.find_element_by_id("this-better-work").text)
        
        for row in range(0, self.size):
            temp = []
            for column in range(0, self.size):
                # If tile object
                if type(data["grid"]["cells"][column][row]) is dict:
                    temp.append(data["grid"]["cells"][column][row]["value"])
                # If null
                else:
                    temp.append(0)
            
            tiles.append(temp)
        
        data["grid"] = tiles
        
        return data