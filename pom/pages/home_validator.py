__author__ = 'Daniel Mevs'
from selenium.webdriver.common.by import By
from .base_page import BasePage
from .nav_bar import NavBar


class HomeValidator(BasePage):
    """
    For validating that we are indeed at the 
    home page
    """
    CONFIG_TEXT_SPAN = (By.CSS_SELECTOR, 'h1.col-md-12.no-pad')
    MAGIC_STRING = 'No config was found for this customer.'
    
    # - Confirm successful login
    def is_home(self, username: str) -> bool:
        username = self.get_username(username)
        message_shown = self.MAGIC_STRING == self.wait_for(
            self.CONFIG_TEXT_SPAN
        ).get_attribute("textContent")
        nav_bar = NavBar(self.driver)
        
        username_shown = nav_bar.is_username_shown(username)
        return message_shown and username_shown
    
    def get_username(self, username: str) -> str:
        return username.split('@')[0]
