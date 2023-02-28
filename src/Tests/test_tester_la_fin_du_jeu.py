import sys
from pathlib import Path
file = Path(__file__).resolve()
package_root_directory = file.parents[1]
sys.path.append(str(package_root_directory))

from game_background.tester_la_fin_du_jeu import move_possible

def test_move_possible():
    assert move_possible([[2, 1, 2, 1], [1, 6, 6, 12], [0, 6, 0, 1], [1, 6, 12, 24]]) == [True,True,True,True]
    assert move_possible([[2, 2, 6, 12], [12, 6, 2, 2], [2, 2, 6, 12], [12, 6, 2, 2]]) == [False,False,False,False]
