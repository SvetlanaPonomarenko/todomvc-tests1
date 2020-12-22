import time
from selene.support.conditions import have
from selene.support.shared import browser


def test_todos():
    browser.open('http://todomvc4tasj.herokuapp.com/')
    time.sleep(2)

    browser.element('#new-todo').type('a').press_enter()
    browser.element('#new-todo').type('b').press_enter()
    browser.element('#new-todo').type('c').press_enter()

    browser.all('#todo-list>li').should(have.exact_texts('a', 'b', 'c'))

    browser.element('#todo-list>li:nth-of-type(2) .view').double_click()
    browser.element('#todo-list>li:nth-of-type(2) .edit').double_click().type('b new').press_enter()

    browser.all('#todo-list>li').should(have.exact_texts('a', 'b new', 'c'))

    browser.element('#todo-list>li:nth-of-type(2) .toggle').click()
    browser.all('#todo-list>li.completed').should(have.exact_texts('b new'))
    browser.all('#todo-list>li:not(.completed)').should(have.exact_texts('a', 'c'))

    browser.element('#clear-completed').click()
    browser.all('#todo-list>li').should(have.exact_texts('a', 'c'))

    browser.element('#todo-list>li:nth-of-type(2) .view').double_click()
    browser.element('#todo-list>li:nth-of-type(2) .edit').double_click().type('c new').press_escape()
    browser.element('#todo-list>li:nth-of-type(2) .destroy').click()

    browser.all('#todo-list>li').should(have.exact_texts('a'))
