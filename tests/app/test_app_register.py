import pytest
from click.core import Group
from unittest.mock import patch
from zunzun import AppRegister, AppRegisterException
from unittest.mock import MagicMock


def test_there_is_not_app():
    app_register = AppRegister(MagicMock())
    with pytest.raises(AppRegisterException):
        app_register.get("not_app")


def test_get():
    class MyApp:
        def __init__(self, name):
            self.name = name

    app_register = AppRegister(MagicMock())
    app_register.add(MyApp("app_1"))
    app_register.add([MyApp("app_2"), MyApp("app_3")])
    try:
        app_register.get("app_1")
        app_register.get("app_2")
        app_register.get("app_3")
    except AppRegisterException:
        pytest.fail("Unexpected AppRegisterException ..")


def test_commands():
    app_register = AppRegister(MagicMock())
    app_register.add(MagicMock())
    with patch.object(Group, "add_command") as add_command:
        app_register.commands()
    assert add_command.call_count == 1
