import pytest
from src.board import Board

def test_initial_board():
    board = Board()
    assert all(cell is None for cell in board.cells)
    assert len(board.get_empty_cells()) == 9

def test_place_mark_valid():
    board = Board()
    assert board.place_mark(1, 'O') is True
    assert board.cells[0] == 'O'
    assert len(board.get_empty_cells()) == 8

def test_place_mark_invalid_occupied():
    board = Board()
    board.place_mark(5, 'O')
    assert board.place_mark(5, 'X') is False
    assert board.cells[4] == 'O'

def test_place_mark_out_of_range():
    board = Board()
    assert board.place_mark(0, 'O') is False
    assert board.place_mark(10, 'O') is False

def test_is_full():
    board = Board()
    for i in range(1, 10):
        assert board.is_full() is False
        board.place_mark(i, 'X')
    assert board.is_full() is True

def test_get_empty_cells():
    board = Board()
    board.place_mark(1, 'X')
    board.place_mark(9, 'O')
    empty = board.get_empty_cells()
    assert empty == [2, 3, 4, 5, 6, 7, 8]
