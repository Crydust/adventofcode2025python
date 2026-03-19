import pytest

from day04.utils import sliding_windows


@pytest.mark.parametrize(
    "rows, expected",
    [
        ([], []),
        (["A"], [("", "A", "")]),
        (["A", "B"], [("", "A", "B"), ("A", "B", "")]),
        (
            ["A", "B", "C"],
            [("", "A", "B"), ("A", "B", "C"), ("B", "C", "")],
        ),
    ],
)
def test_sliding_windows_expected_output(rows: list[str], expected: list[tuple[str, str, str]]) -> None:
    assert list(sliding_windows(rows)) == expected


def test_sliding_windows_preserves_order_for_longer_input() -> None:
    rows = ["r0", "r1", "r2", "r3"]

    windows = list(sliding_windows(rows))

    assert windows == [
        ("", "r0", "r1"),
        ("r0", "r1", "r2"),
        ("r1", "r2", "r3"),
        ("r2", "r3", ""),
    ]

