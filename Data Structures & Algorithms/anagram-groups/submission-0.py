class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        ans_len = 0
        map_list = []
        for string in strs:
            contin = False
            hash_map = {}
            for s in string:
                hash_map[s] = 1 + hash_map.get(s, 0)
            
            for i, m in enumerate(map_list):
                if m == hash_map:
                    ans[i].append(string)
                    contin = True
                    break
            
            if contin:
                continue

            ans.append([])
            ans[ans_len].append(string)
            ans_len += 1
            map_list.append(hash_map)
        
        return ans


