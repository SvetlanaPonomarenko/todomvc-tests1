from selene.support.shared import browser
from todomvc_tests.model.pages import todomvc_old


def test_common_todos():
    browser.config.set_value_by_js = True

    todomvc_old.visit()

    todomvc_old.add('a', 'b', 'c')
    todomvc_old.should_have('a', 'b', 'c')

    todomvc_old.edit('b', 'b edited')

    todomvc_old.toggle('b edited')
    todomvc_old.clear_completed()
    todomvc_old.should_have('a', 'c')

    todomvc_old.cancel_editing('c', ' to be canceled')

    todomvc_old.delete('c')
    todomvc_old.should_have('a')
