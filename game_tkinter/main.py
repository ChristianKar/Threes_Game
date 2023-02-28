import sys
from pathlib import Path
file = Path(__file__).resolve()
package_root_directory = file.parents[1]
sys.path.append(str(package_root_directory))

import argparse
from src.GUI.Final_Game_Tkinter import play


# This file creates a CLI so the user is able to executate the file from the terminal especifing the
# configurations or using default config

parser = argparse.ArgumentParser(
    description='Playing the game Threes!')
args = parser.parse_args()

play()