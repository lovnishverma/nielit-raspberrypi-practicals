import os
from nielit_rpi.config import load_env

def test_load_env():
    # create a mock .env file
    import tempfile
    fd, path = tempfile.mkstemp()
    with open(path, 'w') as f:
        f.write("TEST_VAR=TEST_VAL\n")
    
    try:
        load_env(path)
        assert os.environ.get("TEST_VAR") == "TEST_VAL"
    finally:
        os.close(fd)
        os.unlink(path)
        if "TEST_VAR" in os.environ:
            del os.environ["TEST_VAR"]
