from todomvc_tests.model import todomvc


def test_add_first_one():
    todomvc.visit()

    # WHEN EMPTY
    todomvc.add()

    todomvc.should_be_empty()

    # WHEN
    todomvc.add('a')

    todomvc.should_have('a')
    todomvc.should_have_items_left(1)


def test_add_many():
    todomvc.visit()

    todomvc.add('a', 'b')

    todomvc.should_have('a', 'b')
    todomvc.should_have_items_left(2)


def test_edit():
    todomvc.visit()
    todomvc.add('a', 'b', 'c')

    todomvc.edit('b', 'b edited')

    todomvc.should_have('a', 'b edited', 'c')
    todomvc.should_have_items_left(3)


def test_edit_by_focus_change():
    todomvc.visit()
    todomvc.add('a', 'b', 'c')

    todomvc.edit_by_focus_change('b', 'b edited')

    todomvc.should_have('a', 'b edited', 'c')
    todomvc.should_have_items_left(3)


def test_cancel_editing():
    todomvc.visit()
    todomvc.add('a', 'b', 'c')

    todomvc.cancel_editing('c', ' to be canceled')

    todomvc.should_have('a', 'b', 'c')
    todomvc.should_have_items_left(3)


def test_complete():
    todomvc.visit()
    todomvc.add('a', 'b', 'c')

    todomvc.toggle('b')

    todomvc.should_have_completed('b')
    todomvc.should_have_active('a', 'c')
    todomvc.should_have_items_left(2)


def test_activate():
    todomvc.visit()
    todomvc.add('a', 'b', 'c')
    todomvc.toggle('b')

    todomvc.toggle('b')

    todomvc.should_have_active('a', 'b', 'c')
    todomvc.should_have_completed()
    todomvc.should_have_items_left(3)


def test_complete_all():
    todomvc.visit()
    todomvc.add('a', 'b', 'c')

    todomvc.toggle_all()

    todomvc.should_have_active()
    todomvc.should_have_completed('a', 'b', 'c')
    todomvc.should_have_items_left(0)


def test_activate_all():
    todomvc.visit()
    todomvc.add('a', 'b', 'c')
    todomvc.toggle_all()

    todomvc.toggle_all()

    todomvc.should_have_completed()
    todomvc.should_have_active('a', 'b', 'c')
    todomvc.should_have_items_left(3)


def test_clear_completed():
    todomvc.visit()
    todomvc.add('a', 'b', 'c')
    todomvc.toggle('a')
    todomvc.toggle('c')

    todomvc.clear_completed()

    todomvc.should_have('b')
    todomvc.should_have_items_left(1)


def test_delete():
    todomvc.visit()
    todomvc.add('a', 'b', 'c')

    todomvc.delete('b')

    todomvc.should_have('a', 'c')
    todomvc.should_have_items_left(2)
