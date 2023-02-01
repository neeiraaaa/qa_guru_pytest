import pytest
from selene import be
from selene.support.shared import browser

desktop = pytest.mark.parametrize("window_setup", ["Desktop"], indirect=True)
mobile = pytest.mark.parametrize("window_setup", ["Mobile"], indirect=True)


@desktop
def test_login_desktop_indirect(window_setup):
    browser.open('https://github.com/')
    browser.element('[href="/login"]').click()
    assert browser.element('#login').should(be.visible)


@mobile
def test_login_mobile_indirect(window_setup):
    browser.open('https://github.com/')
    browser.element('.Button-label').click()
    browser.element('[href="/login"]').click()
    assert browser.element('#login').should(be.visible)