class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> hash_map = new HashMap<Integer, Integer>();

        for (int i = 0; i < nums.length;i++){
            int diff = target - nums[i];

            if (hash_map.containsKey(diff)){
                return new int[]{hash_map.get(diff), i};
            }

            hash_map.put(nums[i], i);
        }

        return new int[] {};
    }
}
