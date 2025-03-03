import pytest
from app.commands.basic import AddCommand, SubtractCommand

def test_add():
    add = AddCommand()
    assert add.execute(4, 5) == 9
    assert add.execute(10, -2) == 8

def test_subtract():
    subtract = SubtractCommand()
    assert subtract.execute(10, 5) == 5
    assert subtract.execute(20, 4) == 16
