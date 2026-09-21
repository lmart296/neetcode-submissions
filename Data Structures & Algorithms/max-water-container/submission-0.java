class Solution {
    public int maxArea(int[] heights) {
        int i = 0, j = heights.length-1, maxArea = 0;
        while(i < j){
            int distance = j - i;
            if(heights[i] > heights[j]){
                maxArea = Math.max(heights[j] * distance, maxArea);
                j--;
            } else {
                maxArea = Math.max(heights[i] * distance, maxArea);
                i++;
            }
        }
        return maxArea;
    }
}
