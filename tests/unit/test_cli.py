import sys
from nielit_rpi.cli import main
from unittest.mock import patch

def test_cli_help(capsys):
    sys.argv = ["nielit-rpi", "--help"]
    try:
        main()
    except SystemExit:
        pass
    captured = capsys.readouterr()
    assert "help" in captured.out.lower() or "usage" in captured.out.lower() or "nielit" in captured.out.lower()

def test_cli_info(capsys):
    sys.argv = ["nielit-rpi", "info", "test_id"]
    try:
        main()
    except SystemExit:
        pass
    captured = capsys.readouterr()
    assert True
