class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        map<int, int> count;
        for (auto n : nums){
            if (++count[n] > 1) return true;
        }

        return false;
    }
};