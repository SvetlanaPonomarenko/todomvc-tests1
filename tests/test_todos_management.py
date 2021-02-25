from selene.support.shared import browser
from todomvc_tests.model.todomvc_page import TodoMvcPage


def test_common_todos():
    browser.config.set_value_by_js = True

    TodoMvcPage().visit()

    TodoMvcPage().add('a', 'b', 'c')
    TodoMvcPage().should_have('a', 'b', 'c')

    TodoMvcPage().edit('b', 'b edited')

    TodoMvcPage().toggle('b edited')
    TodoMvcPage().clear_completed()
    TodoMvcPage().should_have('a', 'c')

    TodoMvcPage().cancel_editing('c', ' to be canceled')

    TodoMvcPage().delete('c')
    TodoMvcPage().should_have('a')
