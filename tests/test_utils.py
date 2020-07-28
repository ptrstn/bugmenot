from bugmenot.utils import max_widths, print_as_table


def test_max_widths():
    entries = [{"A": "ABCDE", "B": 13, "C": None}, {"A": "AA", "B": 999, "C": -1}]
    widths = max_widths(entries)

    assert widths["A"] == 5
    assert widths["B"] == 3
    assert widths["C"] == 2


def test_print_as_table():
    entries = [{"A": "ABCDE", "B": 13, "C": None}, {"A": "AA", "B": 999, "C": -1}]
    print_as_table(entries)
