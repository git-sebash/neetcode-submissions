class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = {}
        outputList = []

        for word in range(len(strs)):
            key = ''.join(sorted(strs[word]))
            groups.setdefault(key, []).append(strs[word])
   
        return list(groups.values())



        

        