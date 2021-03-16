from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get('https://www.techlistic.com/p/selenium-tutorials.html')
    yield driver
    

def test_selenium_tutorials(driver):
    driver.find_element_by_name('q').send_keys('api' + Keys.ENTER)
    assert 'rest api' in driver.find_element_by_css_selector('h3').text
    assert 'rest api' in driver.title
