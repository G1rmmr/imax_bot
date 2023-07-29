# imports
from selenium import webdriver as wd
from selenium.webdriver.chrome.service import Service as serv
from webdriver_manager.chrome import ChromeDriverManager as cdm

import bot

class Device:
    # Functions
    def __init__(self):
        # chrome device settings
        self.driver = wd.Chrome(service=serv(cdm().install()),
                           options=wd.ChromeOptions())
        
        self.bot = bot.Bot()

    def check_imax(self, movie_namem):
        # ERROR check
        try:
            # Get Movie data
            self.driver.switch_to.frame("ifrm_movie_time_table")
            xpath = "//div[@class='sect-showtimes']"

            # Check IMAX
            is_imax_available = self.driver.find_element(
                "xpath", xpath).text.find("IMAX")
            
            if is_imax_available:
                self.bot.sendSelf("OPPENHIMER IMAX, NOW Available!!!\n"
                                  + self.driver.current_url)
                return True
            
            else:
                self.bot.sendSelf("IMAX Not Available")
                return False
        except:
            self.bot.sendSelf("Your bot can't find IMAX data")
            return False