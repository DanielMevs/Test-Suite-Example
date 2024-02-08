__author__ = 'Daniel Mevs'
from selenium.webdriver.common.by import By
from .base_page import BasePage
from .helpers.name_generator import get_random_name
from .helpers.file_writer import write_file
from .new_user_form import NewUserForm

"""For the new Customer created"""


class NewCustomer(BasePage):
    CUSTOMERS_ADD_BTN = (By.CSS_SELECTOR, '.btn.btn-primary')
    CUSTOMER_INPUT_SAVE_CUSTOMER = (By.CSS_SELECTOR, '#save-customer')
    
    def add_customer(self):
        self.wait_for(self.CUSTOMERS_ADD_BTN).click()
        form = NewUserForm(self.driver)

        password = form.get_password()
        # - Get random username 
        new_user = get_random_name() 
        # - Fill out the form
        form.enter_name(new_user)
        form.enter_s3_folder(get_random_name())
        email = form.get_email()
        # - Save new creds in a file to log in later
        write_file(email, password)
        # - Create/save new customer
        self.wait_for(self.CUSTOMER_INPUT_SAVE_CUSTOMER).click()

    