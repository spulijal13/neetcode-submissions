class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int i = 0;
        int j = numbers.size() - 1;

        while (i < j){
            if (numbers.at(i) + numbers.at(j) > target){
                j--;
            }else if (numbers.at(i) + numbers.at(j) < target){
                i++;
            }else{
                return vector<int>{i+1, j+1};
            }
        }

        return vector<int>{};
    }
};
