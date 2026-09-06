class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for string in strs:
            word = [0] * 26
            for letter in string:
                word[ord(letter) - ord('a')] += 1

            anagrams[tuple(word)].append(string)
    
        return list(anagrams.values())

