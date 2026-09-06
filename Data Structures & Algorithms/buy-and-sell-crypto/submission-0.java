class Solution {
    public int maxProfit(int[] prices) {
        int bd = 0;
        int sd = 1;
        int max_profit = 0;
        int n = prices.length;
        while (sd < n){
            if (prices[sd] > prices[bd]){
                int profit = prices[sd] - prices[bd];
                max_profit = Math.max(max_profit, profit);
            }else {
                bd = sd;
            }
            sd++;
        }

        return max_profit;
    }
}
