import pytest


def test_variable():
    variable = 10
    assert 10 == variable

    variable = "Hello"
    assert "Hello" == variable


def test_operators():

    a = 10
    b = 20

    assert a != b


def words_count(input_str: str):
    input_str = input_str.strip(' ')
    result = input_str.count(' ')
    if result == 0:
        if len(input_str) == 0:
            pass
        else:
            result = 1
    else:
        result = result + 1
    return result

@pytest.mark.parametrize(
    'data, expected', [
        ('Privet', 1),
        ('', 0),
        ('Hello, world!', 2),
        ( 'Hello, world! ', 2)
    ]
)
def test_words_count(data, expected):
    # A-A-A
    assert expected == words_count(data)
