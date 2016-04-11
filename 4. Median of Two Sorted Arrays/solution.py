class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        lens = len(nums1) + len(nums2)
        if 1 & lens:
            return self.findKthSortedArrays(nums1,nums2,lens/2 + 1)
        else:
            return (self.findKthSortedArrays(nums1, nums2, lens/2) + self.findKthSortedArrays(nums1, nums2, lens/2 + 1))/2.0
        
        
    def findKthSortedArrays(self,A,B,K):
        if len(A) > len(B):
            return self.findKthSortedArrays(B,A,K)
        la,lb,pa,pb = len(A), len(B), min(K/2, len(A)), K - min(K/2, len(A))
        if la == 0:
            return B[K-1]
        if K == 1:
            return min(A[0],B[0])
        
        if A[pa-1] < B[pb-1]:
            return self.findKthSortedArrays(A[pa:],B,K - pa)
        elif A[pa-1] > B[pb-1]:
            return self.findKthSortedArrays(A,B[pb:],K - pb)
        else:
            return A[pa-1]
            