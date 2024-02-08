import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from dotenv import load_dotenv
import os
from pathlib import Path


@pytest.fixture(scope="module")
def driver():
    driver_path = '../drivers/chrome/chromedriver.exe'
    service = Service(executable_path=driver_path)
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    return driver


@pytest.fixture(scope="module")
def env_vars():
    load_dotenv()
    ENV_PATH = Path('.')/'.env'
    load_dotenv(dotenv_path=ENV_PATH)
    vars = {}
    vars['PASSWORD'] = os.getenv('PASSWORD')
    vars['USERNAME'] = os.getenv('EMAIL')
    vars['URL'] = os.getenv('DOMAIN')
    return vars
