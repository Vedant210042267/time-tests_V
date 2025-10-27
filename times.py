import datetime
from pytest import raises

def time_range(start_time, end_time, number_of_intervals=1, gap_between_intervals_s=0):
    if start_time >= end_time:
        raise ValueError("start_time must be earlier than end_time")
    start_time_s = datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    end_time_s = datetime.datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")

    if end_time_s < start_time_s:
        raise ValueError(f"Invalid time range: end_time '{end_time}' is before start_time '{start_time}'")

    d = (end_time_s - start_time_s).total_seconds() / number_of_intervals + gap_between_intervals_s * (1 / number_of_intervals - 1)
    sec_range = [(start_time_s + datetime.timedelta(seconds=i * d + i * gap_between_intervals_s),
                  start_time_s + datetime.timedelta(seconds=(i + 1) * d + i * gap_between_intervals_s))
                 for i in range(number_of_intervals)]
    return [(ta.strftime("%Y-%m-%d %H:%M:%S"), tb.strftime("%Y-%m-%d %H:%M:%S")) for ta, tb in sec_range]


def compute_overlap_time(range1, range2):
    def to_dt(s):
        return datetime.datetime.strptime(s, "%Y-%m-%d %H:%M:%S")
    
    overlap_time = []
    for start1, end1 in range1:
        start1_dt, end1_dt = to_dt(start1), to_dt(end1)
        for start2, end2 in range2:
            start2_dt, end2_dt = to_dt(start2), to_dt(end2)
            low = max(start1_dt, start2_dt)
            high = min(end1_dt, end2_dt)
            if low < high:
             overlap_time.append((
                    low.strftime("%Y-%m-%d %H:%M:%S"),
                    high.strftime("%Y-%m-%d %H:%M:%S"),
             ))

    return overlap_time

if __name__ == "__main__":
    large = time_range("2010-01-12 13:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    print(compute_overlap_time(large, short))