from zunzun import CommandRegister, Command
from unittest.mock import MagicMock


def test_add_commands():
    class MyCommand(Command):
        pass

    class ModuleMock:
        no_command = ""
        command = MyCommand

    injector = MagicMock()
    injector.get = MagicMock(return_value="object_from_injector")
    command_register = CommandRegister(injector)
    group = MagicMock()
    command_register.add_commands(group, ModuleMock)
    assert injector.get.call_count == 1
    group.add_command.assert_called_once_with("object_from_injector")
