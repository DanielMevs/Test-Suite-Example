__author__ = 'Daniel Mevs'
from selenium.webdriver.common.by import By
from .base_page import BasePage


class NewUserForm(BasePage):
    """
    For the form that appears when a customer
    click "Add New Customer"
    """
    
    CUSTOMER_INPUT_EMAIL = (By.CSS_SELECTOR, 'input#email')
    CUSTOMER_INPUT_PASSWORD = (By.CSS_SELECTOR, '[name="password"]')
    CUSTOMER_INPUT_NAME = (By.CSS_SELECTOR, 'input#name')
    CUSTOMER_INPUT_S3_FOLDER = (By.CSS_SELECTOR, '[name="s3_folder"]')

    def get_email(self) -> str:
        email = self.wait_for(self.CUSTOMER_INPUT_EMAIL)
        return str(email.get_attribute('value'))
        
    def get_password(self) -> str:
        password = self.wait_for(self.CUSTOMER_INPUT_PASSWORD)
        return str(password.get_attribute('value'))
    
    def enter_name(self, new_user: str) -> str:
        self.find(self.CUSTOMER_INPUT_NAME).send_keys(new_user)

    def enter_s3_folder(self, random_path: str) -> None:
        self.find(self.CUSTOMER_INPUT_S3_FOLDER).send_keys(
            random_path
        )
   
    