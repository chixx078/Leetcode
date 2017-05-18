public class Solution {
    public int findUnsortedSubarray(int[] nums) {
        /* sort O(nlgn)
        
        int[] temp = nums.clone();
        int r1 = 0;
        int r2 = 0;
        Arrays.sort(nums);
        for(int i=0; i<nums.length;i++){
            if(temp[i]==nums[i]){
                r1++;
            }else{
                break;
            }
        }
        for(int i=nums.length-1; i>=0;i--){
            if(temp[i]==nums[i]){
                r2++;
            }else{
                break;
            }
        }
        int result = nums.length-r1-r2;
        if( result>0) return result;
        else return 0;
        */
        
        /*O(n) 
        
        Examples:
        1) If the input array is [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60], your program should be able to find that the subarray lies between the indexes 3 and 8.
        
        2) If the input array is [0, 1, 15, 25, 6, 7, 30, 40, 50], your program should be able to find that the subarray lies between the indexes 2 and 5.
        
        Solution:
        1) Find the candidate unsorted subarray 
        a) Scan from left to right and find the first element which is greater than the next element. Let s be the index of such an element. In the above example 1, s is 3 (index of 30).
        b) Scan from right to left and find the first element (first in right to left order) which is smaller than the next element (next in right to left order). Let e be the index of such an element. In the above example 1, e is 7 (index of 31).
        
        2) Check whether sorting the candidate unsorted subarray makes the complete array sorted or not. If not, then include more elements in the subarray.
        a) Find the minimum and maximum values in arr[s..e]. Let minimum and maximum values be min and max. min and max for [30, 25, 40, 32, 31] are 25 and 40 respectively.
        b) Find the first element (if there is any) in arr[0..s-1] which is greater than min, change s to index of this element. There is no such element in above example 1.
        c) Find the last element (if there is any) in arr[e+1..n-1] which is smaller than max, change e to index of this element. In the above example 1, e is changed to 8 (index of 35)
        
        3) Print s and e.
        */
        
        int n = nums.length;
        int start=0; 
        int end=n-1;
        for(start=0;start<n-1;start++){
            if(nums[start]>nums[start+1]) break;
        }
        if(start==n-1) return 0;
        
        for(end=n-1;n>0;end--){
            if(nums[end]<nums[end-1]) break;
        }
        
        int max = nums[start];
        int min = nums[start];
        for(int i=start+1;i<=end;i++){
            max=Math.max(max,nums[i]);
            min=Math.min(min,nums[i]);
        }
        
        for(int i=0;i<start;i++){
            if(nums[i]>min) start=i;
        }
        for(int i=n-1;i>end;i--){
            if(nums[i]<max) end=i;
        }
        return end-start+1;
        
    }
}
