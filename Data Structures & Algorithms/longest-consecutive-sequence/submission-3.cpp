class Solution {
public:
    int longestConsecutive(vector<int>& nums) {

        if (nums.empty()){
            return 0;
        }

        std::sort(nums.begin(), nums.end());

        for (int j = 0; j < nums.size() ;++j){
            cout << nums[j] << ",";
        }
        cout << endl;

        int largest_count = 1;
        int count = 1;
        for (int i = 1; i < nums.size();++i){
            if (nums[i] == nums[i - 1]){
                continue;
            }else if (nums[i] == nums[i-1] + 1){
                count++;
            }else{
                largest_count = std::max(largest_count, count);
                count = 1;
            }
        }
        return std::max(largest_count, count);
    }
};
