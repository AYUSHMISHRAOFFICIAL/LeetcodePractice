import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        // Map to store the value and its index
        Map<Integer, Integer> numMap = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            
            // If the complement exists in our map, we found the pair
            if (numMap.containsKey(complement)) {
                return new int[] { numMap.get(complement), i };
            }
            
            // Otherwise, add the current number and its index to the map
            numMap.put(nums[i], i);
        }
        
        // Return an empty array as a fallback (the problem guarantees exactly one solution)
        return new int[] {};
    }
}