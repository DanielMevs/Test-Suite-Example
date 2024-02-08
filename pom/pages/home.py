__author__ = 'Daniel Mevs'
from .base_page import BasePage
from .form_authentication import FormAuthentication


class Home(BasePage):
    """
    For getting started with the website
    """

    def go_to_login(self, url: str) -> None:
        self.driver.get(url)
        return FormAuthentication(self.driver)
    
    

    
