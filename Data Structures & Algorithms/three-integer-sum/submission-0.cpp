class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> ans;

        std::sort(nums.begin(), nums.end());
        unordered_map<int, int> key;
        for (int i = 0; i < nums.size();++i){
            key[nums[i]]++;
        }

        for (int i = 0; i < nums.size(); i++) {
            key[nums[i]]--;
            if (i > 0 && nums[i] == nums[i - 1]) continue;

            for (int j = i + 1; j < nums.size(); j++) {
                key[nums[j]]--;
                if (j > i + 1 && nums[j] == nums[j - 1]) continue;

                int target = -(nums[i] + nums[j]);
                if (key[target] > 0) {
                    ans.push_back({nums[i], nums[j], target});
                }
            }

            for (int j = i + 1; j < nums.size(); j++) {
                key[nums[j]]++;
            }
        }

        return ans;
    }
};
