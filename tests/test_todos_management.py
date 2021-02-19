from selene.support.shared import browser

from todomvc_tests.model import app
browser.config.set_value_by_js = True


def test_add():
    app.TodoMvc.visit_at_all().add('a', 'b').should_have('a', 'b')


def test_edit():
    app.TodoMvc.visit_at_all().add('b').\
        edit('b', 'b edited').should_have('b edited')


def test_complete_clear():
    app.TodoMvc.visit_at_all().add('b').toggle('b').\
        clear_completed().should_be_empty()


def test_cancel_edit():
    app.TodoMvc.visit_at_all().add('c').\
        cancel_editing('c', ' to be canceled').should_have('c')


def test_delete():
    app.TodoMvc.visit_at_all().add('a').delete('a').should_be_empty()
