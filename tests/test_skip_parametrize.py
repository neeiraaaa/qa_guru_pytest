import pytest
from selene.support.shared import browser
from selene import be


@pytest.mark.parametrize("width, height", [pytest.param(1900, 1200), pytest.param(920, 900)])
def test_signin_skip_mobile(width, height):
    if width == 920:
        pytest.skip(reason='Пропустить мобильную версию')
    browser.config.window_width = width
    browser.config.window_height = height
    browser.open('https://github.com/')
    browser.element('[href="/login"]').click()
    assert browser.element('#login').should(be.visible)


@pytest.mark.parametrize("width, height", [pytest.param(1900, 1200), pytest.param(920, 900)])
def test_signin_skip_desktop(width, height):
    if width == 1900:
        pytest.skip(reason='Пропустить десктопную версию')
    browser.config.window_width = width
    browser.config.window_height = height
    browser.open('https://github.com/')
    browser.element('.Button-label').click()
    browser.element('[href="/login"]').click()
    assert browser.element('#login').should(be.visible)