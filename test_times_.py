from times import time_range, compute_overlap_time
import pytest

# Combine all positive tests into one parameterized test
@pytest.mark.parametrize("range1_args, range2_args, expected_overlap, test_id", [
    (
        # Test case 1: From test_given_input (multiple intervals, complex overlap)
        ("2010-01-12 10:00:00", "2010-01-12 12:00:00"), 
        ("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60),
        [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')],
        "given_input_overlap"
    ),
    (
        # Test case 2: From test_no_overlap / test_no_overlap_ranges
        ("2021-01-01 12:00:00", "2021-01-01 13:00:00"),
        ("2021-01-01 14:00:00", "2021-01-01 15:00:00"),
        [],
        "no_overlap"
    ),
    (
        # Test case 3: From test_multiple_intervals_each (full overlap)
        ("2010-01-12 10:00:00", "2010-01-12 10:20:00", 2, 0),
        ("2010-01-12 10:00:00", "2010-01-12 10:20:00", 2, 0),
        [('2010-01-12 10:00:00', '2010-01-12 10:10:00'), ('2010-01-12 10:10:00', '2010-01-12 10:20:00')],
        "multiple_intervals_full_overlap"
    ),
    (
        # Test case 4: From test_touching_endpoints / test_edge_case_no_overlap
        ("2010-01-12 10:00:00", "2010-01-12 10:30:00"),
        ("2010-01-12 10:30:00", "2010-01-12 11:00:00"),
        [],
        "touching_endpoints_no_overlap"
    )
])
def test_compute_overlap(range1_args, range2_args, expected_overlap, test_id):
    """
    Tests compute_overlap_time with various scenarios, including
    overlaps, no overlaps, and multiple intervals.
    """
    # Create the time ranges using the provided arguments
    r1 = time_range(*range1_args)
    r2 = time_range(*range2_args)
    
    # Compute the overlap
    result = compute_overlap_time(r1, r2)
    
    # Assert the result is as expected
    assert result == expected_overlap

# Keep the negative test (checking for errors) separate
def test_invalid_time_range():
    """
    Tests that time_range raises a ValueError when the end_time
    is before the start_time.
    """
    with pytest.raises(ValueError):
        time_range("2022-01-01 12:00:00", "2022-01-01 10:00:00")