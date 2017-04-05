public class Solution {
    public String largestNumber(int[] nums) {
        //how to compare the following strings? 
        //30 ^ 3 = 303
        //3 ^ 30 = 330
        //use Comparator to override compare method
        
        if (nums.length==0){
            return "";
        }
        
        String[] nums_s = new String[nums.length];
        for(int i=0;i<nums.length;i++){
            nums_s[i]=String.valueOf(nums[i]);
        }
        
        Comparator<String> comp = new Comparator<String>(){
            @Override
            public int compare(String str1, String str2){
                String s1 = str1 + str2;
                String s2 = str2 + str1;
                return s2.compareTo(s1); //return 1 0 -1, sort in opposite way so append later
            }
        };
        
        //The java.util.Arrays.sort(T[] a, Comparator<? super T> c) method sorts the specified array of objects according to the order induced by the specified comparator. All elements in the array must be mutually comparable by the specified comparator (that is, c.compare(e1, e2) must not throw a ClassCastException for any elements e1 and e2 in the array).
        Arrays.sort(nums_s, comp);
        
        //edge case: what if the array is full of 0's?
        if(nums_s[0].charAt(0)=='0'){
            return "0";
        }
        
        StringBuilder sb = new StringBuilder();
        for(String s : nums_s){
            sb.append(s);
        }
        
        return sb.toString();
    }
}
