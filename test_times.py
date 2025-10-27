from times import time_range, compute_overlap_time

def test_given_input():
    
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    print(compute_overlap_time(large, short))

    result = compute_overlap_time(large,short)

    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]

    assert result == expected

# multiple intervals in both ranges
def multiple_intervals():
    range1 = time_range("2022-05-01 09:00:00", "2022-05-01 11:00:00", 3, 30)
    range2 = time_range("2022-05-01 10:15:00", "2022-05-01 12:15:00", 4, 15)

    result = compute_overlap_time(range1, range2)

    expected = [('2022-05-01 10:15:00', '2022-05-01 10:30:00'), ('2022-05-01 10:30:00', '2022-05-01 10:45:00'), ('2022-05-01 10:45:00', '2022-05-01 11:00:00')]

    assert result == expected

# two time ranges that end exactly at the same time when the other starts
def edge_case_no_overlap():
    range1 = time_range("2023-03-10 08:00:00", "2023-03-10 09:00:00")
    range2 = time_range("2023-03-10 09:00:00", "2023-03-10 10:00:00")

    result = compute_overlap_time(range1, range2)

    expected = []

    assert result == expected