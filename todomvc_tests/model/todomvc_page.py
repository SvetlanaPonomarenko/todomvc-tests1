from selene import be, have
from selene.support.shared import browser

be_completed = have.css_class('completed')


class TodoMvcPage:
    def __init__(self, ):
        self.browser = browser
        self.list_ = browser.all('#todo-list>li')

    def visit(self):
        self.browser.open('http://todomvc4tasj.herokuapp.com/#/')
        self.browser.should(have.js_returned(
            True,
            'return Object.keys(require.s.contexts._.defined).length === 39;'))
        return self

    def add(self, *todos: str):
        for text in todos:
            browser.element('#new-todo').set_value(text).press_enter()
        return self

    def should_have(self, *todos):
        self.list_.should(have.exact_texts(*todos))
        return self

    def should_have_items_left(self, amount: int):
        browser.element('#todo-count>strong').should(have.exact_text(str(amount)))
        return self

    def start_editing(self, todo: str, new_text: str):
        self.list_.element_by(have.exact_text(todo)).double_click()
        return self.list_.element_by(have.css_class('editing')). \
            element('.edit').with_(set_value_by_js=True).set_value(new_text)

    def edit(self, todo: str, new_text):
        self.start_editing(todo, new_text).press_enter()
        return self

    def edit_by_focus_change(self, todo: str, new_text):
        self.start_editing(todo, new_text).press_tab()
        return self

    def cancel_editing(self, todo: str, new_text):
        self.start_editing(todo, new_text).press_escape()
        return self

    def toggle(self, todo: str):
        self.list_.element_by(have.exact_text(todo)). \
            element('.toggle').click()
        return self

    def toggle_all(self):
        self.browser.element('#toggle-all').click()
        return self

    def should_be_empty(self):
        self.list_.filter_by(be.visible).should(be.empty)
        return self

    def should_have_completed(self, *todos: str):
        self.list_.filtered_by(be_completed).should(have.exact_texts(*todos))
        return self

    def should_have_active(self, *todos: str):
        self.list_.filtered_by(be_completed.not_).should(have.exact_texts(*todos))
        return self

    def clear_completed(self):
        self.browser.element('#clear-completed').click()
        return self

    def delete(self, todo: str):
        self.list_.element_by(have.exact_text(todo)).hover(). \
            element('.destroy').click()
        return self
