class Solution {
    public int stoneGameVIII(int[] stones) {
        int n = stones.length;
        
        // Step 1: Calculate the prefix sums
        int[] prefix = new int[n];
        prefix[0] = stones[0];
        for (int i = 1; i < n; i++) {
            prefix[i] = prefix[i - 1] + stones[i];
        }
        
        // Step 2: Initialize DP with the base case (picking all stones)
        // If we pick all stones (index n-1), the game ends.
        int dp = prefix[n - 1]; 
        
        // Step 3: Work backwards to find the optimal move
        // We stop at 1 because we must remove more than one stone (x > 1).
        for (int i = n - 2; i >= 1; i--) {
            // Option 1: Don't take at this index (keep current dp)
            // Option 2: Take at this index (score is prefix[i] - next player's best)
            dp = Math.max(dp, prefix[i] - dp);
        }
        
        return dp;
    }
}