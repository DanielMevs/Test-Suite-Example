__author__ = 'Daniel Mevs'
from selenium.webdriver.common.by import By
from .base_page import BasePage


class NavBar(BasePage):
    """
    For the nav bar and all its functions
    """

    CUSTOMERS_NAV_BTN = (By.CSS_SELECTOR, 'a.dropdown-toggle')
    CUSTOMERS_DROPDOWN_LIST = (By.CSS_SELECTOR, 'ul .dropdown-menu li')
    ACCNT_NAME_DROPDOWN = (By.CSS_SELECTOR, 'a#navbar-login-menu')
    LOGOUT_BTN_DROPDOWN = (By.CSS_SELECTOR, 'ul.dropdown-menu')

    def go_to_list(self) -> None:
        # - Select customer and click List
        self.find(self.CUSTOMERS_NAV_BTN).click()
        self.wait_for(self.CUSTOMERS_DROPDOWN_LIST).click()

    def logout(self) -> None:
        self.wait_for(self.ACCNT_NAME_DROPDOWN).click()
        self.find_all(self.LOGOUT_BTN_DROPDOWN)[-1].click()

    def is_username_shown(self, username: str) -> bool:
        nav_name = self.wait_for(
            self.ACCNT_NAME_DROPDOWN
        ).get_attribute("textContent").strip()
        
        return nav_name.lower() == username.lower()