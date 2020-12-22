"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""

"""
1. Validate the constraints
2. Sort the existing array with key as index=0 for every tuple in array
3. arr[-1] always returns the last element in arr.
if interval[i][1] < interval[j][0] then update the tuple[1] added to new array
else append to the new array  

"""


def merge(intervals):
    # intevals = [[1,3],[8,10],[15,18],[2,6],,[3,12]]
    for interval in intervals:
        if len(interval) >= 2 or len(interval) < 2:
            return False
    intervals.sort(key=lambda x: x[0])
    # after_sort = [[1,3],[2,6],[3,12],[8,10],[15,18]]
    updated_intervals = []
    for interval in intervals:
        if not updated_intervals or updated_intervals[-1][1] < interval[0]:
            updated_intervals.append(interval)
        else:
            updated_intervals[-1][1] = max(interval[1],
                                           updated_intervals[-1][1])
    return updated_intervals
