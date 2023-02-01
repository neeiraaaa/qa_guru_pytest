from selene import be
from selene.support.shared import browser


def test_login_desktop(browser_desktop):
    browser.open('https://github.com/')
    browser.element('[href="/login"]').click()
    assert browser.element('#login').should(be.visible)


def test_login_mobile(browser_mobile):
    browser.open('https://github.com/')
    browser.element('.Button-label').click()
    browser.element('[href="/login"]').click()
    assert browser.element('#login').should(be.visible)