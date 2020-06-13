from zunzun import App
from unittest.mock import MagicMock
from unittest.mock import patch
from zunzun.app.app import Path, importlib


def test_register_listeners():
    class MyApp(App):
        listeners_config = [("a", "b")]

    listener_connector = MagicMock()
    MyApp(MagicMock(), listener_connector)
    listener_connector.connect.assert_called_once_with("a", "b")


def test_path():
    class MyApp(App):
        __module__ = "module_name.class_name"

    app = MyApp(MagicMock(), MagicMock())
    assert app.path == "module_name"


def test_get_module_by_name():
    class MyApp(App):
        pass

    app = MyApp(MagicMock(), MagicMock())
    with patch.object(Path, "mkdir") as mkdir, patch.object(
        Path, "touch"
    ) as touch, patch.object(importlib, "import_module") as import_module:
        app.get_or_create_module("module_name")
    assert mkdir.call_count == 1
    assert touch.call_count == 1
    assert import_module.call_count == 1
