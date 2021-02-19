from selene.support.shared import browser


def input_(selector, text):
    browser.element(selector).type(text).press_enter()