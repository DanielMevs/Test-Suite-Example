from .conftest import env_vars, driver
from pytest import fixture
from .pages.helpers.file_reader import read_file
from .pages.home import Home
from .pages.new_customer import NewCustomer
from .pages.form_authentication import FormAuthentication
from .pages.nav_bar import NavBar
from .pages.home_validator import HomeValidator


def test_login(env_vars: fixture, driver: fixture) -> None:
    """
    Testing logging in
    """
    home_page = Home(driver)
    url = env_vars["URL"]
    username = env_vars["USERNAME"]
    password = env_vars["PASSWORD"]
    form_auth = home_page.go_to_login(url)
    form_auth.login(username, password)


def test_add_customer(driver: fixture) -> None:
    """
    Testing adding a new customer
    """
    nav_bar = NavBar(driver)
    nav_bar.go_to_list()
    customer = NewCustomer(driver)
    customer.add_customer()
    nav_bar.logout()


def test_new_user_login(driver: fixture, env_vars: fixture) -> None:
    """
    Testing logging out and making sure that new
    users can log in with their new credentials
    """
    url = env_vars["URL"]
    home_page = Home(driver)
    home_validator = HomeValidator(driver)
    auth_form = home_page.go_to_login(url)
    user_name, pass_word = read_file()
    auth_form.login(user_name, pass_word)
    assert home_validator.is_home(user_name)
