__author__ = 'Daniel Mevs'
from selenium.webdriver.common.by import By
from .base_page import BasePage


class FormAuthentication(BasePage):
    """
    For authenticating existing users
    """
    
    USER_EMAIL_SELECTOR = (By.CSS_SELECTOR, '#email')
    PASS_WORD_SELECTOR = (By.CSS_SELECTOR, '#password')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, '#submit')

    def login(self, username: str, password: str) -> None:
        # - Enter username
        user_email = self.wait_for(self.USER_EMAIL_SELECTOR)
        user_email.send_keys(username)
        # - Enter password
        pass_word = self.find(self.PASS_WORD_SELECTOR)
        pass_word.send_keys(password)
        # - Click submit
        self.find(self.SUBMIT_BUTTON).click()








