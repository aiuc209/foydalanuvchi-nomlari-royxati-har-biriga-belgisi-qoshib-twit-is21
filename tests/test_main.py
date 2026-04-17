import pytest

def create_username(names):
    return [f"@{name}" for name in names]

@pytest.mark.parametrize("names, expected", [
    (["John", "Alice", "Bob"], ["@John", "@Alice", "@Bob"]),
    (["Mike", "Emma", "David"], ["@Mike", "@Emma", "@David"]),
    ([], []),
])
def test_create_username(names, expected):
    assert create_username(names) == expected
