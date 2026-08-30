import re

class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0: return ""

        encoded = ""

        for i, word in enumerate(strs):
            delimiter = f"###{len(word)}###"
            encoded += word + delimiter

        return encoded

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []

        pattern = r"(###\d+###)"
        result = re.split(pattern, s)
        decoded = []
        
        # Drop last index if empty
        if result[-1] == '': 
            result.pop()

        for i in range(0, len(result), 2):
            number = int(result[i+1].strip('#'))
            if number > 0:
                decoded.append(result[i])
            else:
                decoded.append("")

        return decoded
