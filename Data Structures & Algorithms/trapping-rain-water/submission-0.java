class Solution {
    public int trap(int[] height) {
        if(height == null || height.length == 0){
            return 0;
        }

        int i = 0, j = height.length - 1;
        int leftMax = height[i], rightMax = height[j];
        int maxArea = 0;

        while(i < j){
            if(leftMax < rightMax){
                i++;
                leftMax = Math.max(leftMax, height[i]);
                maxArea += leftMax - height[i];
            } else {
                j--;
                rightMax = Math.max(rightMax, height[j]);
                maxArea += rightMax - height[j];
            }
        }

        return maxArea;
    }
}
