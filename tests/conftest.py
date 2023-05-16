import pytest
from selene.support.shared import browser

@pytest.fixture(scope='function', autouse=True)
def precondition():
    browser.driver.set_window_size(1920, 1080)
    browser.config.base_url = 'https://demoqa.com'
    yield
    browser.quit()