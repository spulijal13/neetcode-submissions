class Solution {
public:

    string encode(vector<string>& strs) {
        string code = "";
        for (auto str : strs){
            code += str + "\n";
        }

        return code;
    }

    vector<string> decode(string s) {
        string word=""; 
        vector<string> ans;
        for (auto v : s){
            string value(1, v);
            if (value == "\n"){
                ans.push_back(word);
                word = "";
                continue;
            }
            word += value;
        }

        return ans;
    }
};
