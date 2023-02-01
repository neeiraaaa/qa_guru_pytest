from selene.support.shared import browser
import pytest


@pytest.fixture
def browser_desktop():
    browser.config.window_height = 1200
    browser.config.window_width = 1900
    yield
    browser.quit()


@pytest.fixture
def browser_mobile():
    browser.config.window_width = 900
    browser.config.window_height = 920
    yield
    browser.quit()


@pytest.fixture(params=['Desktop', 'Mobile'])
def window_setup(request):
    if request.param == 'Desktop':
        browser.config.window_height = 1200
        browser.config.window_width = 1900
    elif request.param == 'Mobile':
        browser.config.window_width = 900
        browser.config.window_height = 920
    yield browser
    browser.quit()