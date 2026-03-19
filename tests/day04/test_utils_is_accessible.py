import pytest

from day04.utils import is_accessible


@pytest.mark.parametrize(
    "previous, current, next_, col, expected",
    [
        ("...", "...", "...", 1, False),
        ("...", ".@.", "...", 1, True),
        ("...", "@@.", "...", 1, True),
        ("...", "@@@", "...", 1, True),
        (".@.", "@@@", "...", 1, True),
        (".@.", "@@.", ".@.", 1, True),
        (".@.", "@@@", "@@.", 1, False),
        ("@@@", "@@@", "@@@", 1, False),
    ],
)
def test_is_accessible(previous: str, current: str, next_: str, col: int, expected: bool) -> None:
    assert is_accessible(previous, current, next_, col) == expected
