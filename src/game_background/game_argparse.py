"""Run THREES through command line.

This script allows the user to run the game from the terminal!

PYLINT score = 9.17/10
"""
import sys
import argparse
from pathlib import Path

file = Path(__file__). resolve()
package_root_directory = file.parents[1]
sys.path.append(str(package_root_directory))

from GUI.Pygame_with_load import play

# This file creates a CLI so the user is able to executate the file from the terminal especifing the
# configurations or using default configs
parser = argparse.ArgumentParser(
    description='Playing the game THREES!')

args = parser.parse_args()
if __name__ == '__main__':
    play()
    sys.exit(1)
