from times import time_range, compute_overlap_time
import pytest

def test_given_input():
    
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    print(compute_overlap_time(large, short))

    result = compute_overlap_time(large,short)

    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]

    assert result == expected
# no overlap case
def test_no_overlap():
    range1 = time_range("2021-01-01 12:00:00", "2021-01-01 13:00:00")
    range2 = time_range("2021-01-01 14:00:00", "2021-01-01 15:00:00")

    result = compute_overlap_time(range1, range2)

    expected = []

    assert result == expected

# multiple intervals in both ranges
def test_multiple_intervals():
    range1 = time_range("2022-05-01 09:00:00", "2022-05-01 11:00:00", 3, 30)
    range2 = time_range("2022-05-01 10:15:00", "2022-05-01 12:15:00", 4, 15)


def test_no_overlap_ranges():
    r1 = time_range("2010-01-12 09:00:00", "2010-01-12 10:00:00")
    r2 = time_range("2010-01-12 10:30:00", "2010-01-12 11:00:00")
    result = compute_overlap_time(r1, r2)
    assert result == []

def test_multiple_intervals_each():
    r1 = time_range("2010-01-12 10:00:00", "2010-01-12 10:20:00", 2, 0)
    r2 = time_range("2010-01-12 10:00:00", "2010-01-12 10:20:00", 2, 0)
    # r1: [10:00–10:10], [10:10–10:20]
    # r2: [10:00–10:10], [10:10–10:20]
    result = compute_overlap_time(r1, r2)
    expected = [
        ('2010-01-12 10:00:00', '2010-01-12 10:10:00'),
        ('2010-01-12 10:10:00', '2010-01-12 10:20:00'),
    ]
    assert result == expected


def test_touching_endpoints():
    r1 = time_range("2010-01-12 10:00:00", "2010-01-12 10:30:00")
    r2 = time_range("2010-01-12 10:30:00", "2010-01-12 11:00:00")
    result = compute_overlap_time(r1, r2)
    assert result == []

# two time ranges that end exactly at the same time when the other starts
def test_edge_case_no_overlap():
    range1 = time_range("2023-03-10 08:00:00", "2023-03-10 09:00:00")
    range2 = time_range("2023-03-10 09:00:00", "2023-03-10 10:00:00")

def test_invalid_time_range():
    with pytest.raises(ValueError):
        time_range("2022-01-01 12:00:00", "2022-01-01 10:00:00")