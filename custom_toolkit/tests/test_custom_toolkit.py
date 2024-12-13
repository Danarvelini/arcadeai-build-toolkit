import pytest
from arcade.sdk.errors import ToolExecutionError
from arcade_custom_toolkit.tools.hello import hello

def test_hello():
    assert hello("developer") == "Hello, developer!"

def test_hello_raises_error():
    with pytest.raises(ToolExecutionError):
        hello(1)