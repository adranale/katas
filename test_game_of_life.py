import pytest

from game_of_life import *


@pytest.fixture
def mock_count_neighbors(mocker):
    yield mocker.patch("game_of_life.count_neighbors")


def test_get_next_generation_of_cell_is_live_for_3_neighbors(mock_count_neighbors):
    # given
    grid = ["........", "....*...", "...**...", "........"]
    mock_count_neighbors.return_value = 3

    # when
    next_cell = get_next_generation_of_cell(grid, 0, 0)

    # then
    assert '*' == next_cell


def test_get_next_generation_of_cell_is_same_for_2_neighbors(mock_count_neighbors):
    # given
    grid = ["........", "....*...", "...**...", "........"]
    mock_count_neighbors.return_value = 2

    # when
    next_cell = get_next_generation_of_cell(grid, 1, 4)

    # then
    assert grid[1][4] == next_cell


def test_get_next_generation_of_cell_is_dead_for_1_neighbors(mock_count_neighbors):
    # given
    grid = ["........", "....*...", "...**...", "........"]
    mock_count_neighbors.return_value = 1

    # when
    next_cell = get_next_generation_of_cell(grid, 0, 0)

    # then
    assert '.' == next_cell


def test_get_next_generation_of_cell_is_dead_for_0_neighbors(mock_count_neighbors):
    # given
    grid = ["........", "....*...", "...**...", "........"]
    mock_count_neighbors.return_value = 0

    # when
    next_cell = get_next_generation_of_cell(grid, 0, 0)

    # then
    assert '.' == next_cell


def test_get_next_generation_of_cell_is_dead_for_4_neighbors(mock_count_neighbors):
    # given
    grid = ["........", "....*...", "...**...", "........"]
    mock_count_neighbors.return_value = 4

    # when
    next_cell = get_next_generation_of_cell(grid, 0, 0)

    # then
    assert '.' == next_cell


def test_count_neighbors():
    grid = ["........", "....*...", "...**...", "........"]
    assert 0 == count_neighbors(grid, 0, 0)
    assert 1 == count_neighbors(grid, 0, 3)
    assert 1 == count_neighbors(grid, 0, 4)
    assert 0 == count_neighbors(grid, 0, 6)
    assert 0 == count_neighbors(grid, 0, 7)

    assert 0 == count_neighbors(grid, 1, 0)
    assert 1 == count_neighbors(grid, 1, 2)
    assert 3 == count_neighbors(grid, 1, 3)
    assert 2 == count_neighbors(grid, 1, 4)
    assert 2 == count_neighbors(grid, 1, 5)


def test_next_generation():
    input_grid = """4 8
........
....*...
...**...
........"""
    output_grid = get_next_generation(input_grid)
    assert output_grid == """4 8
........
...**...
...**...
........"""

