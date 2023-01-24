"""
    배열의 K번째 큰 요소
    정렬을 이용한 풀이 : 입력값이 고정되어 있기 때문
"""
from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k - 1]