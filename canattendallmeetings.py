# Given meeting intervals [start,end] return True if none of them overlap.
# Problem : Given an array of meeting time intervals where each interval is represented as [start,end] return True
# If a person can attend all the meetings (no two meetings overlap), return True otherwise return False

# If meetings are listed in random order, checking every pair overlaps takes O(N^2) time
# However, if we sort the meetings chronoligically by their start time
# 1. We only need to check adjacent meetings
# 2. An overlap occurs if a meeting starts before previous meeting finishes.
# 3. For two adjacent meetings, M1 = [start1,end1]  and M2 = [start2,end2] (where start1 <= start2)
# Overlap occurs if start2 < start1

def can_attend_meetings(intervals: list[list[int]]) -> bool:
    # Step 1 : Sort intervals chronologically by their start time
    intervals.sort(key = lambda x : x[0])
    
    # Step 2 : Compare each meeting with the right one before it
    for i in range (1, len(intervals)):
        
        # intervals[i] gets the current meeting interval, which looks like [start, end].
        # [0] accesses the first number of that list, which is the start time of the current meeting.
        current_start = intervals[i][0]
        
        # intervals[i-1] looks at the previous meeting in the sorted list.
        # [1] accesses the second number of that list, which is the end time of the previous meeting.
        prev_end = intervals[i-1][1]
        
        # Because the meetings are sorted by start time, the previous meeting started first. 
        # For us to attend both meetings without a conflict.
        # If current_start < prev_end, it means the new meeting is trying to start before the last meeting has actually finished!
        
        if current_start < prev_end:
            return False
    
    # If no overlaps were found after checking pairs, return True
    return True

intervals = [[0,30], [35,45], [45,50]]
print(can_attend_meetings(intervals))        