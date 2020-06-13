from zunzun.commands import RunServerCommand
from unittest.mock import MagicMock


def test_ok():
    http_kernel = MagicMock()
    command = RunServerCommand(http_kernel)
    command.handle()
    assert http_kernel.run.call_count == 1
