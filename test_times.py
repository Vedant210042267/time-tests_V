from times import time_range, compute_overlap_time
import pytest

@pytest.mark.parametrize("time_range_1,time_range_2,expected", [
    # Given input test with overlapping intervals and gaps
    (
        ("2010-01-12 10:00:00", "2010-01-12 12:00:00", 1, 0),
        ("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60),
        [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    ),
    # No overlap case - completely separate ranges
    (
        ("2021-01-01 12:00:00", "2021-01-01 13:00:00", 1, 0),
        ("2021-01-01 14:00:00", "2021-01-01 15:00:00", 1, 0),
        []
    ),
    # No overlap ranges - separated in time
    (
        ("2010-01-12 09:00:00", "2010-01-12 10:00:00", 1, 0),
        ("2010-01-12 10:30:00", "2010-01-12 11:00:00", 1, 0),
        []
    ),
    # Multiple intervals that perfectly overlap
    (
        ("2010-01-12 10:00:00", "2010-01-12 10:20:00", 2, 0),
        ("2010-01-12 10:00:00", "2010-01-12 10:20:00", 2, 0),
        [
            ('2010-01-12 10:00:00', '2010-01-12 10:10:00'),
            ('2010-01-12 10:10:00', '2010-01-12 10:20:00'),
        ]
    ),
    # Touching endpoints - ranges that meet at exact boundary
    (
        ("2010-01-12 10:00:00", "2010-01-12 10:30:00", 1, 0),
        ("2010-01-12 10:30:00", "2010-01-12 11:00:00", 1, 0),
        []
    ),
    # Edge case - ranges end/start at same time
    (
        ("2023-03-10 08:00:00", "2023-03-10 09:00:00", 1, 0),
        ("2023-03-10 09:00:00", "2023-03-10 10:00:00", 1, 0),
        []
    ),
])
def test_compute_overlap(time_range_1, time_range_2, expected):
    r1 = time_range(*time_range_1)
    r2 = time_range(*time_range_2)
    result = compute_overlap_time(r1, r2)
    assert result == expected

def test_invalid_time_range():
    with pytest.raises(ValueError):
        time_range("2022-01-01 12:00:00", "2022-01-01 10:00:00")