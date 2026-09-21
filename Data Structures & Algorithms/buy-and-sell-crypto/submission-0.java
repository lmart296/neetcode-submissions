class Solution {
    public int maxProfit(int[] prices) {
        if(prices.length == 0 || prices.length == 1) return 0;
        
        int i = 0, j = i+1; 
        int profit = 0;

        while(j < prices.length){
            if(prices[i] <= prices[j]){
                profit = Math.max(profit, prices[j] - prices[i]);
                j++;
            } else {
                i++;
            }
        }
        return profit;
    }
}
