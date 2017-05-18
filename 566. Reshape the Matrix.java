public class Solution {
    public int[][] matrixReshape(int[][] nums, int r, int c) {
        int n = nums.length;
        int m = nums[0].length;
        if(r*c != m*n) return nums;
        
        int[][] result = new int[r][c];
        
        int row=0;
        int col=0;
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                result[row][col] = nums[i][j];
                col++;
                if(col==c){
                    col=0;
                    row++;
                }
            }
        }
        
        return result;
    }
}
