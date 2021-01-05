from selene.support.conditions import have
from selene.support.shared import browser


def test_common_tasks_management():
    browser.open('http://todomvc4tasj.herokuapp.com/')
    browser.should(have.js_returned(True, 'return Object.keys(require.s.contexts._.defined).length === 39;'))

    # Add
    browser.element('#new-todo').type('a').press_enter()
    browser.element('#new-todo').type('b').press_enter()
    browser.element('#new-todo').type('c').press_enter()
    browser.all('#todo-list>li').should(have.exact_texts('a', 'b', 'c'))

    # Edit
    browser.all('#todo-list>li').element_by(have.exact_text('b')).double_click()
    browser.all('#todo-list>li').element_by(have.css_class('editing')).element('.edit').\
        type(' edited').press_enter()

    # Complete&Clear
    browser.all('#todo-list>li').element_by(have.exact_text('b edited')).element('.toggle').click()
    browser.element('#clear-completed').click()
    browser.all('#todo-list>li').should(have.exact_texts('a', 'c'))

    # Cancel edit
    browser.all('#todo-list>li').element_by(have.exact_text('c')).double_click()
    browser.all('#todo-list>li').element_by(have.css_class('editing')).element('.edit').\
        type(' to be canceled').press_escape()

    # Delete
    browser.all('#todo-list>li').element_by(have.exact_text('c')).hover().element('.destroy').click()
    browser.all('#todo-list>li').should(have.exact_texts('a'))
