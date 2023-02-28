import sys
from pathlib import Path
file = Path(__file__).resolve()
package_root_directory = file.parents[1]
sys.path.append(str(package_root_directory))

# contents of app.py, a simple API retrieval example
import pytest
from src.side_functions.read_command import read_player_command
from io import StringIO

# contents of test_app.py, a simple test for our API retrieval
# import requests for the purposes of monkeypatching
import requests


def read_player_command():
    move = str(
        input("What is your movement? (g (gauche), d (droite), h (haut), b (bas)):"))
    while move not in ["g", "d", "h", "b"]:
        print("This is not valid.")
        move = str(
            input("What is your movement? (g (gauche), d (droite), h (haut), b (bas)):"))
    return move


mock_input = StringIO('g\n')


def mock_input_return(monkeypatch):

    monkeypatch.setattr("sys.stdin", mock_input)

    assert read_player_command == "g\n"
    result = read_player_command()
    print(result)
