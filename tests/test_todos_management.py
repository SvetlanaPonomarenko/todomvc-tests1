from selene.support.conditions import have
from todomvc_tests.pages import todomvc
from todomvc_tests.pages.todomvc import scroll


def test_common_todos():
    todomvc.visit()

    todomvc.enter('a', 'b', 'c')
    todomvc.check()

    todomvc.edit_b(' edited')

    todomvc.complete_b_clear()
    scroll.should(have.exact_texts('a', 'c'))

    todomvc.cancel_edit_c(' to be canceled')

    todomvc.delete_c()
    scroll.should(have.exact_texts('a'))
