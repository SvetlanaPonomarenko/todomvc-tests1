from selene.support.conditions import have
from selene.support.shared import browser

scroll = browser.all('#todo-list>li')


def visit():
    browser.open('http://todomvc4tasj.herokuapp.com/')
    browser.should(have.js_returned(True, 'return Object.keys(require.s.contexts._.defined).length === 39;'))


def enter(*tasks):
    for text in tasks:
        browser.element('#new-todo').type(text).press_enter()


def check(*todos):
    todos = ['a', 'b', 'c']
    scroll.should(have.exact_texts(*todos))


def edit_b(value: str):
    scroll.element_by(have.exact_text('b')).double_click()
    scroll.element_by(have.css_class('editing')).element('.edit').type(value).press_enter()


def complete_b_clear():
    scroll.element_by(have.exact_text('b edited')).element('.toggle').click()
    browser.element('#clear-completed').click()


def cancel_edit_c(value):
    scroll.element_by(have.exact_text('c')).double_click()
    scroll.element_by(have.css_class('editing')).element('.edit').type(value).press_escape()


def delete_c():
    scroll.element_by(have.exact_text('c')).hover().element('.destroy').click()
