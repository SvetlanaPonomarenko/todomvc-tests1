from selene.support.conditions import be
from selene.support.shared import browser


def should_be_empty(selector):
    browser.all(selector).filter_by(be.visible).should(be.empty)
