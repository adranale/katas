import pytest as pytest

import bowling


@pytest.fixture
def mock_throw_first(mocker):
    yield mocker.patch("bowling.throw_first")


@pytest.fixture
def mock_throw_second(mocker):
    yield mocker.patch("bowling.throw_second")


def test_all_strikes(mock_throw_first):
    # given
    mock_throw_first.return_value = 10

    # when
    lines = bowling.main()

    # then
    assert len(lines) == 3
    for line in lines:
        assert bowling.total(line) == 300


def test_9s_and_misses(mock_throw_first, mock_throw_second):
    # given
    mock_throw_first.return_value = 9
    mock_throw_second.return_value = 0

    # when
    lines = bowling.main()

    # then
    assert len(lines) == 3
    for line in lines:
        assert bowling.total(line) == 90


def test_5s(mock_throw_first, mock_throw_second):
    # given
    mock_throw_first.return_value = 5
    mock_throw_second.return_value = 5

    # when
    lines = bowling.main()

    # then
    assert len(lines) == 3
    for line in lines:
        assert bowling.total(line) == 150
