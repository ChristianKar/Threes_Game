import sys  
from pathlib import Path 
file = Path(__file__). resolve()  
package_root_directory = file.parents [1]  
sys.path.append(str(package_root_directory))

import pytest
from game_background.mettre_en_orchestre_le_jeu import *
from io import StringIO


def test_is_int():
    assert is_int(4) == True
    assert is_int(4.5) == True
    assert is_int(6) == True


def test_get_score():
    assert get_score([[0, 1, 6, 2], [0, 0, 0, 0], [0, 384, 24, 48], [1536, 6144, 384, 0]]) == 201315
    assert get_score([[12, 1, 6, 2], [2, 1, 2, 96], [1, 384, 24, 48], [1536, 6144, 384, 2]]) == 201567
    assert get_score([[2, 1, 2, 1], [1, 6, 6, 12], [0, 6, 0, 1], [1, 6, 12, 6144]]) == 177177


def test_is_record():
    record, score, pos = is_record([[0, 1, 6, 2], [0, 0, 0, 0], [0, 384, 24, 48], [1536, 6144, 384, 0]])
    if record:
        save_record("Isa", score, pos)
    d = shelve.open(record_path)
    list_name = d['name']
    assert list_name[0]=="Isa"
    
    record, score, pos = is_record([[12, 1, 6, 2], [2, 1, 2, 96], [1, 384, 24, 48], [1536, 6144, 384, 2]])
    if record:
        save_record("Victor", score, pos)
    d = shelve.open(record_path)
    list_name = d['name']
    assert list_name[0]=="Victor"
       
    record, score, pos = is_record([[2, 1, 2, 1], [1, 6, 6, 12], [0, 6, 0, 1], [1, 6, 12, 2144]])
    if record:
        save_record("Ana", score, pos)
    d = shelve.open(record_path)
    list_name = d['name']
    print(list_name)
    assert list_name[2]=="Ana"
    
    record, score, pos = is_record([[2, 1, 2, 1], [1, 2, 3, 6], [0, 2, 0, 1], [1, 2, 4, 4]])
    if record:
        save_record("Chris", score, pos)
    d = shelve.open(record_path)
    list_name = d['name']
    assert "Chris" not in list_name
    d.clear()
test_is_record()
