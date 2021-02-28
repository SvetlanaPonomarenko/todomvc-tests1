from todomvc_tests.model import todomvc


def test_common_todos():
    todomvc.visit()

    todomvc.add('a', 'b', 'c')
    todomvc.should_have('a', 'b', 'c')

    todomvc.edit('b', 'b edited')

    todomvc.toggle('b edited')
    todomvc.clear_completed()
    todomvc.should_have('a', 'c')

    todomvc.cancel_editing('c', ' to be canceled')

    todomvc.delete('c')
    todomvc.should_have('a')
