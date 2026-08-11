import sys
import os
from nielit_rpi.cli import main

def test_cli_help(capsys):
    sys.argv = ["nielit-rpi", "--help"]
    try:
        main()
    except SystemExit:
        pass
    captured = capsys.readouterr()
    assert "help" in captured.out.lower() or "usage" in captured.out.lower() or "nielit" in captured.out.lower()

def test_cli_list(capsys):
    sys.argv = ["nielit-rpi", "list"]
    main()
    captured = capsys.readouterr()
    assert "3_1" in captured.out
    assert "3_20" in captured.out

def test_cli_info(capsys):
    sys.argv = ["nielit-rpi", "info", "3_2"]
    main()
    captured = capsys.readouterr()
    assert "GPIO LED Output" in captured.out

def test_cli_export_examples(tmp_path, capsys):
    target = str(tmp_path / "my_examples")
    sys.argv = ["nielit-rpi", "export-examples", "--dest", target]
    main()
    captured = capsys.readouterr()
    assert "Successfully exported" in captured.out
    assert os.path.exists(os.path.join(target, "practical_3_1", "main.py"))
    assert os.path.exists(os.path.join(target, "practical_3_20", "main.py"))
