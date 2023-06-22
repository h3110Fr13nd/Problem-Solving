from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict_letters = dict()
        len_s = len(s)
        len_max_substr = 0
        
        substr_start = 0
        substr_end = 0
        
        for i in range(len_s):
            if s[i] in dict_letters and dict_letters[s[i]]>=substr_start:
                if i-substr_start > len_max_substr:
                    len_max_substr = i - substr_start
                substr_start = dict_letters[s[i]]+1
            dict_letters[s[i]] = i
            substr_end+=1
            
        return max(len_max_substr , substr_end-substr_start)

def test():
    solution = Solution()
    assert solution.lengthOfLongestSubstring("abcabcbb") == 3
    assert solution.lengthOfLongestSubstring("bbbbb") == 1
    assert solution.lengthOfLongestSubstring("pwwkew") == 3
    assert solution.lengthOfLongestSubstring("") == 0
    assert solution.lengthOfLongestSubstring(" ") == 1
    assert solution.lengthOfLongestSubstring("au") == 2
    assert solution.lengthOfLongestSubstring("dvdf") == 3
    assert solution.lengthOfLongestSubstring("abba") == 2
    assert solution.lengthOfLongestSubstring("aab") == 2
    assert solution.lengthOfLongestSubstring("tmmzuxt") == 5
    assert solution.lengthOfLongestSubstring("ohvhjdml") == 6
    assert solution.lengthOfLongestSubstring("bpfbhmipx") == 7
    assert solution.lengthOfLongestSubstring("nfpdmpi") == 5
    assert solution.lengthOfLongestSubstring("aabaab!bb") == 3
    

if __name__ == "__main__":
    test()
    print("Passed All Testcases")

