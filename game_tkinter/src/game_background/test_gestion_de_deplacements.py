from gestion_des_deplacements import move_row_left, move_row_right, move_grid
  
def test_move_row_left():

    assert move_row_left([0, 0, 0, 1]) == [0, 0, 1, 0]
    assert move_row_left([0, 1, 0, 2]) == [1, 0, 2, 0]
    assert move_row_left([1, 2, 0, 2]) == [3, 0, 2, 0]
    assert move_row_left([3, 2, 1, 0]) == [3, 3, 0, 0]
    assert move_row_left([2, 2, 0, 1]) == [2, 2, 1, 0]
    assert move_row_left([2, 0, 0, 1]) == [2, 0, 1, 0]
    assert move_row_left([2, 6, 1, 2]) == [2, 6, 3, 0]
    assert move_row_left([2, 3, 3, 0]) == [2, 6, 0, 0]
    assert move_row_left([6, 12, 24, 48]) == [6, 12, 24, 48]

def test_move_row_right():

    assert move_row_right([0, 0, 0, 1]) == [0, 0, 0, 1]
    assert move_row_right([0, 1, 0, 2]) == [0, 0, 1, 2]
    assert move_row_right([0, 1, 2, 2]) == [0, 0, 3, 2]
    assert move_row_right([2, 1, 2, 1]) == [0, 2, 1, 3]
    assert move_row_right([2, 2, 0, 1]) == [0, 2, 2, 1]
    assert move_row_right([2, 0, 0, 1]) == [0, 2, 0, 1]
    assert move_row_right([2, 6, 1, 2]) == [0, 2, 6, 3]
    assert move_row_right([2, 3, 3, 0]) == [0, 2, 3, 3]
    assert move_row_right([6, 12, 24, 48]) == [6, 12, 24, 48]

def test_move_grid():
    assert move_grid([[1,0,0,2], [6, 6, 0, 0], [6, 0, 6, 0], [0, 2, 1, 0]],"left") == [[1,0,2,0], [12, 0, 0, 0], [6, 6, 0, 0], [2, 1, 0, 0]]
    assert move_grid([[1,0,0,2], [6, 6, 0, 0], [6, 0, 6, 0], [0, 2, 1, 0]],"right") == [[0,1,0,2], [0, 6, 6, 0], [0, 6, 0, 6], [0, 0, 2, 1]]
    assert move_grid([[1,0,0,2], [6, 6, 0, 0], [6, 0, 6, 0], [0, 2, 1, 0]],"up") == [[1,6,0,2], [12, 0, 6, 0], [0, 2, 1, 0], [0, 0, 0, 0]]
    assert move_grid([[1,0,0,2], [6, 6, 0, 0], [6, 0, 6, 0], [0, 2, 1, 0]],"down") == [[0, 0, 0, 0], [1, 0, 0, 2],[6,6,6,0],[6, 2, 1, 0]]
