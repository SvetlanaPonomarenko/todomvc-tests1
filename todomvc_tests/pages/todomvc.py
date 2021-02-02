from selene import command, have
from selene.support.shared import browser

todo_list = browser.all('#todo-list>li')


def visit():
    browser.open('http://todomvc4tasj.herokuapp.com/')
    browser.should(have.js_returned(
        True,
        'return Object.keys(require.s.contexts._.defined).length === 39;'))


def add(*todos: str):
    for text in todos:
        browser.element('#new-todo').type(text).press_enter()


def should_have(*todos):
    todo_list.should(have.exact_texts(*todos))


def start_editing(todo: str, new_text):
    todo_list.element_by(have.exact_text(todo)).double_click()
    return todo_list.element_by(have.css_class('editing')). \
        element('.edit').perform(command.js.set_value(new_text))


def edit(todo: str, new_text):
    start_editing(todo, new_text).press_enter()


def toggle(todo: str):
    todo_list.element_by(have.exact_text(todo)).element('.toggle').click()


def clear_completed():
    browser.element('#clear-completed').click()


def cancel_editing(todo: str, new_text):
    start_editing(todo, new_text).press_escape()


def delete(todo: str):
    todo_list.element_by(have.exact_text(todo)).hover().element('.destroy').click()
