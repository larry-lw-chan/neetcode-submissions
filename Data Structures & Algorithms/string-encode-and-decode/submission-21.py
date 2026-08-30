class Solution:

    def encode(self, strs: List[str]) -> str:
        # Edge Case
        if len(strs) == 0:
            return "||NULL||"

        # Set delimiter and encoded variable
        delimiter = "||leetcode||"
        encoded = ""

        for i, word in enumerate(strs):
            if i >= len(strs) - 1: # don't add delimiter to last word
                encoded += word
            else:
                encoded += word + delimiter

        return encoded

    def decode(self, s: str) -> List[str]:
        delimiter = "||leetcode||"
        word_list = s.split(delimiter)

        # Generate new list, but ignore ||NULL||
        result = [word for word in word_list if word != "||NULL||"]
        
        return result
