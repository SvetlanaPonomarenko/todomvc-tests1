from selene import command, have
from selene.support.shared import browser
from todomvc_tests.model.controls import field, all_list

todo_list = browser.all('#todo-list>li')


class TodoMvcPage:
    def __init__(self, browser=browser,
                 todo_list=browser.all('#todo-list>li'),
                 all_list=all_list,
                 field=field):
        self.browser = browser
        self.todo_list = todo_list
        self.all_list = all_list
        self.field = field

    def visit_at_all(self):
        self.browser.open('http://todomvc4tasj.herokuapp.com/#/')
        self.browser.should(have.js_returned(
            True,
            'return Object.keys(require.s.contexts._.defined).length === 39;'))
        return self

    def add(self, *todos: str):
        for text in todos:
            field.input_('#new-todo', text)
        return self

    def should_have(self, *todos):
        self.todo_list.should(have.exact_texts(*todos))
        return self

    def start_editing(self, todo: str, new_text):
        self.todo_list.element_by(have.exact_text(todo)).double_click()
        return todo_list.element_by(have.css_class('editing')). \
            element('.edit').perform(command.js.set_value(new_text))

    def edit(self, todo: str, new_text):
        self.start_editing(todo, new_text).press_enter()
        return self

    def toggle(self, todo: str):
        self.todo_list.element_by(have.exact_text(todo)).\
             element('.toggle').click()
        return self

    def should_be_empty(self):
        self.all_list.should_be_empty('#todo-list>li')
        return self

    def clear_completed(self):
        self.browser.element('#clear-completed').click()
        return self

    def cancel_editing(self, todo: str, new_text):
        self.start_editing(todo, new_text).press_escape()
        return self

    def delete(self, todo: str):
        self.todo_list.element_by(have.exact_text(todo)).hover().\
             element('.destroy').click()
        return self
