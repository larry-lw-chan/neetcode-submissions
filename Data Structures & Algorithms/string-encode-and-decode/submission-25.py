import re

class Solution:

    def encode(self, strs: List[str]) -> str:
        # Edge Case
        if len(strs) == 0:
            return ""

        # Set delimiter and encoded variable
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
        output = []
        # Drop last index if empty
        if result[-1] == '': result.pop()

        for i in range(0, len(result), 2):
            number = int(result[i+1].strip('#'))
            if number > 0:
                output.append(result[i])
            else:
                output.append("")

        return output
